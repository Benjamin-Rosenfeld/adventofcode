f = open("Day 2/day2.txt", "r+")
suam=0
for x in f:
    parced = x.split(': ')
    stringparced = parced[1]
    games = stringparced.split('; ')
    works = True
    gameblue = 0
    gamegreen=0
    gamered=0
    for game in games:
        game = game.split(', ')
        for gammes in game:
            gammes = gammes.replace('\n', '')
            num, color = gammes.split(" ")
            if color=='red' and int(num)>gamered:
                gamered=int(num)
            elif color=='blue' and int(num) > gameblue:
                gameblue=int(num)
            elif color=='green' and int(num)>gamegreen:
                gamegreen=int(num)
    
    suam+=(gamered*gameblue*gamegreen)
print(suam)