class Authexception(Exception):
    def __init__(self,user_name,user):
        super().__init__(self,username,user)
        self.username = username
        self.user = user
class User_nameAireadyexists(Authexception):
    pass 
class PasswordTooshort(Authexception):
    pass
class InvalidUsername(Authexception):
    pass 
class InvalidPassword(Authexception):
    pass
class NoPermission(Authexception): 
    pass               

