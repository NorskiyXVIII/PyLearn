import abc

class Entity(abc.ABC):
    __name = "Undefined"
    __hp   = 0
    __dmg   = 0

    def __init__(self, name = "Entity", hp = 100, dmg = 10):
        self.__name = name
        self.__hp   = hp
        self.__dmg  = dmg

    def __str__(self):
        return f"Entity(Unknown)<{self.name}>[hp: {self.hp}, dmg: {self.dmg}]"

    @abc.abstractmethod
    def __add__(self, other):
        pass

    def __eq__(self, other):
        return self.hp == other.hp and self.dmg == other.hp
    
    def __ne__(self, other):
        return not(self == other)

    def __gt__(self, other):
        return self.hp > other.hp and self.dmg > other.hp
    def __ge__(self, other):
        return self.hp >= other.hp and self.dmg >= other.hp

    def __lt__(self, other):
        return self.hp < other.hp and self.dmg < other.hp
    def __le__(self, other):
        return self.hp <= other.hp and self.dmg <= other.hp

    def __getitem__(self, indx):
        if indx   == "name": return self.name
        elif indx == "hp":   return self.hp
        elif indx == "dmg":  return self.dmg

        return None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def hp(self):
        return self.__hp


    @hp.setter
    def hp(self, hp):
        if self.__hp == hp or self.__hp * 10 <= hp:
            return
        self.__hp = hp
    
    @property
    def dmg(self):
        return self.__dmg

    @dmg.setter
    def dmg(self, dmg):
        if self.__dmg == dmg or self.__dmg * 10 <= dmg:
            return
        self.__dmg = dmg

    @abc.abstractmethod
    def attack(self, attacked):
        pass

    @abc.abstractmethod
    def display(self):
        pass


class Skeleton (Entity):
    def __init__(self, name = "Skeleton", hp = 100, dmg = 10):
        super().__init__(name, hp, dmg)

    def __str__(self):
        return f"Skeleton<{self.name}>[hp: {self.hp}, dmg: {self.dmg}]"
    
    def __add__(self, other):
        return Skeleton(self.name, self.hp + other.hp, self.dmg + other.dmg)

    def attack(self, attacked):
        attacked.hp -= self.dmg

    def display(self):
        print(self)

vasya = Skeleton("Вася", 50, 30)
danil = Skeleton("Данил", 135, 10)

vasya.display()
danil.display()
print("-----------")

vasya.attack(danil)

vasya.display()
danil.display()
print("-----------")

vasya.dmg = 150
vasya.attack(danil)

vasya.display()
danil.display()
print("-----------")
print(f"{vasya + danil} and {vasya > danil}")
print(vasya["name"], vasya["hp"], vasya["dmg"])