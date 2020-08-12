import requests
import time
import json


HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

meta = {'nameProject': 'push_swap',
	'nameUser': 'slynell'}

cookies = {'_intra_42_session_production': 'bd7e003ef9e5c8e9d0adbe7d908fd1e0',
	'user.id': 'NTY5MDY%3D--e7512a617c68252e33a66385be4cfe6450247b61', '-ga': 'GA1.2.828180123.1597243532'}
user_agent = {'User-agent': 'Mozilla/5.0',
	'Accept': 'application/json,text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

while(time.localtime().tm_hour < 20):
    # r = requests.get('https://projects.intra.42.fr/projects/{nameProject}/slots.json?team_id=3238905&start=2020-08-10&end=2020-08-17'.format(**meta), cookies=cookies, headers = user_agent)
    # result = json.loads(r.text)
    # if len(result) == 0:
	thisTime = time.strftime("%I:%M:%S %p", time.localtime())
	if time.localtime().tm_sec % 2 == 0:
		print thisTime + FAIL + '\tNULL Slot ' + ENDC
	else:
		print thisTime + OKGREEN + '\tFind new Slot ' + ENDC + '= https://projects.intra.42.fr/{nameProject}/{nameUser}'.format(**meta)
	time.sleep(5)
