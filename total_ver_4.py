import copy
import random
import time
import keyboard


# 몬스터 함수
def monster():
    spawn = random.randint(1, 100)

    if 1 <= spawn < 49:
        name = "좀비"
        attack = 100
        hp = random.randint(300, 500)
    elif 49 <= spawn < 79:
        name = "구울"
        attack = 180
        hp = random.randint(450, 700)
    elif 79 <= spawn < 91:
        name = "해골"
        attack = 220
        hp = random.randint(480, 800)
    elif 91 <= spawn < 96:
        name = "버그베어"
        attack = 350
        hp = random.randint(550, 900)
    elif 96 <= spawn < 98:
        name = "동혀니"
        attack = random.randint(1000, 3000)
        hp = random.randint(3000, 8000)
    elif 98 <= spawn < 100:
        name = "홍거리"
        attack = random.randint(1000, 3000)
        hp = random.randint(3000, 8000)
    else:
        name = "디아복로"
        attack = random.randint(2500, 8000)
        hp = random.randint(5000, 15000)
    print(f'{name} 등장!!')   # 추가된 프린트
    return name, hp, attack


# 포탈 좌표 생성 함수
def portal_coord(xy: list, cha: list):
    while True:
        po_coo = list()
        po_coo.append(random.randint(0, xy[0]-1))
        po_coo.append(random.randint(0, xy[1]-1))
        if po_coo[0] == cha[0] and po_coo[1] == cha[1]:
            continue
        else:
            break
    return po_coo


# 맵 생성 함수
def map_creation(cha: list, por: list, xy: list):
    map1 = []
    for i in range(xy[0]):
        list1 = []
        for j in range(xy[1]):
            ran = random.randint(1, 100)
            if ran < 51:
                ran = 0
            elif 50 < ran < 81:
                ran = 1
            else:
                ran = 2
            list1.append(ran)
        map1.append(list1)
    map1[cha[0]][cha[1]] = '*'
    if por[0] == 0 and por[1] == 0:
        pass
    else:
        map1[por[0]][por[1]] = 3
    return map1


# 배열 출력 함수 + 시야(3*3) 적용
def vie(map_list: list):
    map1 = copy.deepcopy(map_list)
    idx = [0, 0]
    for i in range(0, len(map1)):
        for j in range(0, len(map1[i])):
            if map1[i][j] == '*':
                idx = [i, j]
    for i in range(0, len(map1)):
        for j in range(0, len(map1[i])):
            if not idx[0]-2 < i < idx[0]+2 or not idx[1]-2 < j < idx[1]+2:
                map1[i][j] = '$'
    for i in map1:
        for j in i:
            if j == '*':
                j = '🦸‍'
            elif j == 0:
                j = '🦊'
            elif j == 1:
                j = '🎁'
            elif j == 2:
                j = '🟫'
            elif j == 3:
                j = '🌌'
            elif j == '$':
                j = '⬛'
            print(j, end='')
        print()


# 초코의용군의 좌표이동
def move(position: list, map_list: list):
    y_len = len(map_list) - 1
    x_len = len(map_list[0]) - 1
    while 1:
        if keyboard.is_pressed(72):
            print("▲ 방향키 입력")
            time.sleep(0.2)
            if position[0] > 0:
                position[0] -= 1
            return position

        if keyboard.is_pressed(75):
            print("◀ 방향키 입력")
            time.sleep(0.2)
            if position[1] > 0:
                position[1] -= 1
            return position

        if keyboard.is_pressed(77):
            print("▶ 방향키 입력")
            time.sleep(0.2)
            if position[1] < x_len:
                position[1] += 1
            return position

        if keyboard.is_pressed(80):
            print('▼ 방향키 입력')
            time.sleep(0.2)
            if position[0] < y_len:
                position[0] += 1
            return position


# 초코의용군의 좌표이동에 의한 맵 변환및 이벤트
def move_event(map_list: list, position: list):
    x = map_list[position[0]][position[1]]
    for i in range(len(map_list)):
        for j in range(len(map_list[i])):
            if map_list[i][j] == '*':
                map_list[i][j] = 2
                map_list[position[0]][position[1]] = '*'
                return map_list, x


# 길에 떨어지 포션 줍는 함수
def potion():
    get_potion = random.randint(1, 2)
    if get_potion == 1:
        print("체력 포션을 주웠다!!")
        return 1
    else:
        print("포션을 줍지 못했다")
        return 0


# 용사 공격력 함수
def man(power):  # power : 추가공격력
    attack = random.randrange(100, 151)  # randrange(x,y): x<= result <y ,randint(x,y): x<= result <=y
    return round(attack+attack*power*0.05)


# 싸우고나서 포션 얻는 함수
def potion2():
    a = random.randrange(100)    # 0 ~ 99
    po1 = 0
    po2 = 0
    if a < 50:   # 0 ~ 49
        b = random.randrange(1000)   # 0 ~ 999
        if b < 955:  # 0 ~ 954
            print("체력 포션 획득!")
            po1 += 1
        else:    # 955 ~ 999
            print("엘릭서 획득!")
            po2 += 1
    else:    # 50 ~ 99
        print("포션을 얻지 못했다.")
    return po1, po2


# 엘릭서 사용 함수
def potion3(man_hp, man_max_hp, po1, po2):
    eli = 0
    print("1. 체력포션 2. 엘릭서 사용")
    print("사용 안하시려면 아무키")
    po = input()
    if po == '1':
        if po1 == 0:
            print("체력 포션이 없습니다.")
        else:
            print("체력포션 사용")
            man_hp = man_max_hp
            po1 -= 1
            print(f'의용이의 체력이{man_hp}이 되었습니다.')

    if po == '2':
        if po2 == 0:
            print("엘릭서가 없습니다.")
        else:
            print("엘릭서 사용")
            po2 -= 1
            eli = 10
    print("***********************************")
    return man_hp, po1, po2, eli


# 엘릭서 사용 했을 경우 10번 동안 몬스터 공격 0 만들어주는 함수
def elixir(eli, monster_attack):
    if eli != 0:
        print(f'{eli}번 동안 몬스터 공격 0')
        eli -= 1
        monster_attack = 0

    return eli, monster_attack


# 파이트 함수
def fight(man_hp, apower, apo1, apo2):
    monster_name, monster_hp, monster_attack = monster()    # monster 정보 받기 및 등장
    boss_name = 0
    # 매개변수를 변수에 저장 : 이유가 뭘까?
    power = apower
    po1 = apo1
    po2 = apo2
    eli = 0
    monster_attack_original = monster_attack

    while 1:
        run = input("1. 싸움 2. 도망 : ")
        while True:
            if run == "1":
                print("***********************************")
                print("*******싸움 시작!!  의용 등장!!*******")
                add_hp = 1.05 ** power
                man_max_hp = round(500 * add_hp)
                # 반올림 기능, round(number[,ndigitd]): ndigitd의 기본값=none, number 반올림 (단,숫자의 정수가 0 또는 짝수일 경우 반내림)

                while True:
                    print("***********************************")
                    print(f'*********체력포션:{po1} 엘릭서:{po2} ********')
                    print(f'************power : {power} ************')
                    print("***********************************")
                    man_attack = man(power)
                    boss_name = monster_name
                    print(f'     {monster_name} 체력:{monster_hp}, 공격력:{monster_attack}')
                    print(f'     의용 체력❤:{man_hp}/{man_max_hp}, 공격력:{man_attack}')
                    print("***********************************")

                    man_hp, po1, po2, choice = potion3(man_hp, man_max_hp, po1, po2)  # 포션 사용
                    eli += choice
                    eli, monster_attack = elixir(eli, monster_attack_original)

                    print(f'  의용 {man_attack} 공격력으로 {monster_name}를 공격.')
                    monster_hp -= man_attack
                    if monster_hp <= 0:  # 몬스터 1방 컷 전투 종료
                        print(f'  의용이가 이겼다.')
                        print(f'  의용이의 체력 : {man_hp}')
                        po11, po22 = potion2()                                          # 전투 후 포션 생성 함수
                        po1 += po11
                        po2 += po22
                        power += 1                                                      # 한턴 이기고 쌔지는거
                        return man_hp, power, po1, po2, boss_name                                          # 리턴
                    if monster_name == '동혀니' or monster_name == '홍거리' or monster_name == '디아복로':
                        boss = random.randrange(5)
                        # 보스몹일 경우 20%확률로 {monster_attack} 공격력으로 공격
                        if boss == 0:
                            print(f'  {monster_name}의 체력 : {monster_hp}')
                            print(f'  {monster_name} {monster_attack} 공격력으로 의용 공격.')
                            man_hp -= monster_attack
                        else:
                            print(f'{monster_name} 공격을 하지 않음')
                    else:
                        print(f'  {monster_name}의 체력 : {monster_hp}')
                        print(f'  {monster_name} {monster_attack } 공격력으로 의용 공격.')
                        man_hp -= monster_attack

                    print(f'  의용이의 체력 : {man_hp}')
                    print("***********************************")
                    if man_hp <= 0:
                        print(f'몬스터가 이겼다.')
                        print(f'!!게임 종료!!')
                        boss_name = 0
                        return man_hp, power, po1, po2, boss_name

            else:
                end = random.randint(0, 0)
                if end == 0:
                    print('실패')
                    run = "1"
                    continue
                else:
                    print('도망성공')
                    return man_hp, power, po1, po2, boss_name


def main():
    map_size = [15, 15]
    position = [0, 0]

    power = 0
    po1 = 2
    po2 = 0
    man_hp = 500
    h = 1
    map1 = []
    portal = portal_coord(map_size, position)
    print(f'{h}층 던전 진입')
    while True:
        if h != 3:
            map1 = map_creation(position, portal, map_size)
        else:
            h = 3
        for i in range(3):
            print('='*50)
            vie(map1)
            position = move(position, map1)
            map1, event = move_event(map1, position)

            if event == 0:
                man_hp, power, po1, po2, boss = fight(man_hp, power, po1, po2)
                if boss == '디아복로':
                    print('디아복로를 잡아 평화가 찾아왔다.')
                    return
                elif man_hp <= 0:
                    return
            elif event == 1:
                po = potion()
                po1 += po
            elif event == 2:
                print()
            elif event == 3:
                portal = portal_coord(map_size, position)
                h += 1
                print(f'{h}층 던전 진입')
                break
            if i == 2:
                print('맵이 변합니다.')


main()
