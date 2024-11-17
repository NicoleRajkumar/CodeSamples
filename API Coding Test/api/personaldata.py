from api.record import Record
import fnmatch
import os
from api.jsonserializer import JSONSerializer
from api.xmlserializer import XMLSerializer


class PersonalData(object):

    def __init__(self, filename):
        #storing the record data here
        self.records = []
        self.filename = filename
        self.serializer = None
        self.formats = ["json", "xml"]

        # parse the filename to initalize the serializer and store the data in records
        self.serializer = self.getSerializer(self.filename)
        self.records = self.deserialize()
        
    def add(self, *args, **kwargs):
        """
        Add data with Record object or with name, address, and phoneNumber.
        """
        newRecord = None
        # if input is Record
        if len(args) == 1 and isinstance(args[0], Record):
            newRecord = args[0]
            if not self.hasRecord(newRecord):
                self.records.append(newRecord)
                
        # if input is name, address, and phone number
        elif len(kwargs) == 3:
            newRecord = Record(name=kwargs['name'], address=kwargs['address'], phoneNumber=kwargs['phoneNumber'])
            if not self.hasRecord(newRecord):
                self.records.append(newRecord)

    def hasRecord(self, record):
        """
        checks if it already exists in the data
        """
        for r in self.records:
            if r.__dict__ == record.__dict__:
                return True
        return False
        

    def filter(self, name=None, address=None, phoneNumber=None):
        """
        filters by name, address, or phone number using simple search syntax.
        Returns a list of filtered records.
        """
        filteredRecords = []
        if name:
            for record in self.records:
                if fnmatch.fnmatch(record.name, name) and record not in filteredRecords:
                    filteredRecords.append(record)
        if address:
            for record in self.records:
                if fnmatch.fnmatch(record.address, address) and record not in filteredRecords:
                    filteredRecords.append(record)
        if phoneNumber:
            for record in self.records:
                if fnmatch.fnmatch(record.phoneNumber, phoneNumber) and record not in filteredRecords:
                    filteredRecords.append(record)

        return filteredRecords


    def getSerializer(self, filename):
        """
        Gets the correct serializer based on the inputted filename.
        Returns serializer object or None.
        """
        serializer = None
        tmp = filename.split(".")[-1].lower()
        
        if tmp == "json":
            serializer = JSONSerializer(self.records)
        elif tmp == "xml":
            serializer = XMLSerializer(self.records)
        else:
            print("format not supported")
            
        return serializer
    
    def serialize(self):
        """
        Serializes the filename.
        """
        self.serializer.serialize(self.filename, self.records)
    
    def deserialize(self):
        """
        Deserializes the filename.
        """
        return self.serializer.deserialize(self.filename, self.records)
    
    def display(self):
        """
        Displays the records based on the serializer.
        """
        if self.serializer is not None:
            self.serializer.display(self.records)
        else:
            for record in self.records:
                print(record)
    
    def convert(self, filename):
        """
        Converts self.filename to another filetype based on inputted filename.
        Returns corresponding serializer or None.
        """
        tmp = filename.split(".")[-1].lower()
        if tmp in self.formats:
            new_serializer = self.getSerializer(filename)
            new_serializer.serialize(filename, self.records)
            new_serializer.display(self.records)
            return True
        else:
            print("filetype not supported.")
            return False

    def getRecords(self):
        return self.records

