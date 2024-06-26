from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    n = SecretInteger(Input(name="n", party=party1))
    if n <= Integer(1):
        return [Output(n, "fibonacci_output", party1)]
    else:
        a, b = Integer(0), Integer(1)
        counter=2
        while((n+Integer(1)<Integer(counter))):
            a, b = b, a + b
            counter+=1
    return [Output(b, "fibonacci_output", party1)]
