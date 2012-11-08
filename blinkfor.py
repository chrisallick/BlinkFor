import tweepy
import unicodedata
import time
import signal
import sys
import pymcu

class StreamListener( tweepy.StreamListener ):

    def __init__( self ):
        self.auth1 = tweepy.auth.OAuthHandler('Consumer key','Consumer secret')
        self.auth1.set_access_token('Access token','Access token secret')
        self.api = tweepy.API(self.auth1)

        self.board = pymcu.mcuModule()

    def on_status( self, status ):
        val = unicodedata.normalize('NFD', status.text).encode('ascii','ignore')
        print val

        self.board.pinHigh( 1 )
        time.sleep(0.5)
        self.board.pinLow(1)
        time.sleep(0.5)

def signal_handler(signal, frame):
        print 'Exiting...'
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

if len(sys.argv) > 1:
    term = sys.argv[1]
else:
    term = tacos

l = StreamListener()
streamer = tweepy.Stream( auth=l.auth1, listener=l, timeout=3000000000 )
streamer.filter( follow=None, track=[term], async=False )