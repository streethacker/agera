## Agera

!['koenig'](./icon.jpg)

__Agera__ is a bundle of __Web APIs__, which implemented by [__Flask__](https://github.com/mitsuhiko/flask) and designed to used in conjunction
with [__Koenig__](https://github.com/streethacker/koenig);

__Agera__ plays a role of the middleman between the data service and the fore-end display logic.

The whole project will contain 3 parts. Another two parts are:

* __Koenig__ is a bundle of data service APIs, running as a server in the whole system;

* __Wheels__ is a fore-end project, mostly implemented by Angular JS;


## Quick Start


### Requirements

Installation of __Agera__ needs no pre-requisitions, but to run it correctly, [__Koenig__](https://github.com/streethacker/koenig) is required.

### Installation

Install as developer

```
$ make develop
```

Install as package

```
$ make install
```

More options

```
$ make help
```

### Development

Run server, suppose that you put the package to your home directory:

```
$ cd ~/agera/agera
```

then simply run:

```
$ python server
```
