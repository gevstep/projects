class Crypto:
    def __init__(self, number, user_input_text, text):
        self.number = number
        self.user_input_text = user_input_text
        self.text = text

    def cryptograph(self):
        crypted_text = []
        text_for_print = ""
        lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
        for j in text_list:
            index_for_crypt = lowercase.index(j) + number
            crypted_text.append(lowercase[index_for_crypt])

        print(user_input_text)
        print(text_for_print.join(crypted_text))

def user_input():
    global number, text_list, user_input_text
    text_list = []
    number = int(input("Enter a number for cryptography: "))
    user_input_text = input("Enter a text: ")
    text = user_input_text.lower()
    for i in text:
        text_list.append(i)
    #print(text_list)



Crypto.cryptograph(user_input())
