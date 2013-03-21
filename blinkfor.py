import tweepy
import unicodedata
import time
import signal
import sys
import pymcu
import config

class StreamListener( tweepy.StreamListener ):

    def __init__( self ):
        self.auth1 = tweepy.auth.OAuthHandler(config.consumer_key,config.consumer_secret)
        self.auth1.set_access_token(config.access_token,config.access_token_secret)
        self.api = tweepy.API(self.auth1)

        self.board = pymcu.mcuModule()
        self.board.pwmOff(1)

    def on_status( self, status ):
        val = unicodedata.normalize('NFD', status.text).encode('ascii','ignore')
        print val

        self.board.pwmOn(1)

        for i in range(0, 255):
            self.board.pwmDuty( 1, i )
        for i in range(0, 255):
            self.board.pwmDuty( 1, 255-i )

def signal_handler(signal, frame):
        print 'Exiting...'
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

if len(sys.argv) > 1:
    term = sys.argv[1]
else:
    term = "tacos"

l = StreamListener()
streamer = tweepy.Stream( auth=l.auth1, listener=l, timeout=3000000000 )
streamer.filter( follow=None, track=[term], async=False )