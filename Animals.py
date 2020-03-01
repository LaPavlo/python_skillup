from faker import Faker
from collections import defaultdict

fake = Faker()


class Animals:
    def bite(self):
        print("Biting with my sharp tooth, grrr")


class Predators(Animals):
    def __init__(self, name):
        self.name = name

    def chase(self, speed):
        print("Chasing with " + str(speed) + " speed")

    def roar(self):
        print("My name is " + self.name + " and i like to roar")


class Lion(Predators):
    def __init__(self, name, pride=None):
        super().__init__(name)
        self.pride = pride

    def lion_hunting(self):
        if self.pride:
            print("My pride name is " + self.pride + " and we are hunting together")
        else:
            print("I don't have pride, because i like to hunt alone")


class Cheetah(Predators):
    def __init__(self, name):
        super().__init__(name)

    def cheetah_hunting(self):
        print("I am fastest land Animal on the planet")


lion1 = Lion(fake.name(), "Pacani iz Savani")
lion2 = Lion(fake.name(), "Lion's neighborhood")
lion3 = Lion(fake.name(), "Lions4life")
lion4 = Lion(fake.name(), "Lion gang")
lion5 = Lion(fake.name(), "Lion gang")
lion6 = Lion(fake.name())
cheetah1 = Cheetah(fake.name())


def name_to_pride(lions_list):
    lions_dict = {i.pride: i.name for i in lions_list if i.pride is not None}
    return lions_dict


def name_to_pride_advanced(lions_list):
    d = defaultdict(list)
    for i in lions_list:
        if i.pride is not None:
            d[i.pride].append(i.name)
    return dict(d)


lion1.lion_hunting()
lion1.roar()
lion1.chase(50)
lion1.bite()
print("++++++++++++++")
lion3.lion_hunting()
lion3.roar()
lion3.chase(50)
lion3.bite()
print("++++++++++++++")
lion4.roar()
print("++++++++++++++")
lion5.bite()
print("++++++++++++++")
lion6.lion_hunting()
lion6.roar()
lion6.chase(70)
lion6.bite()
print("++++++++++++++")
cheetah1.roar()
cheetah1.chase(120)
cheetah1.bite()
cheetah1.cheetah_hunting()
print("++++++++++++++")
print(name_to_pride([lion1, lion2, lion3, lion4, lion5, lion6]))
print("++++++++++++++")
print(name_to_pride_advanced([lion1, lion2, lion3, lion4, lion5, lion6]))
