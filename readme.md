# Saturated Reverse Polish Notation(SRPN) Calculator

## Description
SRPN is a reverse polish notation calculator with the extra feature that all arithmetic is saturated. For instance, when it reaches the maximum value that can be stored in a variable, it stays at the maximum rather than wrapping around.

A program is written to match the functionality of SRPN as closely as possible. Four categories of tests and example test data are provided:
* Single operations
* Multiple operations
* Saturation
* Obscure functionality

## Automated Tests
``` [srpn.py](https://github.com/fir3buster/SRPN/blob/main/SRPN/srpn.py) ``` contains the all the functionality to pass the standard test data.
``` [mark-code.py](https://github.com/fir3buster/SRPN/blob/main/mark-code.py)``` is a test script to run all the example inputs.

``` python mark-code.py
```
