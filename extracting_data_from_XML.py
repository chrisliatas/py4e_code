import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

while True:
    url = input('Enter location: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data.decode())

    counts = tree.findall('.//count')
    print('Count:', len(counts))
    print('Sum:', sum(int(counts[i].text) for i in range(len(counts))))
