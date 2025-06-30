import random
import string

print("Welcome to the Password Generator!")
length_of_word =int(input("Enter the total number of characters in the password: "))
length_of_litters = int(input("Enter the number of letters in the password: "))
length_of_numbers = int(input("Enter the number of numbers in the password: "))
length_of_symbols = int(input("Enter the number of symbols in the password: "))
thetotal = length_of_litters+length_of_numbers+length_of_symbols

if thetotal!= length_of_word:
    print("Invaild input. The sum of letters, numbers, and symbols doesn't match the password length! ")
else:
    select_litters = (string.ascii_letters) 
    litters_choiced = random.choices(select_litters, k=length_of_litters)
    print(type(litters_choiced))
    
    
    select_numbers = (string.digits)
    numbers_choiced = random.choices(select_numbers, k=length_of_numbers)

    select_symbols = (string.punctuation)
    symbols_choiced = random.choices(select_symbols, k=length_of_symbols)

    
    big_list = [litters_choiced, numbers_choiced, symbols_choiced]
    flat_list = []
    for sublist in big_list:
        for char in sublist:
            flat_list.append(char)
    
    random.shuffle(flat_list)
    jlist= ("".join(flat_list))

    print(f"Generator Password: {jlist}")

    
   


    
    

    
    
    




