f = open("Day 2/day2.txt", "r+")
suam=0
for x in f:
    parced = x.split(': ')
    stringparced = parced[1]
    games = stringparced.split('; ')
    works = True
    for game in games:
        game = game.split(', ')
        for gammes in game:
            gammes = gammes.replace('\n', '')
            num, color = gammes.split(" ")
            if color=='red' and int(num)>12:
                works = False
            elif color=='blue' and int(num) > 14:
                works = False
            elif color=='green' and int(num)>13:
                works = False
    if works:
        suam+=int(parced[0].split()[1])
print(suam)