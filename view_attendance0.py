from pymongo import MongoClient as mc
from certifi import where
from pandas import DataFrame as df

ca = where()
cl = mc("mongodb+srv://Abishek:Rajagiri123!@db.bpuc5.mongodb.net/test")

db = [cl[_] for _ in sorted(cl.list_database_names())]
coll = [db[0][_] for _ in sorted(db[0].list_collection_names())]

def view(date):
    x = coll[0].find({
        f"{date}": {"$exists": True}
    }).sort("_id")
    print("""RETID\t\t1\t2\t3\t4\t5\t6\t7
---------------------------------------------------------------------""")
    
    for _ in x:
        print(_["_id"], end = "\t")
        for __ in range(1, 8):
            P = f"P{__}"
            print(f"{'p' if int(_[date][P]) else ' '}", end = "\t")
        print()

date = input("Enter date: ")
view(date)