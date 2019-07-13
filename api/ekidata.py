import urllib
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

url = "http://www.ekidata.jp/api/s/1130224.xml"

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
	xml_string = response.read()

root = ET.fromstring(xml_string.decode())
root = ET.fromstring(xml_string)

for i in root.findall('./station/*'):
	print (i.text)

