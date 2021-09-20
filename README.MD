
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# pybicyclewheel 

`pybicyclewheel` calulates the required spoke length for bicycle wheels.


# further readings

wikipedia
- [bicycle wheels](https://en.wikipedia.org/wiki/Wheelbuilding)
- [spoke length](https://en.wikipedia.org/wiki/Spoke#Spoke_length)

bicycle guru doc
- [sheldon brown](https://www.sheldonbrown.com/spoke-length.html)
- [christian smolik](http://www.smolik-velotech.de/laufrad/06einsp.htm#Ermittlung%20der%20Speichenl%C3%A4ngen)

## remark

the calculation methods mentioned above differ sligthly from each other by putting e.g. spoke hole, or spoke radius
into consideration or not. 
the provided method within this module uses a mathematic 3d geometric vector and matrix based approach
to determine the length of a spoke using [`numpy`](https://en.wikipedia.org/wiki/NumPy). 


# how to use

maintain your rim and hub data in the xls sheets provided in the github repo

- [hub data xls](https://github.com/kr-g/pybicyclewheel/blob/main/hubs.xls)
- [rim data xls](https://github.com/kr-g/pybicyclewheel/blob/main/rims.xls)


call the [`simple gui`](https://github.com/kr-g/pybicyclewheel/tree/main/pybicyclewheel_gui)
with (remark: hubs.xls, and rims.xls base dir is "~/Downloads")

    python3 -m pybicyclewheel_gui
    
    
or use it along with [`sample.py`](https://github.com/kr-g/pybicyclewheel/blob/main/sample.py).


alternatively explore [`xls_calc.py`](https://github.com/kr-g/pybicyclewheel/blob/main/pybicyclewheel/xls_calc.py)
and use the classes directly (less convinient).


probably a better user interface (then the simple one) will be provided later ... (if i have time i will do)



## structure of the xls - sizing data

todo...


## where to find sizing data 

browse the manufacturer web site and search for specification

- shimano [https://productinfo.shimano.com/#/spec](https://productinfo.shimano.com/#/spec)
- ...

or search for the product detail page



# What's new ?

Check
[`CHANGELOG`](https://github.com/kr-g/pybicyclewheel/blob/main/CHANGELOG.MD)
for latest ongoing, or upcoming news


# Platform

Tested on Python3, and Linux.


# development status

alpha state.
the API or logical call flow might change without prior notice.

read [`CHANGELOG`](https://github.com/kr-g/pybicyclewheel/blob/main/CHANGELOG.MD)
for latest, or upcoming news.


# installation

available on pypi. install with:

    python3 -m pip install pybicyclewheel
    
