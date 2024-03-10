class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    def __init__(self,name,pet_type,owner =None) -> None:
        if pet_type not in Pet.PET_TYPES:
              raise Exception(f"{pet_type}is not a valid pet type")
    
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
   


class Owner:
    def __init__(self,name) -> None:
        self.name = name
    
    def pets(self):
        return[pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self,pet):
        if not isinstance(pet , Pet):
              raise Exception("The pet must be an instance of the Pet class.")
        pet.owner = self
    def get_sorted_pets(self):
          return sorted(self.pets(),  key=lambda pet: pet.name)

        

