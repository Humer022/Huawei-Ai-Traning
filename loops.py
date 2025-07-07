#python iteration
'''n = 5
while n > 0:
    print(n)
    n = n - 1
print('blastoff')
print(n)'''

'''n = 5
while n > 0: #condition always true

    print('Lather')
    print('Rinse')
print('Dry off!')'''

'''n = 0
while n > 0 : # condition always false

    print('Lather')
    print('Rinse')
print('Dry off!')'''

'''while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')'''

'''while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
print(line)
print('Done!')'''

#Definate loop
'''for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')'''

#Definate loop with string
'''friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:', friend)
print('Done!')'''

'''print('Before')
for thing in [9, 41, 12, 3, 74, 15] :
    print(thing)
print('After')'''

#Find largest number
'''numbers = [3 , 41 ,12 , 9, 74, 15]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
print("The largest number is",largest)'''

#Find smallest number
'''numbers = [3 , 41 ,12 , 9, 74, 15]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num
print("The smallest number is",smallest)'''

'''zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1
    print(zork, thing)
print('After', zork)'''


'''zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
    print(zork, thing)
print('After', zork)'''


#Find average number 
'''count = 0
sum = 0

numbers = [3 , 41 ,12 , 9, 74, 15]
for num in numbers:
    count = count + 1
    sum = sum + num
    
print("The average number is",sum /count)'''

'''print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if value > 20:
        print('Large number',value)
print('After')'''

found = False
print('Before', found)
for value in [9, 41, 12, 3, 74, 15] :
    if value == 3 :
        found = True
    print(found, value)
print('After', found)


'''smallest = None
print('Before')
for value in [3, 41, 12, 9, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)'''