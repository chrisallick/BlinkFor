BlinkFor
========

Stream Twitter with Python and blink an LED with PyMCU when a particular word is mentioned! The code I'm talking about during my http://sparkin60.com/ interview: http://vimeo.com/44761015

I've removed my credentials from the init function in the Streaming class.  Credentials can be obtained at: https://dev.twitter.com/

The application defaults to "tacos" if sys.argv[1] is not provided.

Tested on OS X 10.6 Python 2.6 and OS X 10.8 Python 2.7:

First you'll need the FTDI drivers if you want to use the pyMCU: http://www.ftdichip.com/Drivers/VCP.htm

Then (from here: http://www.pymcu.com/Installation.html#OsxInstall ):

$>sudo easy_install pyserial

$>sudo easy_install pymcu

$>python blinkfor.py tacos

Any microcontroller can be used.  Just modify the function "on_status."

I added a new file arduino/pyserial.ino

Tested with python 2.7 on OS X 10.8

It doesn't do much, just sits in a loop waiting for serial commands.
If you add this to your arduino (I used an Uno), you should be good to go.
Modify the Arduino sketch for more flexibility or a generalized platform for prototyping with Python and Arduino via a serial cable.

Thanks,
http://chrisallick.com