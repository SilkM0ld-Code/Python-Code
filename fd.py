import random
with open('Words.txt', 'r') as file:
    a = file.readlines()

while True:
    t =random.choice(a)
    print(t)

