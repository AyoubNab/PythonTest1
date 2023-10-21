import time
import random
import string

class Variable:
    def __init__(self, nom_fichier):
        self.nom_fichier = nom_fichier
        self.fichierCree = False
        self.variables = {}

    def creerFichier(self):
        self.name = f"FICHIER_VARIABLE_{self.nom_fichier}.txt"
        self.file = open(self.name, "w")
        self.fichierCree = True

    def obtenirNomFichier(self):
        return self.name

    def ajouterVariable(self, nomVariable, valeur):
        if self.fichierCree:
            if isinstance(valeur, str):
                self.file.write(f"{nomVariable} = '{valeur}'\n")
            else:
                self.file.write(f"{nomVariable} = {valeur}\n")
            self.variables[nomVariable] = valeur

    def obtenirValeur(self, nomVariable):
        if self.fichierCree and nomVariable in self.variables:
            return self.variables[nomVariable]
        return None

    def fermerFichier(self):
        if self.fichierCree:
            self.file.close()

"""-------------------------------------------------------------------------------------------------"""

def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

sizes = [100, 1000, 10_000, 100_000, 1_000_000]

for size in sizes:
    print(f"\nTaille : {size}")

    var = Variable("test")
    var.creerFichier()

    dict_var = {}

    start_time_var = time.time()
    for i in range(size):
        key = random_string(10)
        value = random_string(5)
        var.ajouterVariable(key, value)
    end_time_var = time.time()
    start_time_dict = time.time()
    for i in range(size):
        key = random_string(10)
        value = random_string(5)
        dict_var[key] = value
    end_time_dict = time.time()

    print(f"Temps d'insertion pour la classe Variable : {end_time_var - start_time_var} secondes")
    print(f"Temps d'insertion pour le dictionnaire    : {end_time_dict - start_time_dict} secondes")

    start_time_var = time.time()
    for key in dict_var.keys():
        _ = var.obtenirValeur(key)
    end_time_var = time.time()
    start_time_dict = time.time()
    for key in dict_var.keys():
        _ = dict_var[key]
    end_time_dict = time.time()

    print(f"Temps de lecture pour la classe Variable  : {end_time_var - start_time_var} secondes")
    print(f"Temps de lecture pour le dictionnaire     : {end_time_dict - start_time_dict} secondes")
