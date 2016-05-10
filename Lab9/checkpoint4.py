import pymongo
import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId

try:
    conn=MongoClient()
    db = conn.csci2963
    definitions = db.definitions

    #Fetch all records
    #for d in definitions.find():
    #    print d


	#Fetch one record
	#print definitions.find_one()


    #Fetch Specific Record
    #print definitions.find_one({"word": "Capitaland"})


    #Fetch record by ID
    #print definitions.find_one({"_id": ObjectId("56fe9e22bad6b23cde07b8ce")})


    #Insert new record
    post = {"word" : "Hodor","definition" : "Hodor","Timestamp": str(datetime.datetime.now())}
    post_id = definitions.insert_one(post).inserted_id
    print definitions.find_one({"_id": ObjectId(str(post_id))})


except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e
conn