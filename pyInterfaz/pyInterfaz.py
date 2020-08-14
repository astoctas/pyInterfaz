from pymata4 import pymata4
import threading
from inspect import signature


class pyInterfaz(pymata4.Pymata4):

    def __init__(self, com_port=None):
        self._analogs = [self.__Analog(self, 0)]
        self._digitals = [self.__Digital(self, 14)]

        super().__init__(com_port=com_port, baud_rate=57600, arduino_wait=1)

    def analog(self, index):
        if index < 1: index = 1
        return self._analogs[index - 1];

    def digital(self, index):
        if index < 1: index = 1
        return self._digitals[index - 1];


    class __Sensor:
        def __init__(self):
            self.changeCallback = None
            pass

        def processCallback(self, callback):
            self.changeCallback = callback

        def _changecb(self, data):
            if not (self.changeCallback is None):
                sig = signature(self.changeCallback)
                params = len(sig.parameters)
                if params == 1:
                    self.changeCallback(data[2])
                elif params == 2:
                    self.changeCallback(data[2], data[3])


    class __Analog(__Sensor):
        def __init__(self, interfaz, index):
            self.interfaz = interfaz
            self.index = index
            super().__init__()

        def on(self, callback):
            self.processCallback(callback)
            self.interfaz.set_pin_mode_analog_input(self.index, self._changecb)

        def off(self):
            self.interfaz.disable_analog_reporting(self.index)

        def read(self):
            return self.interfaz.analog_read(self.index)[0]


    class __Digital(__Sensor):
        def __init__(self, interfaz, index):
            self.interfaz = interfaz
            self.index = index
            super().__init__()

        def on(self, callback):
            self.processCallback(callback)
            self.interfaz.set_pin_mode_digital_input(self.index, self._changecb)

        def off(self):
            self.interfaz.disable_digital_reporting(self.index)

        def read(self):
            return self.interfaz.digital_read(self.index)[0]



    def __shiftout(self, dataPin, clockPin, isBigEndian = False, value = None):
        if value is None:
            value = isBigEndian
            isBigEndian = True
        for i in range(0, 7):
            self.digital_write(clockPin, 0)
            if isBigEndian:
                self.digital_write(dataPin,  (value & (1 << (7 - i ))) | 0)
            else:
                self.digital_write(dataPin,  (value & (1 << i )) | 0)
            self.digital_write(clockPin, 1)




