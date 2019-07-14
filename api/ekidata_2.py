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
ekidata = []
for i in root.findall('./station/*'):
	ekidata.append(i.text)

ekidata_csv = ",".join(map(str,ekidata))
print(ekidata_csv)
