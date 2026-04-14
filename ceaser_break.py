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

def brute_force(ciphertext: str) -> list[tuple[int, str]]:
   risultati = []


   for chiave in range(26):
       testo = encrypt(ciphertext, -chiave)
       risultati.append((chiave, testo))


   return risultati

def main():
   print("ATTACCO BRUTE FORCE AL CIFRARIO DI CESARA\n")


   ciphertext = input("Inserisci il testo cifrato : ")


   print("\nProvando tutte le chiavi che sono possibili\n")


   risultati = brute_force(ciphertext)


   for chiave, testo in risultati:
       print(f"Chiave {chiave:2d}: {testo}")




if __name__ == "__main__":
   main()
