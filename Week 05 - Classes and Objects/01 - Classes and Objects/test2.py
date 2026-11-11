class hobby:

    def __init__(self, name, type, duration):
        self.name = name
        self.type = type
        self.duration = duration

    def getfavouritehobby(self):
        print (self.name, self.type, self.duration)


hobby1 = hobby("Reading", "Indoor", "2 hours")
hobby2 = hobby("Football", "Outdoor", "1 hour")

hobby1.getfavouritehobby()
print(hobby1.name)

hobby2.getfavouritehobby()
print(hobby2.name)
