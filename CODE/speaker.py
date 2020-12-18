"""
--------------------------------------------------------------------------
Speaker Sound Functionality
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
Python threading class designed to provide speaker functionality. Designed to work
with any speaker that operates using PWM.

"""
import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.PWM as PWM
import time
import threading
        
class PlayNote(threading.Thread):
    speaker = None
    freq_to_note = {'C' : 261, 'D' : 294, 'E' : 330, 'F' : 249, 'G' : 392, 'A' : 440, 'B': 494}
    stop = False
    notes = []
    
    def __init__(self, speaker):
        """
        Initialize thread and speaker pin
        """
        threading.Thread.__init__(self)
        self.speaker = speaker

    def run(self):
        """
        Keep speaker on continuous loop, waiting for a new note to play
        """
        while not self.stop:
            if self.notes:
                note = self.notes.pop(0)
                PWM.start(self.speaker, 5, self.freq_to_note[note])
                time.sleep(0.5)
            else:
                PWM.stop(self.speaker)
    
    def add_note(self, note):
        """
        Adds a note to speaker's note buffer, which will be played as soon as possible
        """
        self.notes.append(note)
    
    def end(self):
        """
        Stop the thread
        """
        self.stop = True