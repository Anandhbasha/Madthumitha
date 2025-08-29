import mongoengine as me

me.connect("studentList")

class Student(me.Document):
    name = me.StringField(required=True)
    rollNo = me.StringField(required=True)
    city = me.StringField(required=True)
    stdContactNumber = me.IntField(required=True)

addStu = Student(name="rahul",rollNo="111AI061",city="Trichy",stdContactNumber=989245718)
addStu.save()

for s in Student.objects:
    print(s.name,s.rollNo)