from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name, sound, special_trait=None):
        self.name = name
        self.sound = sound

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return "This is a string"


class Owl(Bird):

    output_str = ""

    def __init__(self):
        super().__init__("Owl", "Toot")
        self.special_trait = "Awake at night"

    def make_sound(self):
        print("toot toot")

    def __repr__(self):
        # output_str += super().__repr__(self)
        output_str = "This is another string!!!"
        return output_str


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

print(owl)
