alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    cipher_text = ""
    # can't shift greater than the # of letters in alphabet
    for letter in text:
        idx = alphabet.index(letter)
        if idx >= len(alphabet) - shift:
            idx -= len(alphabet)
        cipher_idx = idx+shift
        cipher_text += alphabet[cipher_idx]
    print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):
    #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
    #e.g. 
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"
    decrypt_text = ""
    # can't shift to left of first letters in alphabet
    for letter in text:
        idx = alphabet.index(letter)
        if idx <= shift:
            idx = len(alphabet) - (idx-shift)
        decrypt_idx = idx-shift
        decrypt_text += alphabet[decrypt_idx]
    print(f"The decoded text is {decrypt_text}")

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction=="encode":
    encrypt(text=text, shift=shift)
elif direction == "decode":
    decrypt(text=text, shift=shift)
else:
    print("Invalid choice.")