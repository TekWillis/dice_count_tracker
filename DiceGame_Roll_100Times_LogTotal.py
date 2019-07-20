# this program will roll two die and then add them together and keep track of the how frequent the total number comes up.


import random

c1 = int(0)
c2 = int(0)
c3 = int(0)
c4 = int(0)
c5 = int(0)
c6 = int(0)
c7 = int(0)
c8 = int(0)
c9 = int(0)
c10 = int(0)
c11 = int(0)
c12 = int(0)

# sets the roll count base...starting from zero
roll = int(0)

# sets dice integer range
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)


# while statement to have python automatically roll the die, and append the results
while roll <= 1001:
    print("ROLL",roll)
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print("die 1 =", die1)
    print("die 2 =", die2)
    roll += 1
    if die1 + die2 == 2:
        c2 += 1
    if die1 + die2 == 3:
        c3 += 1
    if die1 + die2 == 4:
        c4 += 1
    if die1 + die2 == 5:
        c5 += 1
    if die1 + die2 == 6:
        c6 += 1
    if die1 + die2 == 7:
        c7 += 1
    if die1 + die2 == 8:
        c8 += 1
    if die1 + die2 == 9:
        c9 += 1
    if die1 + die2 == 10:
        c10 += 1
    if die1 + die2 == 11:
        c11 += 1
    if die1 + die2 == 12:
        c12 += 1
    else:
        print("no total")

#print("The total number of two's ", c1)  # this is impossible to roll two die and get a value of one
print("The total number of Two's", c2)
print("The total number of Threes's ", c3)
print("The total number of Fours's ", c4)
print("The total number of Five's ", c5)
print("The total number of Six's ", c6)
print("The total number of Seven's ", c7)
print("The total number of Eight's ", c8)
print("The total number of Nine's ", c9)
print("The total number of Ten's ", c10)
print("The total number of Eleven's ", c11)
print("The total number of Twelve's ", c12)