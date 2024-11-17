from api.serializer import Serializer
from api.record import Record
import xml.etree.ElementTree as ET

class XMLSerializer(Serializer):

    def __init__(self, records):
        self.records = records

    def serialize(self, filepath, pdrecords):
        self.records = pdrecords
        elem = ET.Element("records")
        for x in self.records:
            child = ET.Element("record")
            elem.append(child)
            for y in list(x.__dict__.keys()):
                item = ET.Element(str(y))
                item.text = getattr(x, y)
                child.append(item)

        tree = ET.ElementTree(elem)
        tree.write(filepath)


    def deserialize(self, filepath, pdrecords):
        self.records = pdrecords
        elem = ET.parse(filepath).getroot()

        if not elem:
            return []

        for r in elem: # every record
           record = Record(name = r.find("name").text, address= r.find("address").text, phoneNumber= r.find("phoneNumber").text)
           self.records.append(record)

        return self.records

    def display(self, pdrecords):
        self.records = pdrecords
        for x in self.records:
            child = ET.Element("record")
            for y in list(x.__dict__.keys()):
                item = ET.Element(str(y))
                item.text = getattr(x, y)
                child.append(item)
            print(ET.tostring(child))

