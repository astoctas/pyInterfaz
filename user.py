from pyInterfaz.pyInterfaz import pyInterfaz
import time
i = pyInterfaz()


def hola(d, t):
    print(d, t)

#i.digital(1).change(hola)
#i.digital(1).on();
i.analog(0).on(None)
#i.enable_digital_reporting(14)
time.sleep(5)

for j in range(100000):
    print(i.analog(0).read())
time.sleep(5)
i.analog(0).off()
print("Stop!")




