#simple calculator
def main():
    n1,n2=map(int,input().split())
    opt=input("enter the operator :")
    match(opt):
        case '+':
            print(f'sum of {n1} and {n2} is {n1+n2}')
        case '-':
            print(f'differ of {n1} and {n2} is {n1-n2}')
        case '*':
            print(f'multi of {n1} and {n2} is {n1*n2}')
        case '/':
            print(f'divi of {n1} and {n2} is {n1/n2}')
        case _:
            print("invalid operator")
main()
