import unittest
import os
import io
import sys
import re
from api.personaldata import PersonalData
from api.record import Record

class PersonalDataTest(unittest.TestCase):

    def testOne(self):
        records = PersonalData(self.fileHelper("testOne.json"))
        self.assertEqual(records.records, [])

    def testTwo(self):
        record1 = Record(name="Spongebob", address="Pineapple under the sea", phoneNumber="9999999999")
        records = PersonalData(self.fileHelper("testTwo.json"))
        records.add(record1)
        self.assertTrue(records.hasRecord(record1))
        record2 = Record(name = "Pusheen", address="123 Hello street", phoneNumber="0000000000")
        self.assertFalse(records.hasRecord(record2))
        self.assertEqual(records.serialize(), None)
    
    def testThree(self):
        records = PersonalData(self.fileHelper("testThree.json"))
        self.assertTrue(records.convert(self.fileHelper("testThree.xml")))
        self.assertFalse(records.convert(self.fileHelper("testThree.csv")))
    
    def testFour(self):
        records = PersonalData(self.fileHelper("testFour.json"))
        record = Record(name = "Nicole", address="123 Hello street", phoneNumber="1234567890")
        self.assertEqual(records.display(), None)
        records.add(record)
        
        #redirect print statement to compare with string
        f = io.StringIO()
        sys.stdout = f
        records.display()
        sys.stdout = sys.__stdout__
        output = re.sub('\s+', ' ', f.getvalue().strip())
        self.assertEqual(output.strip(), '{ "name": "Nicole", "address": "123 Hello street", "phoneNumber": "1234567890" }')

    def testFive(self):
        records = PersonalData(self.fileHelper("testFive.json"))
        record = Record(name = "Nicole", address="123 Hello street", phoneNumber="1234567890")
        records.add(record)
        records.add(name = "Santa Claus", address = "North Pole", phoneNumber = "4646464646")
        self.assertEqual(records.filter(), [])
        self.assertEqual(len(records.filter(name = "N*")), 1)

    def fileHelper(self, testfile):
        temp = os.path.abspath(os.path.join(__file__, "..", testfile))
        return temp

    def tearDown(self) -> None:
        if os.path.exists(self.fileHelper("testOne.json")):
            os.remove(self.fileHelper("testOne.json"))
        if os.path.exists(self.fileHelper("testTwo.json")):    
            os.remove(self.fileHelper("testTwo.json"))
        if os.path.exists(self.fileHelper("testThree.json")):    
            os.remove(self.fileHelper("testThree.json"))
        if os.path.exists(self.fileHelper("testThree.xml")):    
            os.remove(self.fileHelper("testThree.xml"))
        if os.path.exists(self.fileHelper("testFour.json")):    
            os.remove(self.fileHelper("testFour.json"))
        if os.path.exists(self.fileHelper("testFive.json")):    
            os.remove(self.fileHelper("testFive.json"))

if __name__ == "__main__":
    unittest.main()
    