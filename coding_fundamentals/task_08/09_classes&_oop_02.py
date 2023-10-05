from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name, sound, special_trait=None):
        self.name = name
        self.sound = sound

    @abstractmethod
    def make_sound(self):
        pass


class Owl(Bird):
    def __init__(self):
        super().__init__("Owl", "Toot")
        self.special_trait = "Awake at night"

    def make_sound(self):
        print("toot toot")


class Dodo(Bird):
    def __init__(self):
        super().__init__("Dodo", "None")
        self.special_trait = "Can't fly!"

    def make_sound(self):
        print("some sound!")


owl = Owl()
dodo = Dodo()

print(owl.special_trait)
print(dodo.special_trait)