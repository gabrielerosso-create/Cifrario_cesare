def encrypt(text: str, key: int) -> str:
    result = ""

    for char in text:
        if char.isalpha(): # Solo lettere
            if char.isupper(): # Maiuscole
                pos = ord(char) - 65
                new_pos = (pos + key) % 26
                result += chr(new_pos + 65)
            else: # Minuscole
                pos = ord(char) - 97
                new_pos = (pos + key) % 26
                result += chr(new_pos + 97)
        else:

            result += char

    return result


def main():
    #1. Scelta utente
    scelta = input("Vuoi cifrare o decifrare? ").strip().lower()

    # 2. Testo
    messaggio = input("Inserisci il testo: ")

    # 3. Chiave
    chiave = int(input("Inserisci la chiave (numero): "))

    # 4. Decifrare = chiave negativa
    if scelta == "decifrare":
        chiave = -chiave

    # 5. Output
    risultato = encrypt(messaggio, chiave)
    print("Risultato:", risultato)


if __name__ == "__main__":
    main()