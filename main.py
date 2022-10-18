import random
list_of_char = ['a','b','c','d','e','f','g'] 
y = random.choice(list_of_char)
print('Try to guess the correct char "---- a, b, c, d, e, f, g ----" ')
print('\t--- To exit the game wirte exit ---')
#y = 'd'
x = input()
n = 0
while True:
    if x == y:
        print('You won! after ' + str(n) + ' trail')
        break
    elif x == 'exit':
        exit()
    else:
        n = n + 1
        print("try again you tried " + str(n) + " times")
        x = input()
        
