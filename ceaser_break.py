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