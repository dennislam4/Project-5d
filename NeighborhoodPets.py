# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 10-22-2022
# Description: Program contating NeighborhoodPets class that has methods for adding, deleting and searching for an
# owner's pet. It saves that data to a JSON file and loads that data to get a set of all the pet species.

import json


class DuplicateNameError(Exception):
    pass


class NeighborhoodPets:
    """Class that represents Neigborhood pets"""

    def __init(self):
        self.pet_dict = {}

    def add_pet(self, name, species, owner_name):
        """
        Add pet method that adds pet to the pet_dictionary set including the name of the pet, species and the owner's
        name.
        """
        if name in self.pet_dict:
            raise DuplicateNameError
        else:
            self.pet_dict[name] = {'name': name, 'species': species, 'owner name': owner_name}

    def delete_pet(self, name):
        """Delete pet method that deletes the pet from pet_dictionary."""
        if name in self.pet_dict:
            del self.pet_dict[name]

    def get_owner(self, name):
        """Get method that returns the name of the owner from pet name in pet_dictionary"""
        if name in self.pet_dict:
            return self.pet_dict[name]['owner name']
        if name not in self.pet_dict:
            pass

    def save_as_json(self, file_name):
        """Save method that saves file as .json"""
        with open(file_name, 'w') as outfile:
            json.dump(self.pet_dict, outfile)

    def read_json(self, file_name):
        """Reads .json file"""

        with open(file_name, 'r') as infile:
            self.pet_dict = json.load(infile)

    def get_all_species(self):
        """Get method which returns all the species of the pets"""
        return self.pet_dict.get('species')
