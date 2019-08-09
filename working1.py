import machine
p4 = machine.Pin(4)
servo = machine.PWM(p4,freq=50)
servo.duty(100)
