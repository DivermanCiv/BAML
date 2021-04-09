from configparser import RawConfigParser
import json

#with open('/baml/BAML/config/config.json', 'r') as fichier:
#    data = json.load(fichier)

#Gestion de config.init
config = RawConfigParser()
config.read('baml/BAML/config/configuration.ini')
print(config.sections())
print(config.get('database', 'nom'))


with open('baml/BAML/config/config.json', 'r') as fichier:
    data = json.load(fichier)

print(data['database'])