import argparse

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client.sync import ModbusSerialClient

def main():
    parser = argparse.ArgumentParser(
                    prog='modbus.py',
                    description='A tiny program that provides to easy access modbus devices',
                    epilog='You need to have a suitable priviledge of tty device.')
    parser.add_argument('-p', '--port', help='tty device name', type=str, default='/dev/ttyUSB0')
    parser.add_argument('-b', '--baudrate', help='baud rate', type=int, default=9600)
    parser.add_argument('-u', '--unit', help='unit number that you communication to', type=int, default=1)
    parser.add_argument('-c', help='command (ri: read input register, rh: read holding register, w: write register)', type=str, default='ri')
    parser.add_argument('-a', '--addr', help='register address to read or write', type=lambda x: int(x,0), default=0x0000)
    parser.add_argument('--value', help='Optional: value to write', type=int)

    args = parser.parse_args()
    print(f'port: {args.port}, baud rate: {args.baudrate}, unit: {args.unit}, command: {args.c}, address: {args.addr}, value: {args.value}')
    
    with ModbusSerialClient(method='rtu', port=args.port, baudrate=args.baudrate) as c:
        if c.connect():
            if args.c == 'ri':
                res = c.read_input_registers(address=args.addr, count=1, unit=args.unit)
                if res.isError():
                    raise Exception(f'Read error from a unit ({args.unit}) with {args.addr}')
                else:
                    v = BinaryPayloadDecoder.fromRegisters(res.registers, byteorder=Endian.Big, wordorder=Endian.Big)
                    print(f'read value is {v.decode_16bit_int()}')
            elif args.c == 'rh':
                res = c.read_holding_registers(address=args.addr, count=1, unit=args.unit)
                if res.isError():
                    raise Exception(f'Read error from a unit ({args.unit}) with {args.addr}')
                else:
                    v = BinaryPayloadDecoder.fromRegisters(res.registers, byteorder=Endian.Big, wordorder=Endian.Big)
                    print(f'read value is {v.decode_16bit_int()}')
            elif args.c == 'w':
                if args.value is not None:
                    res = c.write_register(address=args.addr, value=args.value, unit=args.unit)
                    print(f'wrote value {args.value} to address {args.addr} of {args.unit}')
                else:
                    raise Exception('No value is specified')
        else:
            print(f'Could not connect {args.port}, {args.baudrate}')


if __name__ == "__main__":
    main()

