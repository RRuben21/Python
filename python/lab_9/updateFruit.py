fruit_list = ["apple", "banana", "cherry", "gooseberry", "kumquat", "orange", "pineapple"]

print('Fruit List: Apple, Banana, Cherry, Gooseberry, Kumquat, Orange, Pineapple')

find= True

while find == True:
    search= input("Please enter a name of your favriote fruit from the list: ").lower()
    for i in range(len(fruit_list)):
        if search == (fruit_list[i]):
            print("That fruit is in the list.")
            print('The index value for the fruit is: ', fruit_list.index(search))
            break
        elif i == (len(fruit_list)-1):
            print("That fruit is not in the list.")
    searchagain=input("Would you like to search for another fruit? Y/N: ").lower()
    if searchagain ==("y") or searchagain ==("yes"):
        print("OK")
        find=True
    else:
        print("Thank you, Ending program...")
        find=False
