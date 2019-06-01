<img src="logo.png" width="150px">

[![Build Status](https://travis-ci.com/securisec/saramBinja.svg?branch=master)](https://travis-ci.com/securisec/saramBinja)

# saramBinja
A python plugin to integrate [Binary Ninja](https://binary.ninja/) with Saram. 

**This is a python 2 plugin**

## Installation
Clone this repository in your Binary Ninja plugin directory. If you successfully installed it, you will see it appear in the startup log of Binary Ninja.

## Usage
The `saramBinja` plugin is designed to be run from the python interpreter within Binary Ninja. To load the python prompt in Binary Ninja, one can use `ctrl + ``.

The main class is instantiated with the `bv` object from Binary Ninja. Some of the methods will require the `current_function` object from Binja. From within the prompt, do:
```
from saramBinja import SaramBinja; saram = SaramBinja('avalidentrytoken', bv)
```

Then you can execute one of the available methods by:
```
saram.snb_current_function_comments(current_function).send()
```

The methods currently avaialble are:

- snb_get_strings
- snb_get_functions
- snb_current_function_comments
- snb_current_function_references