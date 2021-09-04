import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    if len(url) < 1: break
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    print('Retrieved', len(data), 'characters')
    js = json.loads(data)
    #print(json.dumps(js, indent=2))
    print('Count:', len(js['comments']))
    print('Sum:', sum(int(item['count']) for item in js['comments']))
