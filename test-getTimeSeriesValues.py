<<<<<<< HEAD
# This is a git test!

=======
#pylint: disable=all
>>>>>>> d422320180677ecb4679acd4a1f79ae496b4bd0a
import sys
sys.path.insert(0, '../Config')
import userConfig
import requests
from webob.multidict import MultiDict
import json


SLV_URL = 'https://slv.poc02.ssn.ssnsgs.net:8443/reports'

#deviceID = '22471'

payload = MultiDict([
  ('deviceId', deviceID),
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