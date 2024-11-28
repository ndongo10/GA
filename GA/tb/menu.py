from authenticator import Authenticator
from authorisator import Authorizor

class Menu:
    def __init__(self):
        self.authenticator = authenticator()
        self.authorisator = Authorisator()
        
        self.choix = {
            "1": self.add_user,
            # "2": self.logout_user,
            # "3": self.add_permission,
         "4": self.quitter,
        }

    def afficher_menu(self):
        print("""
        1. add un user
        2. logout un user
        3.add permission
        4. quitter le programme
        
              """)
    
    def add_user(self):
        '''
        Cette methode permet d'ajouter un user
        '''
        user_name = input("Entrez le nom de l'utilisateur:")
        password = input("entrez le password: ")
        self.authenticator.add_user(user_name, password)
        print("user add avec succes!")

    def quitter(self):
        print("Merci d'avoir utilisé le programme")
        exit(0);

    def run(self):
        while True:
            self.afficher_menu()
            choix_option = input("Entre un choix:")
            action = self.choix.get(choix_option)
            if action:
                action()
            else:
                print("Choix invalide!")