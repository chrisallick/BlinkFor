import tweepy
import serial
import unicodedata
import time
import signal
import sys
import pymcu
import config

# I have a a file called config.py which has the 4 variables required for twitter in my git ignore
# I have a 5v buzzer from the arduino starter kit on digital pin 5 with no resistor :)
# I have an rgb led common ground on pins pwm: 1,2 and 3

class StreamListener( tweepy.StreamListener ):

    def __init__( self ):
        self.auth1 = tweepy.auth.OAuthHandler(config.consumer_key,config.consumer_secret)
        self.auth1.set_access_token(config.access_token,config.access_token_secret)
        self.api = tweepy.API(self.auth1)

        self.board = serial.Serial("/dev/tty.usbmodem1411", 9600)

    def on_status( self, status ):
        val = unicodedata.normalize('NFD', status.text).encode('ascii','ignore')
        print val

        self.board.write(str("w"))

    def exiting( self ):
        self.board.close()

l = StreamListener()

def signal_handler(signal, frame):
        l.exiting()
        print 'Exiting...'
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if len(sys.argv) > 1:
    term = sys.argv[1]
else:
    term = "tacos"

streamer = tweepy.Stream( auth=l.auth1, listener=l, timeout=3000000000 )
streamer.filter( follow=None, track=[term], async=False )