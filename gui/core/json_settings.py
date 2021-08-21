import json
import os


class Settings(object): # App settings
    json_file = "settings.json"
    app_path = os.path.abspath(os.getcwd())
    settings_path = os.path.normpath(os.path.join(app_path, json_file))
    if not os.path.isfile(settings_path):
        print(f"WARNING: \"settings.json\" not found! check in the folder {settings_path}")

    def __init__(self): # Initialize settings
        super(Settings, self).__init__()

        self.items = {} # Settings dict

        self.deserialize()

    def serialize(self): # Serialize JSON
        with open(self.settings_path, "w", encoding='utf-8') as write:
            json.dump(self.items, write, indent=4)

    def deserialize(self): # Deserialize JSON
        with open(self.settings_path, "r", encoding='utf-8') as reader:
            settings = json.loads(reader.read())
            self.items = settings