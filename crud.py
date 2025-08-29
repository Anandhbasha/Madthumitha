from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/')

db = client['studentList']

table = db['stdInfo']

print("db is connected")

for stu in table.find():
    print(stu)

# newStud = {"name":"arjun","rollNo":"111AI002","city":"Salem"}
# table.insert_one(newStud)

# table.update_one({"name":"arjun"},{"$set":{"city":"Kerala"}})
# print("Updated Succesfully")

table.delete_one({"name":"arjun"})
print("Deleted Succesfully")