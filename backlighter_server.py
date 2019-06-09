#!/usr/bin/python3

from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR


class Backlighter:
    BACKLIGHT_DIR = '/sys/class/backlight/amdgpu_bl0'

    def __init__(self, min_brightness):
        self.brightness_dir = Backlighter.BACKLIGHT_DIR + '/brightness'

        f = open(Backlighter.BACKLIGHT_DIR + '/max_brightness')
        self.max_brightness = int(f.read())
        f.close()

        self.percent = self.max_brightness / 100
        self.min_brightness = min_brightness * self.percent

    def change_brightness(self, delta_percent):
        f = open(self.brightness_dir)
        current_brightness = int(f.read())
        f.close()

        new_brightness = current_brightness / self.max_brightness * 100 + delta_percent
        self.set_brightness(new_brightness)

    def set_brightness(self, brightness):
        new_brightness = brightness * self.percent

        if new_brightness < self.min_brightness:
            new_brightness = self.min_brightness

        if new_brightness > self.max_brightness:
            new_brightness = self.max_brightness

        f = open(self.brightness_dir, 'w')
        f.write(str(int(new_brightness)))
        f.close()

    def set_min_brightness(self, min_brightness):
        if min_brightness < 0:
            min_brightness = 0
        if min_brightness > self.max_brightness:
            min_brightness = self.max_brightness

        self.min_brightness = min_brightness

    def start_server(self, host, port):
        sock = socket(AF_INET, SOCK_DGRAM)
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.bind((host, port))

        print('Server started...')
        while True:
            data = sock.recv(1024)
            if not data:
                continue

            data = data.decode().split()
            print('Got command "' + ' '.join(data) + '"')
            if len(data) > 2:
                print('Command is not valid')
                continue

            try:
                if data[0] == 'BRGHT_CHANGE':
                    self.change_brightness(int(data[1]))
                elif data[0] == 'BRGHT_SET':
                    self.set_brightness(int(data[1]))
                elif data[0] == 'MIN_BRGHT_SET':
                    self.set_min_brightness(int(data[1]))
                print('Command executed.')
            except ValueError:
                print('Command is not valid')
                continue


if __name__ == '__main__':
    HOST, PORT = ADDR = '127.0.0.1', 58043
    DEFAULT_MIN_BRIGHTNESS = 10
    back = Backlighter(DEFAULT_MIN_BRIGHTNESS)
    back.start_server(HOST, PORT)
