import socket
import time

CARBON_SERVER = '172.24.1.103'
CARBON_PORT = 2003

class gsend(object):
	def __init__(self):
		self.sock = socket.socket()
		self.sock.connect((CARBON_SERVER, CARBON_PORT))
		
	def close(self):
		self.sock.close()

	def send_message(self,message):
		self.sock.sendall(message)

	def send(self,metric_path,value):
		timestamp = int(time.time())
		message = '%s %s %d\n' % (metric_path, value, timestamp)
		self.send_message(message)

g = gsend()		
def send_to_graphite(group,dic):	
	metric_path_prefix = "heartbeat."+ group + "."
	for key in dic:
		g.send(metric_path_prefix+str(key),dic[key])