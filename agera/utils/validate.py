# -*- coding: utf-8 -*-

import functools
import inspect
import re

import logging

from flask import request

from agera.utils.exc import (
    APIError,
    MissingParameter,
    ParameterFormatError,
)


class Field(object):
    __type__ = None
    __description__ = u''

    def __init__(self, message=None, check=None, **kwargs):
        self._message = message
        if check is not None and not hasattr(check, '__call__'):
            raise Exception("check has no attr '__call__'")
        self._check = check

    def convert(self, val):
        if self.__type__ is None:
            raise NotImplementedError
        try:
            return self.__type__(val)
        except ValueError:
            raise ParameterFormatError(
                u'{}不是有效的{}'.format(val, self.__description__))


class ListField(Field):
    __description__ = u'列表类型'

    def __init__(self, field, seperate=',', **kwargs):
        self._field = field
        if isinstance(field, type) and issubclass(field, Field):
            self._field = field()
        self._seperate = seperate
        super(ListField, self).__init__(**kwargs)

    def convert(self, val):
        if not val:
            return []
        if request.method == 'GET' and self._seperate is not None:
            val = [x.strip() for x in val.split(self._seperate)]
        if not isinstance(val, list):
            raise ParameterFormatError(u'不是有效的列表类型')
        return [self._field.convert(x) for x in val]


class IntField(Field):
    __type__ = int
    __description__ = u'整数'


class StringField(Field):
    __description__ = u'字符串'

    def __init__(self, pattern='.*', **kwargs):
        self._pattern = re.compile(pattern)
        super(StringField, self).__init__(**kwargs)

    def convert(self, val):
        match = self._pattern.match(val)
        if not match:
            raise ParameterFormatError(self._message or u'正则匹配失败')
        return match.group()


class BoolField(Field):
    __type__ = bool
    __description__ = u'布尔值'

    def convert(self, val):
        try:
            return bool(int(val))
        except ValueError:
            raise ParameterFormatError(u'不是有效的布尔值')


class FloatField(Field):
    __type__ = float
    __description__ = u'小数'


class validator(object):

    def __init__(self, fields):
        for param, field in fields.iteritems():
            if isinstance(field, type) and issubclass(field, Field):
                fields[param] = field()
        self._fields = fields

    def __call__(self, func):
        logger = logging.getLogger(func.__module__)

        r = inspect.getargspec(func)
        defaults = r.defaults or []

        self.injectors = []

        for index, arg in enumerate(r.args):
            name = r.args[index]
            if name not in self._fields:
                raise Exception(
                    '\'{}\' field not defined in {}.{}'.format(
                        name, func.__module__, func.__name__))

            _index = index + len(defaults) - len(r.args)
            # injector (name, is_optional, default)
            injector = (name, 1, defaults[_index]) \
                if _index >= 0 else (name, 0, None)
            self.injectors.append(injector)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            params = self.__get_request_params()

            args = []
            kwargs = {}
            for injector in self.injectors:
                name, optional, default = injector
                if not optional and name not in params:
                    raise MissingParameter(name)
                val = params.get(name, default)

                # validate and convert
                field = self._fields[name]
                if optional:
                    kwargs[name] = val if val is None else field.convert(val)
                else:
                    args.append(field.convert(val))

            try:
                return func(*args, **kwargs)
            except APIError as ae:
                message = u"{0} => {1}{2}{3}".format(
                    repr(ae), func.__name__, args, kwargs)
                logger.warning(message)
                raise
            except Exception as e:
                logger.exception("{0} => {1}{2}{3}".format(
                    repr(e), func.__name__, args, kwargs))
                raise

        return wrapper

    def __get_request_params(self):
        params = request.json or {}
        if request.method == 'GET':
            for key, val in dict(request.args).iteritems():
                params[key] = val[0] if isinstance(val, list) else val
        if request.method == 'POST':
            for key, val in dict(request.form).iteritems():
                params[key] = val[0] if isinstance(val, list) else val
        params.update(request.view_args)
        return params
