
# как основная функтсия в Си, хехе
def main(): 
    for i in range(0, 10, 2): # с 0 до 10(не включая 10) с промежутком 2
    # с 0 до 8 посчитает, где 8 включительно
        print(f"{i} итерация: ", end="")
        say_msg()
        print("")


def say_msg():
    # можно создавать локальные функтсии + писать однострочной нотацией:
    def print_hello(): print("hello", end="")
    def print_world(): print("world", end="")

    print_hello()
    print(" ", end="")
    print_world()

main()