import time, random
games = 1
print('Game 1:')
while True:
    rolls = 0
    tobeplayer = []
    tine = 0
    int(tine)
    por = input('porr/> ')
    if por.lower() == 'r':
        tobeplayer = []
        for counter in range(0, 10):
            newnum = input('player1/> ')
            tobeplayer.append(newnum)
            tobeplayer.sort()
        tobeai = []
        for counter in range(0, 10):
            newnum = random.randint(2, 11)
            tobeai.append(newnum)
        tobeai.sort()
        tobeplayer = [int(i) for i in tobeplayer]
        tine = tine + 1
        while tobeplayer or tobeai != []:
           rolls = rolls + 1
           firstdice = random.randint(2, 11)
           ftf = firstdice in tobeplayer
           if ftf == True:
                tobeplayer.remove(firstdice)
                tobeplayer.sort()
                print('-------------')
                print('PlayerSet:',tobeplayer)
                print('AI SET:',tobeai)
                print('Roll:',firstdice)
           else:
               print('-------------')
               print('PlayerSet:',tobeplayer)
               print('AI SET:',tobeai)
               print('Roll:',firstdice)
           firstdice = random.randint(2, 11)
           ftf = firstdice in tobeai
           if ftf == True:
                tobeai.remove(firstdice)
                tobeai.sort()
                print('-------------')
                print('PlayerSet:',tobeplayer)
                print('AI SET:',tobeai)
                print('Roll:',firstdice)
           else:
               tobeplayer
               print('-------------')
               print('PlayerSet:',tobeplayer)
               print('AI SET:',tobeai)
               print('Roll:',firstdice)
           if tobeai == []:
               print('YOU WIN')
               print('Total Rolls:',rolls)
               print()
               print('---------------')
               print()
               games = games + 1
               print('Game:',games)
               break
           elif tobeplayer == []:
               print('YOU LOSE')
               print('Total Rolls:',rolls)
               print()
               print('---------------')
               games = games + 1
               print()
               print('Game:',games)
               break

    if por.lower() == 'p':
        tobeplayer = []
        for counter in range(0, 10):
            newnum = input('player1/> ')
            tobeplayer.append(newnum)
        tobeplayer.sort()
        tobeai = []
        for counter in range(0, 10):
            newnum2 = input('player2/> ')
            tobeai.append(newnum2)
        tobeai.sort()
        tobeplayer = [int(i) for i in tobeplayer]
        tobeai = [int(i) for i in tobeai]
        while tobeplayer or tobeai != []:
            rolls = rolls + 1
            firstdice = random.randint(2, 11)
            ftf = firstdice in tobeplayer
            if ftf == True:
                tobeplayer.remove(firstdice)
                tobeplayer.sort()
                print('-------------')
                print('Player 1 Set:',tobeplayer)
                print('Player 2 Set:',tobeai)
                print('Roll:',firstdice)
            else:
                print('-------------')
                print('Player 1 Set:',tobeplayer)
                print('Player 2 Set:',tobeai)
                print('Roll:',firstdice)
            firstdice = random.randint(2, 11)
            ftf = firstdice in tobeai
            if ftf == True:
                tobeai.remove(firstdice)
                tobeai.sort()
                print('-------------')
                print('Player 1 Set:',tobeplayer)
                print('Player 2 Set:',tobeai)
                print('Roll:',firstdice)
            else:
               tobeplayer
               print('-------------')
               print('Player 1 Set:',tobeplayer)
               print('Player 2 Set:',tobeai)
               print('Roll:',firstdice)
            if tobeai == []:
                print('Player 1 Wins')
                print('Total Rolls:',rolls)
                print()
                print('---------------')
                print()
                games = games + 1
                print('Game:',games)
                break
            elif tobeplayer == []:
                print('Player 2 Wins')
                print('Total Rolls:',rolls)
                print()
                print('---------------')
                print()
                games = games + 1
                print('Game:',games)
                break
        else:
            print("Error 5: not 'p' or 'r'.")
