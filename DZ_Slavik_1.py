#24.02.2023
name_bot = "Вика"
print(f"здравствуйте меня, зовут {name_bot}")
my_name = input("а как зовут вас? ")
print(f"приятно с вами познокомиться, {my_name}")
age = int(input ("а сколько тебе лет? "))
print(f"ого, тебе уже {age} лет. \nПредставляешь, через 10 лет тебе будет {age+10}")
risc_user = float(input("а кокой у тебя рост?"))
print(f"ого, ты токой высокий! мой рост всего 0.53 м. ты выше меня на {risc_user-0.53} метра!")
print(f"Вау я так много о тебе у зналa {my_name} ты выше меня на {risc_user-0.53} метра, и тебе {age} лет")
answer_one = input("""получить совет-1
расказать анекдот-2
получить прогноз погоды-3
ваш ответ: """)
if answer_one == "1":
    answer_two = input("""Вы хотите совет-про 
    1-CS:GO 
    2-про здоровья 
    ваш ответ: """)
    if answer_two == "1":
        print ("разминайся перед матчем")
    elif answer_two == "2":
        print ("делай зарядку по утрам")
    else:
        print("я вас не понял")
elif answer_one == "2":
    print("Кто из мужчин не мечтал уснуть седьмого марта, чтобы проснуться девятого?")
elif answer_one == "3":
    print("прогноз прогноз в Донецке +2° Пасмурно, 4,3 м/с ветер, +2 вечером, −2 ночью")
else: 
    print("я вас не понял")
