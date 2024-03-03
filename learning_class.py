

# class Person:
#     def __init__(self, name, age, gender, hobby):
#         self.name = name 
#         self.age = age 
#         self.gender = gender 
#         self.hobby = hobby 
    

#     def showDetails(self):
#         print({
#             "name": self.name,
#             "age": self.age,
#             "gender": self.gender,
#             "hobby": self.hobby
#         })

# aalina = Person("Aalina", 10, "female", "eating")
# aaron = Person("Aaron", 9, "male", "singing") 

# aalina.showDetails()
# aaron.showDetails()

class Phone:

    total_number_of_phones = 0

    def __init__(self, name, memory):
        self.name = name
        self.battery = 0
        self.memory = memory
        self.status = "off"
        self.is_calling = False

        Phone.total_number_of_phones += 1
    
    def charge(self, percentage):
        if self.battery + percentage > 100:
            self.battery = 100
        else:
            self.battery += percentage


    def on(self):
        if self.status == "on":
            print("Phone is already one")
        else:
            if self.battery == 0:
                print("Phone battery is low, you can not on it")
            else:
                self.status = "on"
        

    def off(self):
        if self.status == "off":
            print("The phone already off")
        else:
            self.status = "off"

    def call(self, phone_number):
        self.is_calling = True
        print("Calling ", phone_number, "📞")

    def cut_call(self):
        if self.is_calling:
            self.is_calling = False
            print("Call cut")
        else:
            print("You are not making a call")

    def show_phone_details(self):
        print({
            "name": self.name,
            "memory": self.memory,
            "battery": self.battery,
            "status": self.status
        })


iphone5 = Phone("Iphone 5", 64)
iphone6 = Phone("Iphone 6", 256)

iphone5.charge(80)
iphone5.charge(50)
iphone5.on()
iphone5.on()