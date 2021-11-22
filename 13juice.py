import random
import numpy as np

def check(card, card_type):
    pair = [i%10 for i in card]
    color = [i//10 for i in card]
    
    flag = 0
    # 對子、三條
    for element in pair:
        if pair.count(element) == 2:
            card_type[0] += 1
            break
        elif pair.count(element) == 3:
            card_type[1] += 1
            break
    
    # 同花
    for element in color:
        if color.count(element) == 3:
            card_type[2] += 1
            break
            
    # 小順
    for i in range(3):
        if ((pair[i]+1) == pair[i+1]) and ((pair[i+1]+1) == pair[i+2]):
            card_type[3] += 1
            
            # 同花小順
            if card_type[2] == 1 :
                card_type[4] += 1
    # 烏龍
    if sum(card_type) == 0 :
        card_type[5] += 1
def out(array):
    if array[5]:
        print("烏龍 ", end="")
    if array[0]:
        print("對子 ", end="")
    if array[1]:
        print("三條 ", end="")
    if array[2]:
        print("同花", end="")
    if array[3]:
        print("小順 ", end=" ")
    if array[4]:
        print("同花小順 ", end=" ")
def PrintResult(result, LEN):
    print("遊戲進行 " + str(LEN) + " 次\n")
    print("烏龍機率：" + str(round(100*(result[5]/LEN), 2)) + "%")
    print("對子機率：" + str(round(100*(result[0]/LEN), 2)) + "%")
    print("三條機率：" + str(round(100*(result[1]/LEN), 2)) + "%")
    print("同花機率：" + str(round(100*(result[2]/LEN), 2)) + "%")
    print("小順機率：" + str(round(100*(result[3]/LEN), 2)) + "%")
    print("同花小順機率：" + str(round(100*(result[4]/LEN), 2)) + "%")
    print()
def BettingOdds(result, LEN):
    print("-----------------------------------------")
    print("建議賠率算法 0.9 * (進行次數 / 牌型出現機率)")
    print("-----------------------------------------")
    print("烏龍賠率：" + str(round(0.9*LEN/result[5], 2)))
    print("對子賠率：" + str(round(0.9*LEN/result[0], 2)))
    print("三條賠率：" + str(round(0.9*LEN/result[1], 2)))
    print("同花賠率：" + str(round(0.9*LEN/result[2], 2)))
    print("小順賠率：" + str(round(0.9*LEN/result[3], 2)))
    print("同花小順賠率：" + str(round(0.9*LEN/result[4], 2)))
    print()

LEN = 10000
result = np.array([0 for i in range(6)])
for time in range(LEN):
    total = 40
    player_number = 8
    card = [i for i in range(1, total+1)]
    card = random.sample(card, total)
    players = []

    for i in range(0, total, 5): # 1人5張牌
        players.append(card[i:i+5])
        players[-1].sort()

    for player in players:
        card_type = [0 for i in range(6)] # 六種牌型：對子、三條、同花、小順、同花小順、烏龍
        check(player, card_type)
    result += np.array(card_type)

PrintResult(result, LEN)
BettingOdds(result, LEN)
