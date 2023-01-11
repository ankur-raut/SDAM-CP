from sympy import randprime
from math import gcd
def gcd(a,b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:    # gcd * k % mod phi = 1
            return x
    return None
keysize= 11
p1=0
p2=0
p3=0
while p1==p2 or p1==p3 or p2==p3 or (p1*p2*p3)>2**keysize:
    p1=randprime(3,2**keysize)
    p2=randprime(3,2**keysize)
    p3=randprime(3,2**keysize)
    
print("1st Prime Number is " + str(p1))
print("2nd Prime Number is " + str(p2))
print("2nd Prime Number is " + str(p3))

rsa_modulus=p1*p2*p3
totient=(p1-1)*(p2-1)*(p3-1)

e=0 #co prime
for i in range(3,totient-1):
    if gcd(i,totient)==1:
        e=i
        break

print("  Public-Key exponent, e -----> " + str(i))
print("  Public Key -----> (" + str(i) + ", " + str(rsa_modulus) + ")")

d = modinv(e,totient) # private key
# Display the private-key exponent d
print("  Private-Key exponent, d -----> " + str(d))

# Display the private key
print("  Private Key -----> (" + str(d) + ", " + str(rsa_modulus) + ")")


def mod(x,y): # get modulus for 2 number
    if(x<y):
        return y
    else:
        c=x%y
        return c

def encryptString(plainText):
    cipher=""
    for x in list(plainText):
        c = mod(ord(x)**e,rsa_modulus) #
        cipher+=(chr(c))
    return cipher
def decryptString(plainText,d,rsa_modulus):
    plain=""
    d=int(d)
    rsa_modulus=int(rsa_modulus)
    for x in list(plainText):
        c = mod(ord(x)**d,rsa_modulus)
        plain+=(chr(c))
    return plain
# s = input("Enter a text to encrypt: ")
# print("\nPlain message: " + s + "\n")
key = "8ej0IiFQ1vR-sPfZZdNd6aC1hqXTVJElifvsJcAda-U="
from cryptography.fernet import Fernet
# key = Fernet.generate_key()
def encrypt_fernet(message):
    
    print("key ",key)
    fernet = Fernet(key)
    message=str(message)
    encMessage = fernet.encrypt(message.encode())
    return encMessage
    

def encrypt_message(s) :
    enc = encryptString(s)
    d_encrypted=encrypt_fernet(d)
    rsa_encrypted=encrypt_fernet(rsa_modulus)

    print("Encrypted message: " + str(enc) + "\n")
    return enc,d_encrypted,rsa_encrypted
    
    
def decrypt_message(enc,d_encrypted,rsa_encrypted):
    fernet = Fernet(key)
    # d = fernet.decrypt(enc)
    d_decrypted = fernet.decrypt(d_encrypted)
    rsa_decrypted = fernet.decrypt(rsa_encrypted)
    dec = decryptString(enc,d_decrypted,rsa_decrypted)
    print("Decrypted message:"+dec+"\n")
    return dec

# def rot(d,rsa_modulus):
#     l1=len(str(d))
#     l2=len(str(rsa_modulus))
#     s=str(d)+str(rsa_modulus)
#     tmp = s[l1 : ] + s[0 : l1]
#     l1=l1*25
#     l2=l2*25
#     print(tmp)
#     derot(tmp,l1,l2)

# def derot(tmp,l1,l2):
#     # print(type(l1))
#     l1 = int(l1/25)
#     l2 = int(l2/25)
#     tmp = tmp[l2 : ] + tmp[0 : l2]
#     print(tmp)


# "gAAAAABjt-Fm5XQ_i2WDJbGYN1qIMa7c1dwXzGBoUNTOsTfAORLoSpHt1ML40GaltExNbZlcTO6lE84eHuhp2q8fIipo4o3oJg=="
# fernet.encrypt(message.encode())

# print("original string: ", message)
# print("encrypted string: ", encMessage)
# decMessage = fernet.decrypt(encMessage).decode()

# print("decrypted string: ", decMessage)

# gAAAAABjt-Fm5XQ_i2WDJbGYN1qIMa7c1dwXzGBoUNTOsTfAORLoSpHt1ML40GaltExNbZlcTO6lE84eHuhp2q8fIipo4o3oJg==
# key = 8ej0IiFQ1vR-sPfZZdNd6aC1hqXTVJElifvsJcAda-U=
# rot(d,rsa_modulus)
# encrypt(d)
# z,a,b=encrypt_message("heiiiiiii")
# print(z)
# print(decrypt_message(z,a,b))