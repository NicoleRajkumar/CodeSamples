from api.serializer import Serializer
from api.record import Record
import json
from json.decoder import JSONDecodeError

class JSONSerializer(Serializer):

    def __init__(self, records):
        self.records = records

    def serialize(self, filepath, pdrecords):
        self.records = pdrecords
        records = []
        for x in self.records:
            records.append(vars(x))

        f = open(filepath, 'w')
        json.dump(records, f, indent = 4)
        f.close()
        
    
    def deserialize(self, filepath, pdrecords):
        self.records = pdrecords
        records = None
        
        with open(filepath, "a+") as f:
            try:
                records = json.load(f)
            except JSONDecodeError:
                return 

        if not records:
            return []

        for x in records:
            record = Record(name=x["name"], address=x["address"], phoneNumber=x["phoneNumber"])
            self.records.append(record)

        return self.records

    def display(self, pdrecords):
        self.records = pdrecords
        for x in self.records:
            print(json.dumps(vars(x), indent=4))
