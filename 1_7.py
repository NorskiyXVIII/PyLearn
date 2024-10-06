def main():
    frst_arr = [30, 13.1, "jouyr", True] # объявление первого массив с помощью квадратных скобок
    secn_arr = list(frst_arr) # объявление второго массива с помощью функтсии
    # функтсия list позволяет нам как создавать просто массив, указывая элементы
    # так и передавать другой массив и он будет копироваться

    print(f"first arr - {frst_arr}, second arr - {secn_arr}")

    arr = [3] * 4 # [3, 3, 3, 3]
    print(arr)

    people = ["Влад", "Дамир"] * 3 # ["Влад", "Дамир", "Влад", "Дамир", "Влад", "Дамир"]
    print(people)

    print(f"{frst_arr[3]} - третий элемент, {people[-1]} - первый элемент с контса")
    people[0] = "Руслан"
    print(people) # Руслан

    ruslan, damir1, vlad1, damir2, vlad2, damir3 = people
    print(f"['{ruslan}', '{damir1}', '{vlad1}', '{damir2}', '{vlad2}', '{damir3}']")

    printarr(people)

    if iseq(frst_arr, secn_arr):
        print("Они равные!")
    else:
        print("Они неравные.")

    slicef = people[1:len(people):2] # с 1 элемента до последнего элемента с шагом 2 - [Дамир, Дамир, Дамир]
    print(slicef)

    # ПРОДОЛЖЕНИЕ...


def printarr(arr):
    print("Array -> [", end="")
    #for elem in arr:
    #    print(f"'{elem}'", end=", ")
    
    i = 0
    while i < len(arr):
        print(f"'{arr[i]}'", end=", ")
        i += 1
    
    print("\b\b]")

def iseq(lst1, lst2):
    return lst1 == lst2


main()