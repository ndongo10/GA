from datetime import datetime

class Note:
     note_id = 0

     def __init__(self,memo,balise):

        
        self.id = Note.id
        self.memo = memo
        self.balise = balise
        self.datecreation = datetime.now()
        Note.id +=1
     


     def correspondance(self,terme):
            return terme.lower() in self.memo.lower or terme.lower() in self.balise.lower
note = Note ("voici votre note","test")
print (note.correspondance("note"))