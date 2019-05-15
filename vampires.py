class Vampire:

    coven = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.in_coffin = True
        self.drank_blood_today = False
    
    def __str__(self):
        return f"Name of Vampire: {self.name}\nAge: {self.age}\nIn coffin: {self.in_coffin}\nDrank Blood Today: {self.drank_blood_today}"

    def __repr__(self):
        return f"{self.name} (Drank Blood: {self.drank_blood_today}  In Coffin: {self.in_coffin})"

    @classmethod
    def create(cls, name, age):
        new_vampire = Vampire(name, age)
        cls.coven.append(new_vampire)
        return new_vampire
    
    @classmethod
    def sunrise(cls):
        for vampire in Vampire.coven:
            if vampire.in_coffin == False or vampire.drank_blood_today == False:
                cls.coven.remove(vampire) 
        return f'Survivors after sunrise: {Vampire.coven}'
    
    @classmethod
    def sunset(cls):
        for vampire in cls.coven:
            Vampire.drank_blood_today = False
            Vampire.in_coffin = False
        return f"After sunset:\nThese all vampires are out of coffin and looking for blood:\n {Vampire.coven}"

    def drink_blood(self):
        self.drank_blood_today = True
    
    def go_home(self):
        self.in_coffin = True



v1 = Vampire.create("Bella", 20000)
v2 = Vampire.create("Elizabeth", 100)
v3 = Vampire.create("Zurie", 200)
v4 = Vampire.create("Ambrosiat", 50000)

print(v1)

print()

print(v2)

print()

print(v3)

print()

print(v4)
print()

print(Vampire.coven[1].drank_blood_today)

print(Vampire.sunset())
(v1.drink_blood())
(v3.drink_blood())
(v4.drink_blood())

print()

print(Vampire.sunrise())
(v1.go_home())
(v2.go_home())
(v3.go_home())
(v4.go_home())

print(Vampire.coven[0].drank_blood_today)

print(Vampire.coven[1].drank_blood_today)

print(Vampire.coven[0].in_coffin)

print(Vampire.coven[2].in_coffin)

print()

print(Vampire.coven)





