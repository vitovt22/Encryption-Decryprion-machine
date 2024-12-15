# Vigenère Cipher for Encryption and Decryption in Ukrainian

key = "тарасгригоровичшевченко"

def encrypt_message(message, key):
    """
    Encrypts the given message using the Vigenère cipher.
    : message: The plaintext message to encrypt.
    : key: The encryption key.
    :return: The encrypted message.
    """
    def vigenere(message, key, direction=1):
        key_index = 0
        alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
        final_message = ''

        for char in message.lower():
            if char not in alphabet:
                final_message += char  # Non-alphabet characters remain unchanged
            else:
                key_char = key[key_index % len(key)]
                key_index += 1

                offset = alphabet.index(key_char)
                index = alphabet.find(char)
                new_index = (index + offset * direction) % len(alphabet)
                final_message += alphabet[new_index]

        return final_message

    try:
        encrypted = vigenere(message, key, 1)
        print("Encrypted message:", encrypted)
        return encrypted
    except Exception as e:
        print(f"Error during encryption: {e}")


def decrypt_message(encrypted_message, key):
    """
    Decrypts the given message using the Vigenère cipher.
    : encrypted_message: The ciphertext to decrypt.
    : key: The decryption key.
    :return: The decrypted message.
    """
    def vigenere(message, key, direction=-1):
        key_index = 0
        alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
        final_message = ''

        for char in message.lower():
            if char not in alphabet:
                final_message += char  # Non-alphabet characters remain unchanged
            else:
                key_char = key[key_index % len(key)]
                key_index += 1

                offset = alphabet.index(key_char)
                index = alphabet.find(char)
                new_index = (index + offset * direction) % len(alphabet)
                final_message += alphabet[new_index]

        return final_message

    try:
        decrypted = vigenere(encrypted_message, key, -1)
        print("Decrypted message:", decrypted)
        return decrypted
    except Exception as e:
        print(f"Error during decryption: {e}")


def main():
    """
    Main function to provide a menu for the encryption/decryption machine.
    """
    print('Hello!')

    while True:
        print('\nEncryption machine')
        print('1. Encrypt message')
        print('2. Decrypt message')
        print('3. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            message = input('Enter your message to encrypt: ')
            encrypt_message(message, key)

        elif choice == '2':
            encrypted_message = input('Enter your message to decrypt: ')
            decrypt_message(encrypted_message, key)

        elif choice == '3':
            print('Exiting the program.')
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
