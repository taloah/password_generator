import string
import secrets

def pass_gen(alphabet:str):

    pwd = ''
    length = int(input('Enter the length of your password: '))

    for _ in range(length):
        pwd = pwd + secrets.choice(alphabet)
    return pwd


alphabet = string.printable

def main():
    print(pass_gen(alphabet))
    
if __name__ == "__main__":
    main()
