def encrypt(text:str, key:int)->str :
    result = ""
    for char in text:
        # Gestione delle lettere minuscole
        if char.isalpha():
            if char.isupper():
            index = (ord(char) - 65 + key) % 26
            result += chr(index + 65)

            else:

            index = (ord(char) - 97 + key) % 26
            result += chr(index + 97)
        else:
            # Caratteri speciali, spazi e numeri restano invariati
            result += char
    return result


def main():
    # Qui aggiungi la parte interattiva (input utente)
    scelta = input("Vuoi cifrare o decifrare? ")
    messaggio = input("Inserisci il testo: ")
    chiave = int(input("Inserisci la (chiave numero): "))

    if scelta.lower() == 'decifrare':
        chiave = -chiave

    print("Risultato:", encrypt(messaggio, chiave))


if __name__ == "__main__":
    main()