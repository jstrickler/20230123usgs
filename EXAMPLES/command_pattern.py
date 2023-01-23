#
from abc import ABCMeta, abstractmethod

class Command(object):
    '''Command "interface"'''
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self): pass


class Fan(object):

    def start_rotate(self):
        print("Fan is rotating")

    def stop_rotate(self):
        print("Fan is not rotating")


class Light(object):

    def turn_on(self):
        print("Light is on")


    def turn_off(self):
        print("Light is off")


class Switch(object):

    def __init__(self, on, off):
        self.on_command = on
        self.off_command = off

    def on(self):
        self.on_command.execute()

    def off(self):
        self.off_command.execute()


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


class FanOnCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.start_rotate()

class FanOffCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.stop_rotate()

if __name__ == '__main__':
    light = Light()
    light_on_command = LightOnCommand(light)
    light_off_command = LightOffCommand(light)

    light_switch = Switch(light_on_command, light_off_command)
    light_switch.on()
    light_switch.off()

    fan = Fan()
    fan_on_command = FanOnCommand(fan)
    fan_off_command = FanOffCommand(fan)

    fan_switch = Switch(fan_on_command, fan_off_command)
    fan_switch.on()
    fan_switch.off()



