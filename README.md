# Modbus-cmd

A tiny program that provides to easy access modbus devices

# Usage

```
usage: modbus.py [-h] [-p PORT] [-b BAUDRATE] [-u UNIT] [-c C] [-a ADDR] [--value VALUE]

A tiny program that provides to easy access modbus devices

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  tty device name
  -b BAUDRATE, --baudrate BAUDRATE
                        baud rate
  -u UNIT, --unit UNIT  unit number that you communication to
  -c C                  command (ri: read input register, rh: read holding register, w: write
                        register)
  -a ADDR, --addr ADDR  register address to read or write
  --value VALUE         Optional: value to write

You need to have a suitable priviledge of tty device.
```

# Setup

- sudo apt install python3-pymodbus

# Example

## Read Input Register

```(bash)
$ python3 modbus.py -u 10 -c ri -a 0x01f4 -b 4800
port: /dev/ttyUSB0, baud rate: 4800, unit: 10, command: ri, address: 500, value: None
read value is 649
```

## Read Holding Register

```(bash)
$ python3 modbus.py -u 20 -c rh -a 0x07d1 -b 4800
port: /dev/ttyUSB0, baud rate: 4800, unit: 20, command: rh, address: 2001, value: None
read value is 1
```

## Write Register

```(bash)
$ python3 modbus.py -u 21 -c w -a 0x07d1 --value 1
port: /dev/ttyUSB0, baud rate: 9600, unit: 21, command: w, address: 2001, value: 1
wrote value 1 to address 2001 of 21
```

