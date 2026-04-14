def encrypt(text: str, key: int) -> str:
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                pos = ord(char) - 65
                new_pos = (pos + key) % 26
                result += chr(new_pos + 65)
            else:
                pos = ord(char) - 97
                new_pos = (pos + key) % 26
                result += chr(new_pos + 97)
        else:
            result += char

    return result


def main():
    scelta = input("Vuoi cifrare o decifrare? ").strip().lower()
    messaggio = input("Inserisci il testo: ")
    chiave = int(input("Inserisci la chiave (numero): "))

    if scelta == "decifrare":
        chiave = -chiave

    risultato = encrypt(messaggio, chiave)
    print("Risultato:", risultato)


if __name__ == "__main__":
    main()