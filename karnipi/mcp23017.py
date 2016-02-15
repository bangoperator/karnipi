#! /usr/bin/env python
# A simple Python command line tool to control an MCP23017 I2C IO Expander
# By Nathan Chantrell http://nathan.chantrell.net
# GNU GPL V3

import sys

sys.path.insert(1, '/usr/lib/python2.7/dist-packages/')
import smbus

import getopt

class MCP23017():
    
    def prepare(self):
        b = smbus.SMBus(0) # 0 indicates /dev/i2c-0
        b.read_byte_data(0x2f,0x58)


    
    # Let them know how it works
    def usage(self):
        print('Usage: mcp23017.py -b <bank> -o <output> -s <high|low>')
        # Handle the command line arguments
    
    def switch(self, value):
        
        self.prepare()
        
        try:
            opts, args = getopt.getopt(sys.argv[1:],"hb:o:s:",["bank=","output=","state="])
            
            if not opts:
                self.usage()
                sys.exit(2)
        
        except getopt.GetoptError:
            self.usage()
            sys.exit(2)
            
        for opt, arg in opts:
            if opt == '-h':
                self.usage()
                sys.exit()
            elif opt in ("-b", "--bank"):
                bank = arg
            elif opt in ("-o", "--output"):
                output = int(arg)
            elif opt in ("-s", "--state"):
                state = arg
                
        # Set the correct register for the banks
        if bank == "a" :
            register = 0x14
        elif bank == "b" :
            register = 0x15
        else:
            print "Error! Bank must be a or b"
            sys.exit()
    
            # Read current values from the IO Expander
            value = self.bus.read_byte_data(self.address,register)
    
            # Shift the bits for the register value, checking if they are already set first
            if state == "high":
                if (value >> output) & 1 :
                    print "Output GP"+bank.upper()+str(output), "is already high."
                    sys.exit()
                else:
                    value += (1 << output)
            elif state == "low":
                if (value >> output) & 1 :
                    value -= (1 << output)
                else:
                    print "Output GP"+bank.upper()+str(output), "is already low."
                    sys.exit()
            elif state == "read":
                if (value >> output) & 1 :
                    print "high"
                else:
                    print "low"
                
                sys.exit()
            else:
                print "Error! state must be high or low"
                sys.exit()
                
        # Now write to the IO expander
        self.bus.write_byte_data(self.address,register,value)
        # Tell them what we did
        print "Output GP"+bank.upper()+str(output), "changed to", state
        