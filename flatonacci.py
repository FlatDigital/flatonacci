"""
Flatonacci secuence is a secuence which is result from the same given secuence 
plus the sum of the last 3 numbers of the secuence. 

The challenge is to create a flatonacci function that given a signature returns the first 
n elements - signature included of the so seeded sequence. So, if we are to 
start our Flatonacci sequence with [1, 1, 1] as a starting input (AKA signature) and n = 8,
we have this sequence:

[1, 1 ,1, 3, 5, 9, 17, 31]

Another example; if signature is the secuence [0, 0, 1] we should get some thing
like:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]

- Signature will always contain 3 numbers 
- n will always be a non-negative number
- if n == 0, then return an empty list and be ready for anything else which is not
clearly specified ;)

Note. Please note that we are gonna test the funcion against a lot of different signatures and n's
"""

SIGNATURE_LENGTH = 3


def flatonacci(signature: list, n: int) -> list:
    for i in range(n - SIGNATURE_LENGTH):
        first = signature[i]
        middle = signature[i + 1]
        last = signature[i + 2]
        val = last + middle + first
        signature.append(val)
    return signature


def read_signature() -> list:
    count = 1
    signature = []
    while count <= SIGNATURE_LENGTH:
        val = input('Enter seed: ')
        if not val.isdigit():
            continue
        else:
            val = int(val)
            signature.append(val)
            count += 1
    return signature


def run():
    menu = """
- Press 0 - to finish
- Press any key to new flatonacci
"""
    option = '1'
    while option != '0':
        n = input('Enter number of elements: ')
        if not n.isdigit():
            print('Bad Choice!!!: ')
            option = input(menu)
        else:
            n = int(n)
            signature = read_signature()
            result = flatonacci(signature, n)
            print('¡¡¡FLATONACCI!!!')
            print(result)
            option = input(menu)


if __name__ == '__main__':
    run()
