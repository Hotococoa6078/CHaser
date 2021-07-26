import CHaser
import random
wayList = ['up','left','down','right']
wayListNum = {'up': '0 1 2', 'left': '0 3 6', 'down': '6 7 8','right': '2 5 8'}

firstmove = False

movemain = {'up' : 'client.walk_up()', 'down' : 'client.walk_down()', 'left' : 'client.walk_left()', 'right' : 'client.walk_right()', 'None' : 'pass'}
moveList = [[['up', 'left'],['left','up']],['up'],[['up', 'right'],['right','up']],['left'],['right'],[['down', 'left'],['left','down']],['down'],[['down', 'right'],['right','down']]]
def main():
    value = []
    client = CHaser.Client()
    firstway = random.choice(wayList)
    while(True):
        value = client.get_ready() #ex : [2, 0, 0, 0, 0, 0, 0, 0, 2], chaserEx.png
        if firstmove == False:
            if 1 in [value[1], value[3], value[5], value[7]]: #상대 확인
                Evalue = [value[1], value[3], value[5], value[7]]
                enemy = Evalue.index(1)
                if enemy == 0:#상단
                    value = client.put_up()
                    lastmove = 'None'
                    firstmove = True
                elif enemy == 1:#좌측
                    value = client.put_left()
                    lastmove = 'None'
                    firstmove = True
                elif enemy == 2:#우측
                    value = client.put_right()
                    lastmove = 'None'
                    firstmove = True
                elif enemy == 3:#하단
                    value = client.put_down()
                    lastmove = 'None'
                    firstmove = True
                else:
                    print('error')
                    #exit()
            elif 1 in [value[0],value[2],value[6],value[8]]:#각 모서리에 적이 있으면 -> 옆보고 continue하고 위로
                value = client.look_left()
                firstmove = True
                continue
            else:
                for i in range(4):
                    for e in range(3):
                        WNum = [wayListNum[firstway].split(' ')]
                        if value[WNum[e]] in 0:
                            firstway = random.choice(wayList)
        else:
            pass


if __name__ == "__main__":
    main()