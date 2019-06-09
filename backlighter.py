from socket import socket, AF_INET, SOCK_DGRAM
from sys import argv


HOST, PORT = ADDR = '127.0.0.1', 58043


if len(argv) != 3:
    print('Wrong count of arguments')
    quit(1)
else:
    cmd = {
        'change': 'BRGHT_CHANGE',
        'set': 'BRGHT_SET',
        'min_set': 'MIN_BRGHT_SET'
    }.get(argv[1], None)
    if cmd is None:
        print('Wrong argument -> "' + argv[1] + '"')
        quit(1)

    try:
        value = int(argv[2])
    except ValueError:
        print('Wrong argument -> "' + argv[2] + '"')
        quit(1)
    else:
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.connect(ADDR)
        sock.sendall((cmd + ' ' + str(value)).encode())
        sock.close()
