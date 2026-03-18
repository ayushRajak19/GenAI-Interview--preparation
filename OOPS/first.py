class Animal:
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

    def __repr__(self):
        return f"Animal(name={self.name})"


class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name, sound="Woof")  # inherit parent init
        self.tricks = []

    def learn_trick(self, trick: str):
        self.tricks.append(trick)

    def show_tricks(self):
        if not self.tricks:
            return f"{self.name} knows no tricks yet"
        return f"{self.name} knows: {', '.join(self.tricks)}"


dog = Dog("Bruno")
print(dog.speak())        # Bruno says Woof
print(dog)                # Animal(name=Bruno) ← __repr__
dog.learn_trick("sit")
dog.learn_trick("shake")
print(dog.show_tricks())  # Bruno knows: sit, shake