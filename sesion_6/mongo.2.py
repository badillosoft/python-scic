from pymongo import MongoClient

client = MongoClient()

db = client.cic

cursor = db.alumnos.find({}, {"_id": 0})

for alumno in cursor:
    print(alumno)

client.close()