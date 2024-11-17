class Record(object):

    def __init__(self, name = None, address = None, phoneNumber = None):

        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber
    
    def __str__(self) -> str:
        return f"Name={self.name}, Address={self.address}, Phone Number={self.phoneNumber}"
    
    # getters for the attributes
    
    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address

    def getPhoneNumber(self):
        return self.phoneNumber