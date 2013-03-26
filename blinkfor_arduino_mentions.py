from rauth.service import OAuth1Service

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import pymcu

import serial
import unicodedata
import time
import signal
import sys
import json

# I have a a file called config.py which has the 4 variables required for twitter in my git ignore
# I have a 5v buzzer from the arduino starter kit on digital pin 5 with no resistor :)
# I have an rgb led common ground on pins pwm: 1,2 and 3

class StdOutListener( StreamListener ):

    def __init__( self ):
        self.board = serial.Serial("/dev/tty.usbmodem1411", 9600)

    def on_data( self, data ):
        dataObj = json.loads( data )

        if "entities" in dataObj:
            #print "yes entities"
            if "user_mentions" in dataObj["entities"]:
                #print "yes user_mentions"
                #print data["entities"]["user_mentions"]
                for mention in dataObj["entities"]["user_mentions"]:
                    #print "yes mention"
                    if mention["screen_name"] == username:
                        #print "yes!!!"
                        self.board.write(str("w"))
        return True

    def on_error(self, status):
        print status

    def exiting( self ):
        self.board.close()

def signal_handler(signal, frame):
        l.exiting()
        print 'Exiting...'
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = "chrisallick"


twitter = OAuth1Service(
    name='twitter',
    consumer_key="J8MoJG4bQ9gcmGh8H7XhMg",
    consumer_secret="7WAscbSy65GmiVOvMU5EBYn5z80fhQkcFWSLMJJu4",
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize',
    base_url='https://api.twitter.com/1/')

request_token, request_token_secret = twitter.get_request_token()

authorize_url = twitter.get_authorize_url(request_token)

print 'Visit this URL in your browser: ' + authorize_url
pin = raw_input('Enter PIN from browser: ')

session = twitter.get_auth_session(request_token,
                                   request_token_secret,
                                   method='POST',
                                   data={'oauth_verifier': pin})

l = StdOutListener()
auth = OAuthHandler("J8MoJG4bQ9gcmGh8H7XhMg","7WAscbSy65GmiVOvMU5EBYn5z80fhQkcFWSLMJJu4")
auth.set_access_token(session.access_token,session.access_token_secret)

stream = Stream(auth, l)
stream.userstream()