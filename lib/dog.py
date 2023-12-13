#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self,name,breed):
        self._name=name
        self._breed=breed

    def get_name(self):
        print ("Retrieving name.")
        return self._name
    
    def set_name(self,name):
        if (not isinstance(name,str)) or not (1<= len(name) <=25):
           print ("Name must be string between 1 and 25 characters")
            
        
        else:
            self._name=name   

fido= Dog(123)
print (fido._name)