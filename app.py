from pymongo import MongoClient

client = MongoClient('mongodb://<username>:<password>@<mongo_ip_address>:<mongo_port>')
db = client['learnfiles']
course_collection = db['course']

course_name = input("insert course name : ")
course_time = input("insert course time : ")
course_type = input("insert course type : ")

course_data = {

    "name" : course_name,
    "time" : course_time,
    "type" : course_type

}

course_collection.insert_one(course_data)
