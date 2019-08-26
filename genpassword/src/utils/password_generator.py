from random import choice, randint
import string


class Generator:

    @classmethod
    def generate(cls):
        chars = [string.ascii_lowercase,
                 string.ascii_uppercase,
                 string.digits]

        pass_length = randint(10, 20)

        return ''.join([choice(choice(chars)) for i in range(pass_length)])


