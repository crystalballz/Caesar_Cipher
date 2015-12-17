def caesar(plaintext,shift):

    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l",
    "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    dic={}
    for i in range(0,len(alphabet)):
        dic[alphabet[i]]=alphabet[(i+shift)%len(alphabet)]

    ciphertext=""
    for l in plaintext.lower():
        if l in dic:
            l=dic[l]
        ciphertext+=l

    return ciphertext

plaintext=raw_input("What text file do we want to encrypt?")
shift=raw_input("How many characters do you want to shift?")
print "Plaintext:", plaintext
print "Cipertext:",caesar(plaintext,shift)

