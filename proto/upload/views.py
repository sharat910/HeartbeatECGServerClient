from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import csv
import json
import time
from ipware.ip import get_ip
from plt_help import send_to_graphite
# Create your views here.
@csrf_exempt
def upload(request):
	timestamp = time.time()
	ip = get_ip(request)
	beat=request.POST['HeartBeat']
	send_to_graphite(str(ip).replace(".","_"),{"Heartbeat":beat})
	with open('datanew.csv', 'a') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|')
		spamwriter.writerow([timestamp]+[ip]+[beat])
	return HttpResponse('Data uploaded')

def download(request):
	a={}
	with open('data.csv', 'r') as csvfile:
		spamwriter = csv.reader(csvfile, delimiter=',',quotechar='|')
		for row in spamwriter:
			a[row[0]]=row[1]
		a=json.dumps(a)
	return HttpResponse(a)
