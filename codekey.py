import random

str_1 = "r|!bU<0idFlZc4V67#vgtwx^O3eS%:$z XPjJ/R,_knNpD-TK*>AhqC~8osa1Em?9YQfM&IyW@GL=`BH;.25u+"
str_2 = "wEApvozQ>8dr3`.%;j?MFOS/i7bNl&e,Cm~4D!9^n5K|YJ0X_qPT@G$HtVkIWB<2xL1fcR+Z#:hy=U*-gs ua6"
salt = "HomeImprovement"

def check_access(password):
    key_pass = "dankmemes"
    if password == key_pass:
        return True
    else:
        return False

def encrypt_password(password):
    encrypted_phrase = ""
    if len(password) < 15:      
        password = password + salt
    for letter in password:
        index = str_1.index(letter)
        encrypted_letter = str_2[index]
        encrypted_phrase = encrypted_phrase + encrypted_letter
    return(encrypted_phrase)

def unencrypt_password(clearance, encrypted_word):
    if clearance == True:
        encrypted_phrase = ""
        for letter in encrypted_word:
            index = str_2.index(letter)
            encrypted_letter = str_1[index]
            encrypted_phrase = encrypted_phrase + encrypted_letter
        return(encrypted_phrase)
    else:
        return("I don't think so, Tim")

