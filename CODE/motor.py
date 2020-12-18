"""
--------------------------------------------------------------------------
Continuous Servo Motor Functionality
--------------------------------------------------------------------------
License:   
Copyright 2020 Michael Tang

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------
Python file that contains class to operate motor servo. Intended to work using
any continuous rotation servo.
"""

import Adafruit_BBIO.PWM as PWM
import threading

class RunMotor(threading.Thread):
    motor = None
    stop = False
    halt = True
    
    def __init__(self, motor):
        """
        Initializes thread and pin connected to continuous servo motor
        """
        threading.Thread.__init__(self)
        self.motor = motor
    
    def run(self):
        """
        Servo runs by continuuously waiting for a stop signal
        """
        # wait for stop to be signalled
        while True:
            # if halt command is given, pause the motor's operation
            if self.halt:
                PWM.stop(self.motor)
            # if stop command is given, terminate the motor's operation
            if self.stop:
                PWM.stop(self.motor)
                break
                
    def pause(self):
        """
        Pause the motor
        """
        self.halt = True
        
    def unpause(self):
        """
        Unpause the motor
        """
        self.halt = False
        # start motor
        PWM.start(self.motor, 25, 400)
                
    def end(self):
        """
        Stop the thread
        """
        self.stop = True
        