import machine
import utime

led=machine.Pin(2, machine.Pin.OUT)
led.on()
utime.sleep(1)
led.off()

class Wheel:
    # Control one  wheel.
    def __init__(self, pin=4, zerovalue=77, speedscale=1):
        # zerovalue = PWM value to make the wheel stop
        # speedscale is change in PWM value (vs zerovalue) per meter/second
        # the left and right wheels will have speedscales of opposite sign
        self.pin = machine.Pin(pin)
        self.zerovalue = zerovalue
        self.speedscale = speedscale
        self.pwm = machine.PWM(self.pin, freq=50)
        self.pwm.duty(zerovalue)

    def setspeed(self, speed):
        pwmvalue = self.zerovalue + speed * self.speedscale
        self.pwm.duty(pwmvalue)

    def stop(self):
        self.pwm.duty(0)
        #self.setspeed(0)


class Mover:
    def __init__(self, leftpin=5, rightpin=4,
                 leftspeedscale=1, rightspeedscale=-1,
                 leftzero=77, rightzero=77):
        self.wright = Wheel(pin=rightpin, zerovalue=rightzero, speedscale=rightspeedscale)
        self.wleft = Wheel(pin=leftpin, zerovalue=leftzero, speedscale=leftspeedscale)

    def go(self, speed=1, turn=0, duration=None, distance=None):
        """
        
        :param speed: 
        :param turn: Right is positive
        :param duration: in seconds. If none, return immediately
        :param distance: 
        :return: 
        """
        self.wleft.setspeed(speed + turn)
        self.wright.setspeed(speed - turn)
        if duration is not None:
            utime.sleep(duration)
            self.stop()

    def stop(self):
        self.wleft.stop()
        self.wright.stop()
        #self.go(speed=0)

class PIR:
    def __init__(self, pin=18):
        self.pin = machine.Pin(pin, machine.Pin.IN)

    def value(self):
        return self.pin.value()

def testmover(speed=1):
    mover = Mover()
    mover.go(speed=speed, duration=5)
    mover.go(speed=speed,turn=1, duration=5)
    mover.go(speed=-speed, duration=5)
    mover.go(speed=speed,turn=1, duration=5)
    mover.stop()


def test1():
    wright = Wheel(pin=4, speedscale=1)
    wleft = Wheel(pin=5, speedscale=-1)
    wleft.setspeed(1)
    wright.setspeed(1)
    utime.sleep(5)
    wleft.stop()
    wright.stop()


def testpir(duration=10):
    global led
    timestep = 0.1
    nsteps = duration / timestep
    pir = PIR()
    for i in range(nsteps):
        led.value(pir.value())
        utime.sleep(timestep)

def killallhumans(duration=100):
    global led
    mover = Mover()
    timestep = 0.1
    nsteps = duration / timestep
    pir = PIR()
    for i in range(nsteps):
        if pir.value():
            print("person detected")
            mover.go(speed=10)
            led.on()
        else:
            led.off()
            print("searching")
            mover.go(speed=0,turn=1, duration=0.1)
            mover.stop()
        utime.sleep(timestep)
    mover.stop()
    led.off()



# class Mover:
# Control both wheels to make the robot move
# def __init__(self, leftwheel, rightwheel):
# def move(self, speed, turnrate=None, duration=None):
# speed in meters per second
# turnrate in degrees per second (use different wheel speeds to turn)
# duration: if a value, finish this move after this many seconds
# def turn(self, angle):
# def stop():
# def _endmove():
