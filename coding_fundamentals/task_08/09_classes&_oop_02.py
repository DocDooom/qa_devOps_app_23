from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name, sound, special_trait=None):
        self.name = name
        self.sound = sound


class Owl(Bird):
    def __init__(self):
        super().__init__("Owl", "Toot")
        self.special_trait = "Awake at night"

class Dodo(Bird):
    def __init__(self):
        super().__init__("Dodo", "None")
        self.special_trait = "Can't fly!"


owl = Owl()
dodo = Dodo()

bird = Bird("some", "something")

print(owl.special_trait)
print(dodo.special_trait)
print(bird.name)