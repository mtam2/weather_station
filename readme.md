# Weather Station v0.1
## Requirements
### Hardware
1. Linux Box (I'm using a Raspberry Pi 3)
1. TemperUSB Stick (https://www.amazon.com/Jepeak-Thermometer-Temperature-Record-Laptop/dp/B009YRP906)
### Software
1. Python 2.7
1. Native Ubuntu (Can't use VM due to segmentation faults)
## Setup
1. Run the following commands
```
sudo apt-get update
sudo apt-get install python-usb python-setuptools snmpd # The latter is only necessary for SNMP-usage.
sudo easy_install snmp-passpersist
```
1. Change directory into the temper-python folder and run `sudo python setup.py install`
1. Test the temperature reading by running `sudo temper-poll`
1. `pip install flask`
1. `python flaskServer.py`
### Credit
Thank https://github.com/padelt/temper-python for the TemperUSB Python library
