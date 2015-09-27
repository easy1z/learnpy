from random import choice

score=[0,0]
direction=['left','center','right']

def kick():
    print'======YOU KICK====='
    print'CHOOSE ONE SIDE TO SHOOT'
    you=raw_input()
    print'YOU KICKED'+you
    com=choice(direction)
    print'COMPUTER SAVED'+com
    if you!=com:
        print'GOAL'
        score[0]+=1
    else:
        print'OPPS'
    print'SCORE:%d(YOU)--%d(COMPUTER)'%(score[0],score[1])


    print'======COMPUTER KICK====='
    print'CHOOSE A SDIE TO SAVE'
    you=raw_input()
    print'YOU SAVED'+you
    com=choice(direction)
    print'COMPUTER KICKD'+com
    if you!=com:
        print'YOU MISSED'
        score[1]+=1
    else:
        print'NICE!!!'
    print'SCORE:%d(YOU)--%d(COMPUTER)'%(score[0],score[1])

for i in range(5):
    print'=====ROUND %d======'%(i+1)
    kick()



if score[0]>score[1]:
    print'YOU WIN'
else:
    print'YOU Lose'

