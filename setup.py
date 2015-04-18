from setuptools import setup, find_packages

requires = []

setup(
    name='agera',
    version='0.1',
    description='Web API for Koenig',
    author='YUCHI',
    author_email='wei.chensh@ele.me',
    packages=find_packages(),
    url='https://github.com/streethacker/agera',
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)
