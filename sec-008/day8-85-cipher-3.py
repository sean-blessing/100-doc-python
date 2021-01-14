alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(text, shift, direction):
    new_text = ""
    # can't shift to left of first letters in alphabet
    for letter in text:
        idx = alphabet.index(letter)
        print(f"letter = {letter}")
        new_idx = 0
        if direction=="encode":
            if idx >= (len(alphabet) - shift):
                idx -= len(alphabet)
            new_idx = idx+shift
        elif direction=="decode":
            new_idx = idx-shift
            if new_idx < 0:
                new_idx = len(alphabet) + new_idx
        print(f"new_idx={new_idx}")
        new_text += alphabet[new_idx]
    print(f"The {direction}d text is {new_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text,shift,direction)