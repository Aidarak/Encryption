# encryption.py
# ARYAN KARADIA, ENDG 233 F21
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# You may optionally import the string module from the standard Python library. No other modules may be imported.
# Remember to include docstrings for your functions and comments throughout your code.



### Define your functions here

import string
alphabet = string.ascii_lowercase
alpha_list = list(alphabet) #lower case alphabet turned into a list

def cipher_dict(user_cipher, alphabet_list): 
    ''' Function to create cipher dictionary. 
           
            Arguments: user cipher, alphabet list

            Return: cipher dictionary '''
    
    pair_text_cipher = zip(alphabet_list, user_cipher) #assigns user cipher with corresponding letter
    cipher_dict = dict(pair_text_cipher)
    return cipher_dict

def encode_txt(usr_cipher_dict, text_to_encode):
    ''' Function to encode user text
    
        Arguments: encoded dictionary, text to encode
        
        Return: encoded text '''
    
    encoded_text = ''
    i = 0
    while i < len(text_to_encode): 
        ''' For every letter in input, checks if letter is in cipher dictionary.
            If true, adds the correspoding encoded value to output '''
        
        if text_to_encode[i] in usr_cipher_dict.keys():
            encoded_text += usr_cipher_dict[text_to_encode[i]]
            i += 1
    return encoded_text

def decode_txt(text_to_decode, usr_cipher_dict):
    ''' Function to decode user text
    
        Arguments: text to decode, encoded dictionary
        
        Return: decoded text '''
    
    decoded_text = []

    ''' Splits up user cipher dictionary into alphabet list and user cipher list '''
    alphabet = list(usr_cipher_dict.keys()) 
    cipher = list(usr_cipher_dict.values())

    i = 0
    while i < len(text_to_decode): 
        ''' For every letter in input, checks the letters index, goes to the alphabet and find value at that index.
            Adds the value to decoded text '''
        
        position = cipher.index(text_to_decode[i])
        key = alphabet[position]
        decoded_text.append(key)
        i += 1

    return ''.join(decoded_text)

#Nice
### Add your main program code here

print("ENDG 233 Encryption Program")

user_choice = int(input('Select 1 to encode or 2 to decode your message, select 0 to quit: ')) 

'''Prompts user to choose an action and based on that choice either encodes or decodes messages'''

while user_choice != 0:
    if user_choice == 1:
        ''' User wants to encode text, provides text needed to be encoded and cipher to encode with'''

        text_to_encode = str(input('Please enter the text to be encoded: '))
        user_cipher = list(input('Please enter the cipher: '))
        
        '''Tests if user cipher is valid. If not valid, asks the user to input a valid cipher'''

        while len(set(user_cipher)) != 26: 
            print('Your cipher must contain 26 unique elements of a-z or 0-9.')
            user_cipher = list(input('Please enter the cipher text: '))
        else:
            print('Your cipher is valid.')
        
        '''creates encoded dictionary, then uses that dictionary to encode the text given. 
                
            Prints decoded text as output and prompts user for next choice'''

        usr_cipher_dict = cipher_dict(user_cipher, alpha_list)
        encoded_txt = encode_txt(usr_cipher_dict, text_to_encode)
        print('Your output is: {}' .format(encoded_txt))
        user_choice = int(input('Select 1 to encode or 2 to decode your message, select 0 to quit: ')) 


    elif user_choice == 2:
        ''' User wants to decode text provided the cipher the text was encoded with'''

        txt_to_decode = str(input('Please enter the text to be decoded: '))
        user_cipher = list(input('Please enter the cipher: '))

        '''Tests if user cipher is valid. If not valid, asks the user to input a valid cipher'''

        while len(set(user_cipher)) != 26: 
            print('Your cipher must contain 26 unique elements of a-z or 0-9.')
            user_cipher = list(input('Please enter the cipher text: '))
        else:
            print('Your cipher is valid.')
        
        '''Creates cipher dictionary and decodes provided text. 
            
            Prints decoded text as output and prompts user for next choice'''

        usr_cipher_dict = cipher_dict(user_cipher, alpha_list)
        decoded_text = decode_txt(list(txt_to_decode), usr_cipher_dict)
        print('Your output is: {}' .format(decoded_text))
        user_choice = int(input('Select 1 to encode or 2 to decode your message, select 0 to quit: ')) 


    else:
        print('Invalid Entry')
        break

print('Thank you for using the encryption program.')