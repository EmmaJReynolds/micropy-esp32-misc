class Wheel:
   # Control one  wheel.
   import machine 
   p4 = machine.Pin(4)
   zerovalue = machine.PWM(freq=65)
   speedscale = 0
   speed = 50
   def __init__(self, p4, zerovalue, speedscale):
        # zerovalue = PWM value to make the wheel stop
        # speedscale is change in PWM value (vs zerovalue) per meter/second
        # the left and right wheels will have speedscales of opposite sign
   def setspeed(self, speed):
   def stop():



       
#class Mover:
    # Control both wheels to make the robot move
   #def __init__(self, leftwheel, rightwheel):
   #def move(self, speed, turnrate=None, duration=None):
       # speed in meters per second
       # turnrate in degrees per second (use different wheel speeds to turn)
       # duration: if a value, finish this move after this many seconds
   #def turn(self, angle):
   #def stop():
   #def _endmove():
