import json
import os


# KARDB CLASS

class kardb:
    def __init__(self,dbname):
        self.dbname = dbname
        self.docname = 'main'

        self.createdirs()

        self.data = {}
        self.load()


    def load(self):
        filepath = f'{self.dbname}/{self.docname}.json'

        if os.path.exists(filepath):
            with open(filepath,'r') as f:
                data = json.load(f)

            self.data = data

    def save(self,indent=3):
        filepath = f'{self.dbname}/{self.docname}.json'

        with open(filepath,'w') as f:
            json.dump(self.data,f,indent=indent)

    def createdirs(self):
        directory = os.path.dirname(f'./{self.dbname}/')

        if directory and not os.path.exists(directory):
            os.makedirs(directory)

    def getdirs(self):
        directory = os.path.dirname(f'./{self.dbname}/')

        return directory
