import pymongo
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://asmafariha:access123@cluster0.t1qqadg.mongodb.net/?retryWrites=true&w=majority")
db=cluster["jobhuntbuddy"]
collection=db["cloudapp"]

post1={"_id": 1, "name":"fariha", "email":"fariha.fa@mail"}
post2={"_id": 2, "name":"arif", "email":"arif.fa@mail"}
post3={"_id": 3, "name":"ahmad", "email":"ahmad.fa@mail"}
#collection.insert_many([post1,post2,post3])
results=collection.find({"name":"asma"})
for result in results:
    print (result["email"])

