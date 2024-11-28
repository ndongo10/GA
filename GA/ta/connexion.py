import sqlite3
print(sqlite3.sqlite_version)
connexion = sqlite3.connect("note.db")
print("case de donnees cree")
curseur = connexion.cursor()
# creer une table
curseur.execute('''CREATE TABLE IF NOT EXISTS NOTES( id integer primary key,balise text not null,memo text not null)''')
print('table cree avec succes')
# inser des donnees
curseur.execute('''INSERT INTO NOTES(balise,memo) VALUES('bonjours','rendez-vous prevu')''')
print('donnees inserees avec succes')
# selection des donnees
curseur.execute('SELECT * FROM NOTES')
resultats = curseur.fetchall()
print('resultat')
connexion.close()