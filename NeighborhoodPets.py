# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 10-22-2022
# Description: Program containing NeighborhoodPets class that has methods for adding, deleting and searching for an
# owner's pet. It saves that data to a JSON file and loads that data to get a set of all the pet species.
import json


class DuplicateNameError(Exception):
    pass


class NeighborhoodPets:
    """Class that represents Neigborhood pets"""
    def __init__(self):
        self._pet_dict = {}

    def add_pet(self, name, species, owner_name):
        """
        Add pet method that adds pet to the pet_dictionary set including the name of the pet, species and the owner's
        name.
        """
        if name in self._pet_dict:
            raise DuplicateNameError

        else:
            self._pet_dict[name] = {'name': name, 'species': species, 'owner name': owner_name}

    def delete_pet(self, name):
        """Delete pet method that deletes the pet from pet_dictionary."""
        if name in self._pet_dict:
            del self._pet_dict[name]

    def get_owner(self, name):
        """Get method that returns the name of the owner from pet name in pet_dictionary"""
        if name in self._pet_dict:
            return self._pet_dict[name]['owner name']

    def save_as_json(self, json_file):
        """Save method that saves file as .json"""
        with open(json_file, 'w') as outfile:
            json.dump(self._pet_dict, outfile)

    def read_json(self, json_file):
        """Reads .json file"""
        with open(json_file, 'r') as infile:
            self._pet_dict = json.load(infile)

    def get_all_species(self):
        """Get method which returns all the species of the pets"""
        return self._pet_dict.get('species')
