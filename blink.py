import pymcu
import random
 
mb = pymcu.mcuModule()
 
mb.pwmOn(1)
mb.pwmOn(2)

for x in range( 0, 5 ):
    for i in range(0, 255):
        mb.pwmDuty( 1, i )
        mb.pwmDuty( 2, i )

    for i in range(0, 255):
        mb.pwmDuty( 1, 255-i )
        mb.pwmDuty( 2, 255-i )