import requests
import os
from time import sleep 


frame = 0
while True:
	print('sending img'+str(frame)+'.jpg...')
	requests.post('http://192.168.1.17/success', files = {'file' : open('img'+str(frame)+'.jpg', 'rb')})
	frame = (frame+1)%3
	sleep(.06)