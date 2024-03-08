import json
import os


# KARDB CLASS

class kardb:
    def __init__(self,dbname):
        self.dbname = dbname
        self.docname = 'main'
        self.createdirs()
        self.load()


    def load(self):
        filepath = f'{self.dbname}/{self.docname}.json'

        if os.path.exists(filepath):
            with open(filepath,'r') as f:
                data = json.load(f)

            self.data = data

        else:
            self.data = {}


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


    def createdoc(self,docname):
        data = {}
        path = f'{self.dbname}/{docname}.json'

        with open(path,'w') as f:
            json.dump(data,f)


    def changedoc(self,docname):
        self.save()

        self.docname = docname

        self.load()


    def cacdoc(self,docname):
        self.createdoc(docname)
        self.changedoc(docname)


    def renamedoc(self,old_docname,new_docname):
        path = f'{self.dbname}/{old_docname}.json'
        new_path = f'{self.dbname}/{new_docname}.json'

        os.rename(path,new_path)

        if self.docname = old_docname:
            self.changedoc(new_docname)
            self.load()


    def deletedoc(self,docname):
        path = f'{self.dbname}/{docname}.json'

        os.remove(path)

        if self.docname = docname:
            path = f'{self.dbname}/main.json'

            if os.path.exists(path):
                self.changedoc('main')
            else:
                self.cacdoc('main')


    def updatedoc(self, branch, docname=self.docname, indent=3):
        path = f'{self.dbname}/{docname}.json'

        with open(path,'r') as f:
            data = json.load(f)

        data.update(branch)

        with open(path,'w') as f:
            json.dump(data,f,inden)


    def doctype(self, docname=self.docname):
        if not docname == self.docname:
            path = f'{self.dbname}/{docname}.json'

            with open(path,'r') as f:
                data = json.load(f)

            return type(data)

        else:
            return type(self.data)