import json
import os
from logic.classes.edoc import Edoc

PATH = os.getcwd()
DIR_DATA = PATH + '{0}data{0}'.format(os.sep)


class EdocController(object):
    def __init__(self):
        self.file = '{0}{1}'.format(DIR_DATA, 'edoc_storage.json')

    def add(self, edoc: Edoc = Edoc()) -> str:
        with open(self.file, 'r+') as f:
            data = json.load(f)
            data['edoc'].append(edoc.__str__())
            f.seek(0)
            json.dump(data, f)
        f.close()
        return edoc.__str__()

    def show(self):
        # Opening JSON file
        with open(self.file, 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        return json_object
