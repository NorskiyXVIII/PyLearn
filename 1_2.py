lang = input("Type your lang: ")
stat_placeholder = "Nil"

while "Англ" not in lang or "Eng" not in lang or "Нем" not in lang or "De" not in lang or "Рус" not in lang or "Rus" not in lang:
    if "Англ" in lang or "Eng" in lang:
        print("Hello, your lang English;", end=" ")
        name = input("Print your name: ")
        age  = int(input(f"{name}, print your age: "))
        bio  = input(f"{name}[{age}], print your bio: ")
    
        if bio == "" or bio == "" or bio == "Nil" or bio == "Null" or "No" in bio or "no" in bio:
            stat_placeholder = f'''
            -----INFORMATION-----
            Name = {name}
            Age  = {age}
            bio  = [!(No bio yet)]
            -----INFORMATION-----
            '''
        else:
            stat_placeholder = f'''
            ------INFORMATION------
            Name = {name}
            Age  = {age}
            bio  = {bio}
            ------INFORMATION------
            ''' 
        if stat_placeholder == "Nil":
            print("Critical error in prog")
            exit(1)

        print(stat_placeholder)
        break
    elif "Нем" in lang or "De" in lang:
        print("Hallo, Ihre Sprache Deutsch;", end=" ")
        name = input("Drucken Sie Ihren Namen: ")
        age  = int(input(f"{name}, gib dein Alter aus: "))
        bio  = input(f"{name} [{age}], drucke deine Biografie aus: ")
 
        if bio == "" or bio == "" or bio == "Null" or bio == "Null" or "Nein" in bio or "nein" in bio:
            stat_placeholder = f'''
            -----INFORMATION-----
            Name  = {name}
            Alter = {age}
            bio   = [!(Noch keine Biografie)]
            -----INFORMATION-----
            '''
        else:
            stat_placeholder = f'''
            ------INFORMATION------
            Name  = {name}
            Alter = {age}
            bio   = {bio}
            ------INFORMATION------
            ''' 
    
        if stat_placeholder == "Nil":
            print("Kritischer Fehler im Programm")
            exit(1)

        print(stat_placeholder)
        break
    elif "Рус" in lang or "Rus" in lang:
        print("Здравствуйте, вы выбрали Русский язык;", end=" ")
        name = input("Введите свое имя: ")
        age  = int(input(f"{name}, Введите свой возраст: "))
        bio  = input(f"{name}[{age}], Введите свое описание: ")
    
        if bio == "" or bio == "" or bio == "Ничего" or bio == "Нулл" or "Не" in bio or "не" in bio:
            stat_placeholder = f'''
            -----INFORMATION-----
            Name = {name}
            Age  = {age}
            bio  = [!(Описание не задано)]
            -----INFORMATION-----
            '''
        else:
            stat_placeholder = f'''
            ------INFORMATION------
            Name = {name}
            Age  = {age}
            bio  = {bio}
            ------INFORMATION------
            ''' 
        if stat_placeholder == "Nil":
            print("Критическая ошибка в программе")
            exit(1)
        
        print(stat_placeholder)
        break
    else:
        print(f"unknown lang[{lang}]")
        lang = input("Type your lang: ")


# есть еще тсикл for, с функтсией range, но я не знаю пока, где ее можно применить без массивов