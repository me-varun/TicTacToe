a = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
done = []  # list that stores each step so that there is no repetition
sy = 'O'  # It store The current symbol( X or O)
turns = 0


# Function that display the updated status of the game

def display():
    print(' ', a[0][0], ' | ', a[0][1], ' | ', a[0][2])
    print('-----------------')
    print(' ', a[1][0], ' | ', a[1][1], ' | ', a[1][2])
    print('-----------------')
    print(' ', a[2][0], ' | ', a[2][1], ' | ', a[2][2])


# Function just changes the symbol for next turn

def changeturn():
    global sy
    if sy == 'X':
        sy = 'O'
    else:
        sy = 'X'


# This function checks if someone has win or not

def check():
    for i in range(3):
        if (a[i][0] == 'X' and a[i][1] == 'X' and a[i][2] == 'X'):
            display()
            print('X Wins')
            return True
    for i in range(3):
        if (a[0][i] == 'X' and a[1][i] == 'X' and a[2][i] == 'X'):
            display()
            print('X Wins')
            return True
    for i in range(3):
        if (a[i][0] == 'O' and a[i][1] == 'O' and a[i][2] == 'O'):
            display()
            print('O Wins')
            return True

    for i in range(3):
        if (a[0][i] == 'O' and a[1][i] == 'O' and a[2][i] == 'O'):
            display()
            print('O Wins')
            return True

    if (a[0][0] == 'X' and a[1][1] == 'X' and a[2][2] == 'X'):
        display()
        print(' X Wins')
        return True

    if (a[0][0] == 'O' and a[1][1] == 'O' and a[2][2] == 'O'):
        display()
        print(' O Wins')
        return True

    if (a[0][2] == 'X' and a[1][1] == 'X' and a[2][0] == 'X'):
        display()
        print(' X Wins')
        return True

    if (a[0][2] == 'O' and a[1][1] == 'O' and a[2][0] == 'O'):
        display()
        print(' O Wins')
        return True

    return False


# This function takes the user input and first check if there is any repetion or not
# If there is no repetion then it assignt he value to the matrix

def assign(n, sy):
    global turns
    for i in range(len(done)):
        if done[i] == n:
            print('Try again!')
            if sy == 'X':
                sy = 'O'
            else:
                sy = 'X'
            return sy

    done.append(n)
    turns += 1

    if n == 1:
        a[0][0] = sy
    elif n == 2:
        a[0][1] = sy
    elif n == 3:
        a[0][2] = sy
    elif n == 4:
        a[1][0] = sy
    elif n == 5:
        a[1][1] = sy
    elif n == 6:
        a[1][2] = sy
    elif n == 7:
        a[2][0] = sy
    elif n == 8:
        a[2][1] = sy
    elif n == 9:
        a[2][2] = sy

    return sy


# Main Function Where all The other functions are called

def main():
    global sy
    chance = False
    sy = 'O'
    while not chance:
        display()
        changeturn()

        print('Enter The Box number where You Have to insert(1-9)', sy)
        box = eval(input())
        if box < 10 and box > 0:
            sy = assign(box, sy)
        else:
            changeturn()
            continue
        chance = check()
        if turns > 9:
            print("It's a Draw")
            exit(0)


# Our only one command for python :)
main()
