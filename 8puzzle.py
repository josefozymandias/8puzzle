import random

print
print "Use move the blank space"
print "until the grid looks like this."
print "+-----------+"
print "| 1 | 2 | 3 |"
print "+---+---+---+"
print "| 4 | 5 | 6 |"
print "+---+---+---+"
print "| 7 | 8 |   |"
print "+-----------+"
print
print "Use wasd to move and q to quit."
print

numbers = ['1','2','3','4','5','6','7','8',' ']
correct = ['1','2','3','4','5','6','7','8',' ']
random.shuffle(numbers)

def draw_grid():
    global numbers
    n = numbers
    print "+-----------+"
    print "| %s | %s | %s |" % (n[0],n[1],n[2])
    print "+---+---+---+"
    print "| %s | %s | %s |" % (n[3],n[4],n[5])
    print "+---+---+---+"
    print "| %s | %s | %s |" % (n[6],n[7],n[8])
    print "+-----------+"

def move_up():
    indx = numbers.index(' ')
    if indx - 3 >= 0:
        num = numbers[indx-3]
        numbers[indx] = num
        numbers[indx-3] = ' '

def move_down():
    indx = numbers.index(' ')
    if indx + 3 <= 8:
        num = numbers[indx+3]
        numbers[indx] = num
        numbers[indx+3] = ' '

def move_right():
    indx = numbers.index(' ')
    if indx != 0 and indx != 3 and indx != 6:
        num = numbers[indx-1]
        numbers[indx] = num
        numbers[indx-1] = ' '

def move_left():
    indx = numbers.index(' ')
    if indx != 2 and indx != 5 and indx != 8:
        num = numbers[indx+1]
        numbers[indx] = num
        numbers[indx+1] = ' '

while True:
    draw_grid()

    print "> ",
    i = raw_input()
    if i == 'w':
        move_up()
    if i == 's':
        move_down()
    if i == 'a':
        move_right()
    if i == 'd':
        move_left()
    if i == 'q':
        break

    if numbers == correct:
        draw_grid()
        print "Congratulations!!!"
        break
