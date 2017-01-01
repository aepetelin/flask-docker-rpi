#!/usr/bin/env python
#
#
#
import time

class UnknownRevision(Exception):
    pass

class Toolbox:
    '''Set of utilities to exercise the power of the Raspberry Pi'''
    def __init__(self):
        pass
    
    def get_revision(self):
        'Return Model and Revision of the current board'
        with open('/proc/cpuinfo', 'r') as f:
            for line in f:
                if 'Revision' in line:
                    rev = line.split(':')[1].strip()
                    #print rev
                    # Data from: http://raspberryalphaomega.org.uk/?p=428
                    if rev == '0002':
                        return ('Model B', 'Revision 1.0', '256MB')
                    elif rev == '0003':
                        return ('Model B', 'Revision 1.0+', '256MB')
                    elif rev == '0004' or rev == '0005' or rev == '0006':
                        return ('Model B', 'Revision 2.0', '256MB')
                    elif rev == '0007' or rev == '0008' or rev == '0009':
                        return ('Model A', 'Revision 1.0', '256MB')
                    elif rev == '000d' or rev == '000e' or rev == '000f':
                        return ('Model B', 'Revision 2.0' '512MB')
                    else:
                        raise UnknownRevision('Revision is: ' + rev)
                
 
    def gpio_setup_output(self, pin, output):
        with open("/sys/class/gpio/export", 'w') as f:
            f.write(str(pin))
        with open("/sys/class/gpio/gpio%d/direction" % pin, 'w') as f:
            f.write(output)
    
    def gpio_set_output(self, pin, val):
        with open("/sys/class/gpio/gpio%d/value" % pin, 'w') as f:
            f.write(str(val))    

    def gpio_cleanup(self, pin):
        with open("/sys/class/gpio/unexport", 'w') as f:
                f.write(str(pin))
    

if __name__ == '__main__':
    t = Toolbox()
    print ', '.join(t.get_revision())
    
    # LED Blink
    try:
        for i in range(0, 100):
            # Uses BCM numbering
            t.gpio_setup_output(11, "out")
            t.gpio_set_output(11, 1)
            time.sleep(.5)
            t.gpio_set_output(11, 0)
            time.sleep(.5)
    finally:
        t.gpio_cleanup(11)