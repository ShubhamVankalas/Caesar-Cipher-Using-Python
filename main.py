from art import logo

print(logo)
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input(
    "Type 'Encode' to encrypt, type 'Decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(input_text, input_shift):
    encrypt_text = ""
    for letter in input_text:
        if letter in alphabet:
            og_index = alphabet.index(letter)
            final_index = og_index + input_shift
            if final_index > len(alphabet) - 1:
                final_index = 0 + input_shift
                final_index -= ((len(alphabet) - 1) - og_index)
                encrypt_text += alphabet[final_index]
            else:
                encrypt_text += alphabet[final_index]
        else:
            encrypt_text += " "

    print(f"This in encrypted text: '{encrypt_text}'")


def decrypt(input_text, input_shift):
    decrypt_text = ""
    for letter in text:
        if letter in alphabet:
            og_index = alphabet.index(letter)
            final_index = og_index - input_shift
            if final_index < 0:
                final_index = -abs(len(alphabet) - 1)
                final_index += input_shift
                decrypt_text += alphabet[final_index]
            else:
                decrypt_text += alphabet[final_index]
        else:
            decrypt_text += " "

    print(f"This in decrypted text: '{decrypt_text}'")


if direction == "encode":
    encrypt(input_text=text, input_shift=shift)
elif direction == "decode":
    decrypt(input_text=text, input_shift=shift)
else:
    print("Please type either to encode or decode. Check for misspells")
