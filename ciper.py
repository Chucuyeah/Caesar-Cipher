def caesar_cipher(text, shift, encrypt=True):
    result = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char_code = ord(char.lower()) - ord('a')
            
            if encrypt:
                char_code = (char_code + shift) % 26
            else:
                char_code = (char_code - shift) % 26
            
            char_code += ord('a')
            
            if is_upper:
                result += chr(char_code).upper()
            else:
                result += chr(char_code)
        else:
            result += char

    return result

# Pilihan untuk enkripsi atau dekripsi
choice = input("Pilih 'e' untuk enkripsi atau 'd' untuk dekripsi: ").lower()

plaintext = input("Masukkan pesan: ")
shift_amount = int(input("Masukkan jumlah pergeseran: "))

if choice == 'e':
    cipher_text = caesar_cipher(plaintext, shift_amount, encrypt=True)
    print("Pesan terenkripsi:", cipher_text)
elif choice == 'd':
    decrypted_text = caesar_cipher(plaintext, shift_amount, encrypt=False)
    print("Pesan terdekripsi:", decrypted_text)
else:
    print("Pilihan tidak valid. Silakan pilih 'e' untuk enkripsi atau 'd' untuk dekripsi.")
