from pymongo import MongoClient

client = MongoClient()

db = client.cic

result = db.alumnos.insert_one({
    "nombre": "Pepe",
    "cursos": ["Python Basico", "Java Intermedio", "C# Avanzado"]
})

print(result.inserted_id)

client.close()