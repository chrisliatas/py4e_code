# using the examples from: https://dev.socrata.com/docs/paging.html#2.1
# and: https://dev.socrata.com/foundry/data.consumerfinance.gov/jhzv-w97w

import ssl
import urllib.request
import json


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

limit = None
offset = None

baseurl = 'https://data.consumerfinance.gov/resource/jhzv-w97w.json'

try:
    limit = abs(int(input('Enter integer limit: ')))
    offset = abs(int(input('Enter integer offset: ')))
except:
    limit = None
    offset = None

# Create the url to request
if limit is None and offset is None:
    url = baseurl
elif limit > 0 or offset > 0:
    url = baseurl + '$limit=' + str(limit) + '&' + '$offset=' + str(offset)
elif limit > 0 and offset == 0:
    url = baseurl + '$limit=' + str(limit) + '&' + '$offset=0'
elif limit == 0 and offset > 0:
    url = baseurl + '$limit=0' + '&' + '$offset=' + str(offset)
else:
    url = baseurl

print('Retrieving:', url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    print(data)

print(json.dumps(js, indent=2))
