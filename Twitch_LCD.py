#!/usr/bin/python
#--------------------------------------
#
#     _ ___          ________              __   ___          __   
#    (_) _ \___  ___/ /_  __/__  __ ______/ /  / _ \__ _____/ /__ 
#   / / ___/ _ \/ _  / / / / _ \/ // / __/ _ \/ // / // / _  / -_)
#  /_/_/   \___/\_,_/ /_/  \___/\_,_/\__/_//_/____/\_,_/\_,_/\__/ 
#                                                                                                                                 
#
#  Twitch_LCD.py
#  Twitch API LCD Script
#
# Author : iPodTouchDude
# Date   : 12/11/2016
#
#
# Copyright 2016 iPodTouchDude
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#--------------------------------------

import urllib, json
from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime

lcd = Adafruit_CharLCD(rs=21, en=20, d4=19, d5=13, d6=6, d7=5, cols=16, lines=2)

lcd.clear()
twitchUser = raw_input("What twitch channel would you like to monitor? ")
client_id = ''

def run_cmd(twitchUser):
        url = "https://api.twitch.tv/kraken/streams/"+twitchUser+"?client_id="+client_id
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        try:
        	return data
        except TypeError:
        	return 'Offline'
        	
def request_name(twitchUser):
        url = "https://api.twitch.tv/kraken/channels/"+twitchUser+"?client_id="+client_id
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        if 'error' in data:
        	return twitchUser
        else:
			return data['display_name']
        	
name = request_name(twitchUser)

def main():
	while 1:
	
			lcd.home()
			viewers = run_cmd(twitchUser)
		
			if 'stream' in viewers and viewers['stream'] is None or 'error' in viewers:
				lcd.clear()
				lcd.message('%s is\n' % (name))
				lcd.message('Offline')
			else:
				lcd.clear()
				lcd.message('%s\n' % (viewers['stream']['channel']['status'][:16]))
				lcd.message('%s' % (viewers['stream']['channel']['game']))
			sleep(5)

			if 'stream' in viewers and viewers['stream'] is None or 'error' in viewers:
				lcd.clear()
				lcd.message('%s is\n' % (name))
				lcd.message('Offline')
			else:
				lcd.clear()
				count = len(str(viewers['stream']['viewers']))
				lcd.message('%s\n' % (name))
				if count == 5:
					lcd.message('Viewers:   %s' % (viewers['stream']['viewers']))
				elif count == 4:
					lcd.message('Viewers:    %s' % (viewers['stream']['viewers']))
				elif count == 3:
					lcd.message('Viewers:     %s' % (viewers['stream']['viewers']))
				elif count == 2:
					lcd.message('Viewers:      %s' % (viewers['stream']['viewers']))
				else:
					lcd.message('Viewers:       %s' % (viewers['stream']['viewers']))

			sleep(15)

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd.clear()
    lcd.message('Created by\niPodTouchDude')
    sleep(2)
    lcd.clear()