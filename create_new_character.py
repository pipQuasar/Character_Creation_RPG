from abc import ABC,abstractclassmethod
class Race(ABC):
    def __init__(self,pasive):
        self.pasive = pasive
        
    @abstractclassmethod
    def pasive_skill(self):
        return f"Pasive skill: {self.pasive}"

Ratifero = Race("lil rat, +1 AGI")
Orc = Race("0 patience, +1 ATQ")
Human = Race("wazaaa, +1 INT")
Elf = Race("nuh uh, +1 MAN")
Ent = Race("Yo, +1 VIT")


class Class:
    def __init__(self, vit, man, atq, agi, itg):
        self.vit = vit
        self.man = man
        self.atq = atq
        self.agi = agi
        self.itg = itg



class Character:
    pass