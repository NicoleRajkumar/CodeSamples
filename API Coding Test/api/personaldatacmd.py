#!/usr/bin/python

import argparse
from api.personaldata import PersonalData

def add():
    parser = argparse.ArgumentParser(
        description="Add records by data"
    )
    parser.add_argument("file", help="personal data file to ingest")
    parser.add_argument("-n", "--name", help="name")
    parser.add_argument("-a", "--address", help="address")
    parser.add_argument("-p", "--phone", help="phone number ")

    args = parser.parse_args()
    records = PersonalData(args.file)
    records.add(name=args.name, address=args.address, phoneNumber=args.phone)
    print("record added to personal data.")

def addByRecord():
    parser = argparse.ArgumentParser(
        description="Add records by record"
    )
    parser.add_argument("file", help="personal data file to ingest")
    parser.add_argument("-r", "--record", help="Add by record") 
    
    args = parser.parse_args()
    records = PersonalData(args.file)
    records.add(args.record)
    print("record added to personal data.")

def display():
    parser = argparse.ArgumentParser(
        description="Display records"
    )
    parser.add_argument("file", help="personal data file to ingest")

    args = parser.parse_args()
    records = PersonalData(args.file)
    records.display()

def convert():
    parser = argparse.ArgumentParser(
        description="Convert records"
    )
    parser.add_argument("fromfile", help="File to convert")
    parser.add_argument("tofile", help="Converted file")
    
    args = parser.parse_args()
    records = PersonalData(args.fromfile)
    result = records.convert(args.tofile)
    if not result:
        print("Could not convert.")

def filter():
    parser = argparse.ArgumentParser(
        description="Filter records"
    )
    parser.add_argument("file", help="personal data file to ingest")
    #optional args
    parser.add_argument("-n", "--name", help="name filter")
    parser.add_argument("-a", "--address", help="address filter")
    parser.add_argument("-p", "--phone", help="phone number filter")
    
    args = parser.parse_args()
    records = PersonalData(args.file)
    filtered_results = records.filter(name=args.name, address=args.address, phoneNumber=args.phone)
    
    if len(filtered_results) != 0:
        for result in filtered_results:
            print(result)
    else:
        print("No matches found.")

