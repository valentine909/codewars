class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.encoding_dict = dict(zip(self.alphabet, self.key * (len(self.alphabet) // len(self.key)) + self.key[:len(self.alphabet) % len(self.key)]))
        self.decoding_dict = dict(zip(self.key * (len(self.alphabet) // len(self.key)) + self.key[:len(self.alphabet) % len(self.key)], self.alphabet))

    @staticmethod
    def create_dict(one, two):
        from itertools import cycle
        return dict(zip(one, cycle(two)) if len(one) > len(two) else zip(cycle(one), two))

    def encode(self, text):
        result = ""
        for i in text:
            if i in self.alphabet:
                result += self.encoding_dict[i]
            else:
                result += i
        return result

    def decode(self, text):
        result = ""
        for i in text:
            if i in self.alphabet:
                result += self.decoding_dict[i]
            else:
                result += i
        return result

abc = "abcdefghijklmnopqrstuvwxyz"
ke = "password"
c = VigenereCipher(ke, abc)
print(c.decode('CODEWARS'))
