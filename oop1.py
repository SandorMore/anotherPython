import random
import time as t

class PlayerCharacter:
    def __init__(self, name, HP, DMG, ARMOR, LUCK, SPEED):
        self.name = name
        self.DMG = DMG
        self.HP = HP
        self.ARMOR = ARMOR
        self.LUCK = LUCK
        self.SPEED = SPEED
    def Attack(self, target): 
        '''
        Basic attack függvény nem ad vissza semmit. Kalkulál egy sebzést a self sebzése és a target armorja alapján. Amennyiben a Calculate dodge függvény True-t ad vissza. A sebzés meghiúsult.

        :Parameters: slef, target target az ellenség self maga a karakter!
        '''
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
        '''
        Kiszámolja a dodgot a self LUCKja alapján.

        :Return: True ha a Luck és egy random szám 1 és 100 között összege nagyobb mint 75. False mindig máskor.

        :Parameters: self, maga a karakter
        '''
        self.DODGE = random.randint(1,100) + self.LUCK
        if self.DODGE >= 75:
            return True
        else:
            return False


def Harcrendszer(harc_tagjai = []):
    '''
    Bubble sortolja a harc_tagjai listátá ami egy teljes roster ami az elérhető ellenfelekből áll!

    :Parameters: harc_tagjai[]

    '''
    for harcosok in harc_tagjai:
        for j in harcosok:

            if j[harcosok].SPEED > j[harcosok + 1].SPEED:
                j[harcosok], j[harcosok + 1] = j[harcosok + 1], j[harcosok]
            
    def Harc(harcosok):
        '''
        Elindítja a harc funkciót. Kérdés elé állítja a játékost, hogy szeretne-e harcolni és ez alapján indít egy while ciklust!

        :Parameters: harcosok[] .SPEED orderben, ők fognak harcolni
        '''
        harc = True
        while harc:
            print("Mit szeretnél?")
            print("1 ha harcolni szeretnél!")
            print("2 ha meneküni szeretnél!")
            print("3 ha beszélni szeretnél!")
            kerdes = int(input(f"Válassz: "))
            if kerdes == 1:
                print("Harc! Készülj a küzdelemre!")
            elif kerdes == 2:
                print("Menekülés! Fuss az életedért!")
            elif kerdes == 3:
                print("Beszélgetni próbálsz!")
                print('\n')
                print("A szörnynek nincs semmi mondanivalója! Harc!")

player1 = PlayerCharacter("player1", 100, 15, 5, 12)
player2 = PlayerCharacter("player2", 200, 4, 20, 8)
player1.Attack(player2)
player2.Attack(player1)



