class Person:
    def __init__(self,fname,lname,phone):
        self.fname= fname
        self.lname= lname
        self.phone = phone
    def person_info(self):
        print("fname:",self.fname,"","lname:",self.lname,"","phone:",self.phone)
class Call:
   def call_person(self,call):
       print("call to" + self.fname + self.lname  ,"phone:" + self.phone)


class Callmix(Person,Call):
    pass

per1 = Callmix("Mate","adamia","5991234567")
per1.person_info()
per1.call_person("x")