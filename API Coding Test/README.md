
# Overview

This is an API created for the coding test provided by Animal Logic.
This is a simple service where records can be stored, modified, and displayed.
This APi supports JSON and XML serialisation, but can be expanded to support other formats.

# Setup

To install as a package, change the working directory to `codingtest` and run
`python setup.py install --user`

# How to Use

## Creating Personal Data Object

Create a personal data object using PersonalData class from personaldata.py.
It requires a filename for input, which will determine the serializer to use.
If the file doesn't exist, it will be created.
If the inputted file is not a supported format, a message will print to notify the user.

    pd = personalData(filename="test.json")


## Adding Records

Adding records to the personal data object can be done manually or by creating a record and passing that.
When done manually, the name, address, and phone number must be given.

    pd.add(name="Nicole", address="123 hello street", phoneNumber = "1234567890")

To add a record with a record object, it must be created first.
It can be created with the Record class from record.py. 
It requires the name, address, and phone number for input.

    person = Record(name="Nicole", address="123 hello street", phoneNumber = "1234567890")
    pd.add(person)


## Filtering

Filtering is done using `fnmatch.fnmatch`, which supports Unix shell-stlye wildcards.
It can be done by providing the name, address, and/or phoneNumber arguments.
Some examples are provided below:

    pd.filter(name = "N*")
    pd.filter(name = "N*", address = "*hello*")


## Converting Data

Converting data can be done with the supported formats only using the `convert` method.
Convert takes a new filename as an input, which determines the format to convert to and outputs to that path.

    pd.convert("test.xml")


## Displaying the Data

Displaying the stored data is done using the `display` method, which is determined by the file type/ serializer.
When called, it will display in one of the supported formats (currently JSON or XML).

    pd.display()


## Command Line Interface Usage

All commands are stored in the `bin` folder. To execute them, please navigate to that directory in the terminal.
It can then be used like in this example:
    >>python pd_add -h


## Extending the API

This was written with a factory design pattern. `serializer.py` is an abstract class which provides the blueprint for other 
serializer formats.
The formats can be queried, as they serializer classes are in the api folder with a standard name: `{filetype}serializer.py`