import tkinter as tk
from tkinter import messagebox


def valider():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    ville = entry_ville.get()
    chaine_info = f"{nom}// {prenom} // {ville}"
    
    label_resultat.config(text=chaine_info)

def reinitialiser():
        entry_nom.delete(0, tk.END)
        entry_prenom.delete(0, tk.END)
        entry_ville.delete(0, tk.END)
        
        label_resultat.config(text="")

def quitter():       
    fenetre.destroy()  




fenetre = tk.Tk()
fenetre.title("INFORMATIONS DE L'UTILISATEUR")

tk.Label(fenetre , text="VOTRE NOM :").grid(row=0, column=0 , padx= 10, pady= 5)
entry_nom =tk.Entry(fenetre)
entry_nom.grid(row= 0, column= 1, padx= 10, pady= 5)


tk.Label(fenetre , text="VOTRE PRENOM :").grid(row=1, column=0 , padx= 10, pady= 5)
entry_prenom =tk.Entry(fenetre)
entry_prenom.grid(row= 1, column= 1, padx= 10, pady= 5)

tk.Label(fenetre , text="VOTRE VILLE :").grid(row=2, column=0 , padx= 10, pady= 5)
entry_ville =tk.Entry(fenetre)
entry_ville.grid(row= 2, column= 1, padx= 10, pady= 5)



button_valider = tk.Button(fenetre , text= "valider" ,bg= "green", fg= "white",command= valider)
button_valider.grid(row=3, column= 0  , padx= 5,pady= 10, sticky= "w")

button_reinitialiser = tk.Button(fenetre , text= "reinitialiser" ,bg="orange",fg="black" ,command= reinitialiser)
button_reinitialiser.grid(row=3, column= 1  , padx= 20,pady= 10, sticky= "w")

button_quitter = tk.Button(fenetre , text= "quitter" , command= quitter)
button_quitter.grid(row=3, column= 1  , padx= 150,pady= 10, sticky= "e")


label_resultat = tk.Label(fenetre,text="",bg="lightgray", fg="black", font=("arial", 12) , width=50,anchor="w")
label_resultat.grid(row=5 , column=0, columnspan= 3 , padx=10,pady=10, sticky="w")



fenetre.mainloop()




