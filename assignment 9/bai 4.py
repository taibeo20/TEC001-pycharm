def caesar_cipher_file(input_file, output_file, shift, direction):
    if direction == "left":
        shift = -shift

    result = ""

    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            for char in line:
                if char.isupper():
                    new_char = chr((ord(char) - 65 + shift) % 26 + 65)
                    result += new_char

                elif char.islower():
                    new_char = chr((ord(char) - 97 + shift) % 26 + 97)
                    result += new_char

                else:
                    result += char

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(result)