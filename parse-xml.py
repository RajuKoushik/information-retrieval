#parsing an xml file and outputting a txt file

import xml.etree.ElementTree as ET
tree = ET.parse('hindi-document-00001.xml')
notags = ET.tostring(tree.getroot(), encoding='utf-8',method='text')
print(notags)