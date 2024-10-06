def main():
    print("Здравствуйте! Введите 1 число: ", end = "")
    try:
        frst = int(input())
    except:
        print("Ошибка: Не правильно интерпретировано входящее значение в 1 число.")
    finally:
        print("Число 1 принято.")
    print("Здравствуйте! Введите 2 число: ", end = "")
    try:
        sec = int(input())
    except:
        print("Ошибка: Не правильно интерпретировано входящее значение в 2 число.")
    finally:
        print("Число 2 принято.")

    try:
        print(f"Плюс:      {frst + sec}")
        print(f"Минус:     {frst - sec}")
        print(f"Умножение: {frst * sec}")
        print(f"Деление:   {frst // sec}")
    except ZeroDivisionError:
        print("Ошибка: Нельзя делить на 0!")
    finally:
        print("Задача решена.")

main()