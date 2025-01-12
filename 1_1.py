print("Привет, мир!")

# В Python можно получить ошибку для отступов
#print("Привет, ")
#   print("мир!")
# вызовет ошибку

# Строки можно писать и так:
print("Привет," " мир" "!")
# можно поставить запятую после строчки 
print("Привет,", "мир!")
# тогда python самостоятельно в строчке поставит пробел между перечисляемыми строками
# т.е без запятых питон просто соеденяет строки, а с запятой между строчек ставит пробел

# можно создавать переменные а так же принимать ввод
name = input("Введите свое имя: ")
print("Привет,", name, "!") # однако после вызова переменных требуется запятая

# есть тип данных complex(комплексные числа):
cmpl = 3+34j # нельзя называть переменные как ключевые слова
print(cmpl) # (3+34j)

# в переменные строки можно разбивать на части
my_str = ("Это мой текст"
"Муахаха")
# Для этого нужно всего лишь их объеденять в скобки 


# выведет "Это мой текстМуахаха"
print(my_str)

#строки можно делать многострочными
my_str1 = '''lorem ipsum
amet ken
choujitsu''' 
# нужно лишь между строками написать 6 одинарных кавычек

# каждая строчка выводится с новой строки
print(my_str1)

#Есть так же f - строки
name  = input("Введите ваше имя: ")
age   = int(input("Введите ваш возраст: "))
hobby = input("Введите ваше хобби: ")

#f - строки могут форматировать строку. И без разнитсы, какая это строка - многострочная или обычная
stat = f'''
    Имя   пользователя: {name}
    Лет   пользователю: {age}
    Хобби пользователя: {hobby}
'''

print(stat)
# можно так же узнать тип данных переменной с помощью функтсии type()
print(type(stat)) # <class 'str'>

# можно так же изменять конетс выводимой строки:

print("Привет, мир! Меня зовут", end=" ")
print(f"{name} ", end="и мне ")
print(age)

# аргумент end у print в конетс строки выводит какую то строку.
# Изначально end="\n", т.е переводит на новую строку вывод
# однако мы можем этот конетс изменять на любую строку

# !ВАЖНО! писать после строки запятую, и только потом end
# python может складывать только строки!


# Есть кстати отличия от / и // в python
# / делит ненатсело, т.е 7 / 2 = 3.5, а // делит без остатка, т.е 3
# есть так же оператсия возведения в степень
# 2 ** 4 = 2^4 = 16

print(f"7 делим на 2 разными способами: [/({7 / 2})] и [//({7 // 2})]", end=" и ")
print(f"возводим 2 в степень 4: {2 ** 4}")

# Есть функтсия round, которое округляет до ближайшего четного числа:
print(round(3.5)) # 4
print(round(2.9)) # 2

# можно написать второй аргумент, который будет округлять до n-ного порядка
print(round(2.394819, 2)) # округляем до 2 знаков
print(round(3.145961, 3)) # округляем до 3 знаков

number = 39 # 10 - система
# можно форматированно писать числа в разных системах счисления
print(f"десятичная - {number}, шестнадтсатеричная - {number:0x}, восьмеричная - {number:0}, двоичная - {number:0b}")
# все побитовые оператсии работают в питоне

# есть конструктсия in, которая говорит true, если допустим строка "hello" есть в строке "hello incredible"
print("hello" in "hello incredible") # true
# мы можем добавить not
print("Привет" not in "Привет!!!") # false
print(type("Привет" not in "Хахаха")) # <class: bool>