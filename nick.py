import random
print("Hello, i can help you to create a nickname!")
nol = int(input("How many letters do you want in your nickname ?"))
alphabet = []
vovels = []
consonants = []
rndm_list = [0,1]
nickname_list = []
nickname = ""
v = set("aeiouy")
alpha = 'a'
for i in range(0, 26): 
    alphabet.append(alpha) 
    alpha = chr(ord(alpha) + 1) 
for i in alphabet:
    if i in v:
        vovels.append(i)
    else:
        consonants.append(i)
x = nol
f_l = int(input("How do you want your nickname to start? \n1: vovel \n2 : consonant"))
if f_l == 1 :
    while x > 0:
        nickname += str(random.choice(vovels))
        x -= 1
        nickname += str(random.choice(consonants))
        x -= 1
elif f_l == 2:
    while x > 0:
            nickname += str(random.choice(consonants))
            x -= 1
            nickname += str(random.choice(vovels))
            x -= 1
else:
    print("invalid answer")

extra_letter = nickname[len(nickname)-1]
if len(nickname) != nol:
    nickname = nickname.replace(str(extra_letter), "")
print("Your new nickname can be: ",nickname)