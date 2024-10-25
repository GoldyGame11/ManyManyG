import time

class Dog:
    eat = 100
    water = 100
    sleep = 100
    cash = 100


    while eat > 0:
        print(f"Текущая еда: {eat}")
        a = input("Купить еду? ")
        print(cash)
        if a == "Да":
            eat =+ 100
            cash =- 10
        eat  -= 10
        time.sleep(2)

        print(f"Текущая вода: {water}")
        a = input("Купить воду?? ")
        print(cash)
        if a == "Да":
            water =+ 100
            cash =- 10
        water -= 10
        time.sleep(2)
        print(f"Текущая сон: {sleep}")
        a = input("Положить спать? ")
        print(cash)
        if a == "Да":
            sleep = + 100
            cash = - 10
        sleep -= 10
        time.sleep(2)

dog = Dog()
dog.start()



