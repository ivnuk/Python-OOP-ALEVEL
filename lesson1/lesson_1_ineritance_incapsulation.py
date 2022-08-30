from datetime import datetime
from typing import List


class Primate:
    eye_color = "Blue"
    is_human = False

    def eat(self, food):
        return f"Eating {food}"

    def walk(self, from_, to_) -> str:
        return f"Walking on four from {from_} to {to_}"

    def _inhale(self) -> None:
        print("Inhale")

    def __exhale(self):
        print("exhale")

    def _exhale_with_sound(self, word):
        print(f"Talking '{word}'")


class Human(Primate):
    first_name = 'John'
    last_name = 'Doe'
    date_of_birth = datetime.strptime("01/04/1961", "%d/%m/%Y")

    def talk_word(self, word):
        self._inhale()
        self._exhale_with_sound(word)
        self.__exhale()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def walk(self, from_, to_):
        return f"{self.get_full_name()} walking straight from {from_} to {to_}"

    def age(self):
        return (datetime.now() - self.date_of_birth).days // 365


if __name__ == '__main__':
    john = Human()
    print("First Name:", john.first_name)
    print("Full Name:", john.get_full_name())
    print("Eye color:", john.eye_color)
    print("Eat apple:", john.eat('apple'))
    john.talk_word("Hello World!")

    john._inhale()
    john.__exhale()
