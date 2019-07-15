import urllib
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

url = "http://zip.cgis.biz/xml/zip.php?zn=2450018"

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
	xml_string = response.read()

root = ET.fromstring(xml_string.decode())
root = ET.fromstring(xml_string)
ekidata = []

for i in root.findall('./*'):
	for h in i.attrib:
		ekidata.append(h)

#ekidata_csv = ",".join(map(str,ekidata))
print(ekidata)
