class Class:
    def __init__(self, vit, man, atq, agi, itg, des):
        self.vit = vit
        self.man = man
        self.atq = atq
        self.agi = agi
        self.itg = itg
        self.des = des

    def __str__(self):
        print(f"VIT: {self.vit}\nMAN: {self.man}\nATQ: {self.atq}\nAGI: {self.agi}\nDES: {self.des}\nINT: {self.itg}")

warrior = Class("●●●●●●●○○○","●●●●○○○○○○","●●●●●●●●○○","●●●●●○○○○○","●●●○○○○○○○","●●●●●●○○○○")
paladin = Class("●●●●●●●○○○","●●●●●●○○○○","●●●●●●○○○○","●●●●●○○○○○","●●●●●○○○○○","●●●●○○○○○○")
archer = Class("●●●●●○○○○○","●●●●●○○○○○","●●●●●●●○○○","●●●●●●●○○○","●●●●●●○○○○","●●●○○○○○○○")
mage = Class("●●●●○○○○○○","●●●●●●●●●○","●●●●●●○○○○","●●●●○○○○○○","●●●●●●●●○○","●●●○○○○○○○")

class Character:
    pass