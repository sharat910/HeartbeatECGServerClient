import requests
import json
import glob
import time

url = 'http://127.0.0.1:8000/upload/'
data = {}

files = sorted(glob.glob("heartbeat/*.txt"))

for file in files:
	with open(file) as f:
		hbeats = map(float,f.read().splitlines())
		for hbeat in hbeats:
			data['HeartBeat']=hbeat
 			response = requests.post(url, data)
 			print hbeat
 			time.sleep(1)
