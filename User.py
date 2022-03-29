import json


class User:
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.email = None
        self.hashedpwd = None
        self.token = None
    
    def setFirstName(self, firstname):
        self.firstname = firstname
    
    def setLastName(self, lastname):
        self.lastname = lastname
    
    def setEmail(self, email):
        self.email = email
    
    def setHashedPasswd(self, pwd):
        self.hashedpwd = pwd

    def setToken(self, token):
        self.token = token

    def display(self):
        print("Welcome " + self.firstname + " " + self.lastname + "!!")
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)