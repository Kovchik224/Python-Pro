import pyautogui
import keyboard
import time
#if keyboard.is_pressed('d'):
#        if play[]
#🡨🡫🡩🡪
#🡸🡻🡹🡺
i = 1
j = 1
flag = 0
what = 0
score = 0
hp = 0
accuraty = 0
pausetime = 0
game = 0
bpm = int(input('Введите BPM: '))
def miss():
    global score
    global hp
    score-=100
    hp-=5
    return('Miss')
def reaction():
    global score
    global hp
    accuraty = 0
    if hp != 100:
        hp+=5
        
    if speed < (bpm * 0.25) and speed > 0:
        score+=100
        return 'Идеально!'
    if speed < (bpm * 0.5) and speed > (bpm * 0.25):
        score+=75
        return 'Хорошо!'
    if speed < (bpm * 0.75) and speed > (bpm * 0.5):
        score+=50
        return 'Плохо!'
    if speed < bpm and speed > (bpm * 0.75):
        score+=25
        return 'Ужасно!'
dadbattle = [['🡨', '🡫', '🡩', '🡪'],
             [' ', ' ', '🡹', ' '],
             [' ', ' ', ' ', ' '],
             ['🡸', ' ', ' ', ' '],
             [' ', '🡻', ' ', ' '],
             [' ', ' ', '🡹', ' '],
             [' ', ' ', ' ', ' '],
             [' ', '🡻', ' ', ' '],
             [' ', ' ', '🡹', ' '],
             [' ', ' ', ' ', '🡺'],
             ['🡸', ' ', ' ', ' '],
             [' ', ' ', ' ', '🡺'],
             [' ', '🡻', ' ', ' '],
             [' ', ' ', ' ', '🡺'],
             [' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' '],
             ['⚐', '⚐', '⚐', '⚐']]

megalovania = [['🡨', '🡫', '🡩', '🡪'],
               [' ', '🡻', ' ', ' '],
               [' ', '🡻', ' ', ' '],
               [' ', ' ', '🡹', ' '],
               [' ', ' ', ' ', ' '],
               ['🡸', ' ', ' ', ' '],
               [' ', ' ', ' ', ' '],
               [' ', ' ', '🡹', ' '],
               [' ', ' ', ' ', ' '],
               [' ', ' ', ' ', '🡺'],
               [' ', ' ', ' ', ' '],
               [' ', '🡻', ' ', ' '],
               [' ', ' ', ' ', ' '],
               ['🡸', ' ', ' ', ' '],
               [' ', ' ', '🡹', ' '],
               [' ', ' ', ' ', '🡺'],
               [' ', ' ', ' ', ' '],
               ['🡸', ' ', ' ', ' '],
               ['🡸', ' ', ' ', ' '],
               [' ', ' ', ' ', '🡺'],
               [' ', ' ', ' ', ' '],
               [' ', '🡻', ' ', ' '],
               [' ', ' ', ' ', ' '],
               [' ', ' ', ' ', '🡺'],
               [' ', ' ', ' ', ' '],
               [' ', ' ', ' ', '🡺'],
               [' ', ' ', ' ', ' '],
               [' ', '🡻', ' ', ' '],
               [' ', ' ', ' ', ' '],
               ['🡸', ' ', ' ', ' '],
               [' ', ' ', '🡹', ' '],
               [' ', ' ', ' ', '🡺'],
               [' ', ' ', ' ', ' '],
               ['🡨', '🡫', '🡩', '🡪'],
               [' ', '🡻', ' ', ' '],
               [' ', '🡻', ' ', ' '],
               [' ', ' ', '🡹', ' '],
               [' ', ' ', ' ', ' '],
               ['🡸', ' ', ' ', ' '],
               [' ', ' ', ' ', ' '],
               [' ', ' ', '🡹', ' '],
               [' ', ' ', ' ', ' '],
               [' ', ' ', ' ', '🡺'],
               [' ', ' ', ' ', ' '],
               [' ', '🡻', ' ', ' '],
               [' ', ' ', ' ', ' '],
               ['🡸', ' ', ' ', ' '],
               [' ', ' ', '🡹', ' '],
               [' ', ' ', ' ', '🡺'],
               [' ', ' ', ' ', ' '],
               ['🡸', ' ', ' ', ' '],
               ['🡸', ' ', ' ', ' '],
               [' ', ' ', ' ', '🡺'],
               [' ', ' ', ' ', ' '],
               [' ', '🡻', ' ', ' '],
               [' ', ' ', ' ', ' '],
               [' ', ' ', ' ', '🡺'],
               [' ', ' ', ' ', ' '],
               [' ', ' ', ' ', '🡺'],
               [' ', ' ', ' ', ' '],
               [' ', '🡻', ' ', ' '],
               [' ', ' ', ' ', ' '],
               ['🡸', ' ', ' ', ' '],
               [' ', ' ', '🡹', ' '],
               [' ', ' ', ' ', '🡺'],
               ['⚐', '⚐', '⚐', '⚐']]


play = []
while True:
    play = dadbattle
    for i in range(6):
        for j in range(len(play[i])):
            print(play[i][j], end=' ')
        print()
    time.sleep(0.5)
    #maxhp = 100, minhp = 0
    hp = 50
    score = 0
    accuraty = 0
    while game == 0:
        flag = 0
        speed = 0
        pausetime = 0
        print('score:', score)
        print('HP:', hp)
        for i in range (bpm):
            speed+=1
            if flag == 0:
                if keyboard.is_pressed('d'):
                    if play[0][0] == '🡨':
                        print(miss())
                    if play[0][0] == '🡸':
                        print(reaction())
                    flag = 1
            
                if keyboard.is_pressed('f'):
                    if play[0][1] == '🡫':
                        print(miss())
                    if play[0][1] == '🡻':
                        print(reaction())
                    flag = 1
            
                if keyboard.is_pressed('j'):
                    if play[0][2] == '🡩':
                        print(miss())
                    if play[0][2] == '🡹':
                        print(reaction())
                    flag = 1
                
                if keyboard.is_pressed('k'):
                    if play[0][3] == '🡪':
                        print(miss())
                    if play[0][3] == '🡺':
                        print(reaction())
                    flag = 1
            
                if keyboard.is_pressed('enter'):
                    if hp > 0:
                        print('Pause')
                        time.sleep(0.5)
                        while pausetime == 0:
                            if keyboard.is_pressed('enter'):
                                pausetime = 1
                                time.sleep(0.5)
                                print('3')
                                time.sleep(0.5)
                                print('2')
                                time.sleep(0.5)
                                print('1')
                                time.sleep(0.5)
                                print('GO!')
                                time.sleep(0.5)

            time.sleep(0.01)
            
        what = 0
        if play[0][0] == '🡸' or play[0][1] == '🡻' or play[0][2] == '🡹' or play[0][3] == '🡺':
            play[0] = ['🡨','🡫','🡩','🡪']
        for i in range(len(play)-1):
            for j in range(0,4):
                #No Arrow
                if what == 0:
                    if play[i] == [' ',' ',' ',' '] and play[i-1] == ['🡨','🡫','🡩','🡪']:
                        play.pop(1)
                        play.append([' ',' ',' ',' '])
                        what = 1
                    
                #Left
                if what == 0:
                    if play[i][j] == '🡸' and play[i-1] == ['🡨','🡫','🡩','🡪']:
                        play[i-1][j] = '🡸'
                        play.pop(1)
                        play.append([' ',' ',' ',' '])
                        what = 1
            
                #Down
                if what == 0:
                    if play[i][j] == '🡻' and play[i-1] == ['🡨','🡫','🡩','🡪']:
                        play[i-1][j] = '🡻'
                        play.pop(1)
                        play.append([' ',' ',' ',' '])
                        what = 1
                    
                #Up
                if what == 0:
                    if play[i][j] == '🡹' and play[i-1] == ['🡨','🡫','🡩','🡪']:
                        play[i-1][j] = '🡹'
                        play.pop(1)
                        play.append([' ',' ',' ',' '])
                        what = 1
                    
                #Right
                if what == 0:
                    if play[i][j] == '🡺' and play[i-1] == ['🡨','🡫','🡩','🡪']:
                        play[i-1][j] = '🡺'
                        play.pop(1)
                        play.append([' ',' ',' ',' '])
                        what = 1
                    
                #Finish
                if play[1] == ['⚐','⚐','⚐','⚐']:
                    print('GAME OVER')
                    time.sleep(1)
                
        for i in range(6):
            for j in range(len(play[i])):
                print(play[i][j], end=' ')
            print()
            
        if hp <= 0:
            game = 1
    
    if hp <= 0:
        print('Game Over')
        time.sleep(1)
        print('Restart?')
        while game == 1:
            if keyboard.is_pressed('enter'):
                game = 0
                hp = 50
                time.sleep(1)
        
