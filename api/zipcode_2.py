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
zipcode_head = []
zipcode = []

for i in root.findall('./ADDRESS_value/*'):
	for h in i.attrib:
		zipcode_head.append(h)
		zipcode.append(i.attrib[h])

zipcode_head_csv = ",".join(map(str,zipcode_head))
zipcode_csv = ",".join(map(str,zipcode))

print(zipcode_head_csv)
print(zipcode_csv)
