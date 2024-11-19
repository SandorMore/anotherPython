import random

class PlayerCharacter:
    def __init__(self, name, HP, DMG, ARMOR, LUCK, SPEED):
        self.name = name
        self.DMG = DMG
        self.HP = HP
        self.ARMOR = ARMOR
        self.LUCK = LUCK
        self.SPEED = SPEED
    def Attack(self, target): 
        damage_dealt = (self.DMG * 3) - target.ARMOR
        
        if self.CalculateDodge() == True:
            print(f"{self.name} sikersen kitért!")
            damage_dealt = 0
        elif self.CalculateDodge() == False:
            print("Kitérési prúbálkozás meghíúsúlt!")
            target.HP -= damage_dealt
            print(f"{self.name} megtámadta {target.name}-et és {damage_dealt} mennyiségű sebzést okozott!")
        print(f"{target.name}-nek ennyi HP-ja maradt: {target.HP}")
    def CalculateDodge(self):
        self.DODGE = random.randint(1,100) + self.LUCK
        if self.DODGE >= 75:
            return True
        else:
            return False


def Harcrendszer(harc_tagjai = []):
    for harcosok in harc_tagjai:
        for j in harcosok:

            if j[harcosok].SPEED > j[harcosok + 1].SPEED:
                j[harcosok], j[harcosok + 1] = j[harcosok + 1], j[harcosok]
            
    def Harc():
        pass


player1 = PlayerCharacter("player1", 100, 15, 5, 12)
player2 = PlayerCharacter("player2", 200, 4, 20, 8)
player1.Attack(player2)
player2.Attack(player1)



