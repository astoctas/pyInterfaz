from pyInterfaz.pyInterfaz import i32
import time

def adata(d):
    print(d)
    #print(a.values.get(0))

i = i32("/dev/ttyUSB1")
i.input(4).on(adata);
#i.analog[3].enable_reporting();
#i.sp.write([0xc3,0x01]);

i.loop();


i.output(1).speed(100)
i.output(1).on()
i.output(1).direction(1)
time.sleep(2)
i.output(1).direction(0)
time.sleep(2)
i.output(1).direction(1)
time.sleep(2)
i.output(1).inverse()
time.sleep(2)
i.output(1).inverse()
time.sleep(2)


#i.output(1).inverse()
#time.sleep(2)
#i.output(1).inverse()
#time.sleep(2)
i.output(1).off()

#i.joystick().data(adata).on()

i.loop();
exit();



a = i.i2c(0x48)
operation = 4 | 0 | (0B01000000&0B01000000);

a.write(operation)
a.data(adata)
a.read_continuous(4)



i.report_dispatch.update({4: [_report_joystick, 1]})

time.sleep(3)
i._send_sysex(4);

while True:
    pass

time.sleep(3)





exit();

i.set_pin_mode_i2c();
global x
x = 0

def hola(d):
    #print ('%d %d %d %d' % (d[3], d[4] >> 7, d[5], d[5] >> 7))
    print(d)

i.set_sampling_interval(10)
# i.i2c_write(0x48, [operation])
operation = 0 | 0 | (0B01000000&0B01000000);
i.i2c_write(0x48, [operation]);

for j in range(1000):
    i.i2c_read(0x48, None, 1, hola)
    time.sleep(0.02)

while True:
    pass
    #print(i.i2c_read_saved_data(0x48))
time.sleep(0.05)
time.sleep(3)
exit();

"""

[6, 72, 68, 210, 209, 254, 87, 137, 1597964783.0892673]
[6, 72, 68, 209, 211, 220, 91, 137, 1597964802.792048]
[6, 72, 68, 211, 247, 220, 77, 137, 1597964820.1682987]

i.set_pin_mode_digital_output(7)
i.set_pin_mode_pwm_output(6)
i.digital_pin_write(7,1)
i.pwm_write(6,10)

time.sleep(3)
exit()


i.analog(0).on(None)


i.output(0).on()
time.sleep(2)
i.output(0).inverse()
time.sleep(2)
i.output(0).direction(0)
time.sleep(2)
i.output(0).speed(50)
time.sleep(2)
i.output(0).off()
time.sleep(2)
"""

i.servo(2).position(10)

exit()

#i._send_sysex(2, [0, 0]);

print(len("abc"))
for char in ("abc"):
    print(ord(char))

i._send_sysex(3, [1, 251 & 0x7F, 251 >> 7])

exit();

def hola(d, t):
    print(d, t)

#i.digital(1).change(hola)
#i.digital(1).on();
i.digital(0).on(hola)
#i.enable_digital_reporting(14)
time.sleep(5)
i.digital(0).off()
print(i.digital(0).read())
time.sleep(5)

print("Stop!")




