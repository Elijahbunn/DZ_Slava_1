my_name = input(" Как вас зовут? ")
print(f" Приятно с вами познокомится {my_name}")
one_artifact = False
two_artifact = False
three_artifact = False
score = 0
print(f""" Самое время отправляться в путешествие!
 {my_name}, ты начинаешь игру с 0 очков. В ходе игры ты будешь получаться очки, за которые ты сможешь приобрести интересные вещи и артефакты, кото-рые помогут тебе достичь победы.
 За каждый ответ на 1-ое задание: 10 очков
 За правильный ответ на 2-ое задание: 20 очков
 За правильный ответ на 3-ое задание: 30 очков""")
print(""" Два медвежонка нашли головку сыра. Они долго спорили, как ее поделить, но никто не хотел уступать.
 Мимо пробегала лиса. 
 Узнав, о чем спор, она предложила помочь, разломив головку сыра на 2 части так, чтобы одна из них была полкилограмма,а другая меньше.
 Затем она спросила, усмехаясь: Куски равны? Жадные медвежата дали отрицательный ответ.
 Тогда лиса откусила от большей части, но так, чтобы от нее остался кусок меньше, чем другая часть, и повторила вопрос.
 И на этот раз медвежата сообщили, что получились неравные части. 
 После этого лиса повторила откусывание еще 9 раз, каждый раз откусывая одинаковое количество сыра.
 В результате остались маленькие кусочки, причем один из них оказался на 20 граммов больше другого.
 Лиса заявила, что медвежатам трудно угодить. 
 Она отправила оба кусочка в рот и, вильнув хвостом, скрылась в кустах.
 Какова была масса головки сыра в граммах?""")
answer_one = input(" Ваш ответ: ")
if answer_one == "450":
    one_artifact = True
    score+=10
    print(f" Теперь у вас {score} очков.")
else: 
    print(f" Ответ не верный у вас {score} очков. ")
answer_two = input(""" Стрелки бегают по кругу, Не догнать никак друг друга. Иногда встречаются, Но быстро разбегаются. 
 Ваш ответ: """)
if answer_two == "часы":
    two_artifact = True
    score+=20
    print(f" Теперь у вас {score} очков.")
else:
    print(f" Ответ не верный у вас {score} очков. ")
answer_three = input(""" В каком городе родился Александр Македонский. 
 Ваш Ответ: """)
if answer_three == "пелла":
    three_artifact = True
    score+=30
    print(f" Теперь у вас {score} очков.")
else:
    print(f" Ответ не верный у вас {score} очков. ")
print(""" Ты завершил испытания, можешь проследовать в магазин и выбрать себе что-нибуть одно: 
1. Мороженое 10 points
2. Щит капитана америки 20 points
3. Зелье силы 24 points
4. Яблочный сок 13 points
5. Футбольный мяч 14 points
6. Колонка 12 points
7. Зелье скорости 24
8. Телефон 19 points
9. Playstation 5 22 points
10. Пропустить """)
product = input(" Вы будете что-то покупать в магазине? ")
if product == "1" or product == "2" or product == "3" or product == "4" or product == "5" or product == "6" or product == "7" or product == "8" or product == "9":
    if product == "1" and score >=10:
        print(" Вы купили Мороженое. ")
        score-=10
    elif product == "2" and score >=20:
        print(" Вы купили Щит капитана америки.")
        score-=20
    elif product == "3" and score >=24:
        print(" Вы купили зелья силы.")
        score-=24
    elif product == "4" and score >=13:
        print(" Вы купили Яблочный сок.")
        score-=13
    elif product == "5" and score >=14:
        print(" Вы купили футбольный мяч.")
        score-=14
    elif product == "6" and score >=12:
        print(" Вы купили колонку.")
        score-=12
    elif product == "7" and score >=24:
        print(" Вы купили зелья скорости.")
        score-=24
    elif product == "8" and score >=19:
        print(" Вы купили телефон.")
        score-=19
    elif product == "9" and score >=22:
        print(" Вы купили playstation 5.")
        score-=22
    else:
        print(" У вас недостаточно points.")
elif product == "10":
    print(" Вы проиграли магазин.")
else:
    print(" Простите я вас не понял.")
if one_artifact == two_artifact == three_artifact ==True:
    print(f" Поздравляю ты молодец! Ты прошёл текстовой квест у вас {score} points. ")
elif one_artifact == two_artifact ==True and three_artifact ==False:
    print(f" Вы не ответили на 3 вопрос у вас {score} points.")
elif one_artifact == three_artifact == True and two_artifact ==False:
    print(f" Вы не ответили на 2 вопрос у вас {score} points.")
elif two_artifact == three_artifact ==True and one_artifact ==False:
    print(f" Вы не ответили на 1 вопрос у вас {score} points.")
elif (one_artifact == two_artifact ==False and three_artifact ==True) or (one_artifact == three_artifact ==False and two_artifact ==True) or (two_artifact == three_artifact ==False and one_artifact ==True):
    print(" Вы ответили на 1 вопрос вы проиграли.")
else:
    print(" Вы проиграли.")

