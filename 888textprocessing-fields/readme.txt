
txp-fl.py

purpose:
    takes sqlacodegen output file and puts field names beside each other.

generate models from db...
    c:\p2\python27\scripts\sqlacodegen sqlite:///Chinook_Sqlite_AutoIncrementPKs.sqlite > modelsgen.txt

txp-fl.py
    this reads modelsgen.txt and creates modelsgen-fieldlist.txt

2016-04-02
David Gleba
    