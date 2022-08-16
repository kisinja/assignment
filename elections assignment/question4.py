def dementia():
    person = input("Enter the name of the person: ")
    if person == "John".lower():
        print("John is Luke's father!")
    elif person == "Mary".lower():
        print("Mary is Luke's mother!")
    elif person == "Joan".lower():
        print("Joan is Luke's Sister")

    else:
        print("The person given is not a member of the family!!!")


dementia()