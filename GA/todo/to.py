import  tkinter as tk 
from tkinter import messagebox
from PIL import Image

def se_connecter():
    username = entry_username.get()
    password = entry_password.get()
    if username and password:
     messagebox.showinfo("Information" , "connexion reussi !")
    else:
        messagebox.showwarning("Avertissement" , "veuillez entrer un nom d'utilisateur et un mot de passe.")

def se_deconnecter():
    messagebox.showinfo("Information ", "vous etes deconnnecte.")
    
    image = Image.open("votre_image.jpg")
    image= image.resize((150,150))
    image.show() 


fenetre = tk.Tk()
fenetre.title("AUTHENTICATOR")

label_username= tk.Label(fenetre, text="NOM:" )
label_username.pack(pady=5)
entry_username = tk.Entry(fenetre, width=30)
entry_username.pack(pady=5)

label_password = tk.Label(fenetre, text="MOT DE PASSE:")
label_password.pack(pady=5)
entry_password = tk.Entry(fenetre, show="*",width=30)
entry_password.pack(pady=5)

btn_connexion = tk.Button(fenetre, text=" connecte", command=se_connecter , bg="blue" , fg="white" , width=15 , height=2)
btn_connexion.pack(pady=20)



btn_deconnecte = tk.Button(fenetre, text=" deconnecte", command=se_deconnecter , bg="red" , fg="white", width=15, height=2)
btn_deconnecte.pack(pady=20)

fenetre.mainloop()

             
