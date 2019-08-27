from random import choice, randint
import string
import hashlib


class Generator:

    @classmethod
    def generate_unbreakable(cls):
        chars = [string.ascii_lowercase,
                 string.ascii_uppercase,
                 string.digits,
                 string.punctuation]

        pass_length = randint(15, 30)

        return hashlib.sha512(''.join([choice(choice(chars)) for i in range(pass_length)]).encode('utf-8')).hexdigest()

    @classmethod
    def generate(cls):
        chars = [string.ascii_lowercase,
                 string.ascii_uppercase,
                 string.digits,
                 string.punctuation]

        pass_length = randint(15, 30)

        return ''.join([choice(choice(chars)) for i in range(pass_length)])