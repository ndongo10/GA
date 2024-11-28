import tkinter as tk
from tkinter import messagebox

# Fonction pour valider la permission
def assign_permission():
    # Récupérer les valeurs de l'interface
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    permission = entry_permission.get()
    
    if not nom or not prenom or not permission:
        messagebox.showwarning("Champs incomplets", "Veuillez remplir tous les champs!")
        return
    
    # Affichage du résultat sous forme de chaîne de caractères
    result.set(f"Utilisateur: {prenom} {nom}, Permission: {permission}")

# Fonction pour réinitialiser les champs
def reset_fields():
    entry_nom.delete(0, tk.END)
    entry_prenom.delete(0, tk.END)
    entry_permission.delete(0, tk.END)
    result.set("")

# Fonction pour quitter l'application
def quit_application():
    root.quit()

# Création de la fenêtre principale
root = tk.Tk()
root.title("AUTHORIZOR - Gestion des Permissions")
root.geometry("400x300")

# Label et champs pour le nom
label_nom = tk.Label(root, text="Nom :")
label_nom.pack(pady=5)
entry_nom = tk.Entry(root)
entry_nom.pack(pady=5)

# Label et champs pour le prénom
label_prenom = tk.Label(root, text="Prénom :")
label_prenom.pack(pady=3)
entry_prenom = tk.Entry(root)
entry_prenom.pack(pady=3)

# Label et champs pour la permission
label_permission = tk.Label(root, text="Permission :")
label_permission.pack(pady=5)
entry_permission = tk.Entry(root)
entry_permission.pack(pady=5)

# Variable pour afficher le résultat
result = tk.StringVar()

# Label pour afficher le résultat
label_result = tk.Label(root, textvariable=result, font=("Helvetica", 10, "italic"))
label_result.pack(pady=10)

# Boutons pour valider, réinitialiser et quitter
btn_valider = tk.Button(root, text="Valider", command=assign_permission ,  bg="red" , fg="white", width=15, height=2)
btn_valider.pack(pady=5)

btn_reset = tk.Button(root, text="Réinitialiser", command=reset_fields, bg="black" , fg="white", width=15, height=2)
btn_reset.pack(pady=5)

btn_quitter = tk.Button(root, text="Quitter", command=quit_application , bg="blue" , fg="white", width=15, height=2)
btn_quitter.pack(pady=5)

# Lancer la boucle principale de l'application
root.mainloop()
