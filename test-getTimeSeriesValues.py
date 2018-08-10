# This is a git test!

import sys
sys.path.insert(0, '../Config')
import userConfig
import requests
from webob.multidict import MultiDict
import json


SLV_URL = 'https://slv.poc02.ssn.ssnsgs.net:8443/reports'

deviceID = '22471'

payload = MultiDict([
  ('deviceId', '22471'),
#  ('name', 'MainVoltage'),
#  ('name', 'SwitchOnCounter'),
#  ('name', 'LampEnergy'),
  ('name', 'LuxLevel'),
  ('from', '10/07/2018 00:00:00'),
  ('to', '02/08/2018 12:00:00'),
  ('ser', 'json')
])

response = requests.post(SLV_URL + "/api/logging/getDevicesLogValues", data=payload, auth=(userConfig.USERNAME, userConfig.PASSWORD))
print(response)
data = json.loads(response.text)
print(json.dumps(data, indent=2))