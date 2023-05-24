#si with fixed andvariable rate
def simple_intrest(p,t,r=3):
    si=(p*t*r)/100
    return si
def main():
    a=simple_intrest(6000,1)
    b=simple_intrest(2000,1,r=2.5)
    print(f'si with fixed rate {a:.3f}')
    print(f'si with variable rate {b:.3f}')
main()
