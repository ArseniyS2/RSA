from math import isqrt
import random

def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

def create_primes() -> int:
    while True:
        a = random.randint(10, 50)
        if is_prime(a) is True:
            return a


def compute_lcm(a, b: int) -> int:
    greater = greater_num(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        else:
            greater += 1

def greater_num(a, b: int) -> int:
    if a > b:
        return a
    else:
        return b
    
def totient_func(a, b: int) -> int:
    return compute_lcm(a - 1, b - 1)

def coprime_calc(a, b: int) -> bool:
    num = 2
    greater = greater_num(a, b)
    while True:
        if a % num == 0 and b % num == 0:
            return False
        num += 1
        if num == greater:
            return True

def creating_e(a, b) -> int:
    while True:
        c = totient_func(a, b)
        e = random.randrange(3, c)
        if coprime_calc(e, c) is True:
            return e

def creating_d(a, b) -> int: 
    return pow(creating_e(a, b), -1, totient_func(a, b))

class Key_Pair_Generation:
    def __init__(self) -> None:
        self.p = create_primes()
        self.q = create_primes()
        self.n = self.p * self.q
        self.e = creating_e(self.p, self.q)
        self.d = pow(self.e, -1, totient_func(self.p, self.q))
    
    def publickey(self):
        return (self.n, self.e)
    
    def privatekey(self):
        return (self.n, self.d)

    def encrypt(self, m):
        new_letter = ord(m)
        cipher = (new_letter**self.e) % self.n
        return cipher
    
    def decrypt(self, s):
        letter = (s**self.d) % self.n
        plain_text = bytes([letter]).decode('ascii')
        return plain_text


if __name__ == "__main__":
    keys = Key_Pair_Generation()
    while True:
        inp = int(input("What do you want to do: (1 - encrypt, 2 - decrypt, 3 - print public key, 4 - print private key, 5 - exit): "))
        if inp == 1:
            plain_text = input("Write text to encrypt: ")
            cipher_text = ""
            for letter in plain_text:
                cipher_text += str(keys.encrypt(letter)) + " "
            print(f"Your encrypted text is: {cipher_text}")

        elif inp == 2:
            text = input('Write your text to decrypt: ')
            text = text.split()
            decrypted = ''
            for i in text:
                i = int(i)
                decrypted += keys.decrypt(i)
            print(f"Your decrypted text is: {decrypted}")

        elif inp == 3:
            print(f"Your public key is: {keys.publickey()}")
        
        elif inp == 4:
            print(f"Your private key is: {keys.privatekey()}")
        
        elif inp == 5:
            break

        else:
            print('Invalid command, try again')
#print(is_prime(int(input("Write a number: "))))