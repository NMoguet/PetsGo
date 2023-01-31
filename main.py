# Create a pet class to store pet information
class Pet:
    def __init__(self, name, breed, age, owner_first, owner_last, owner_phone, expenses):
        self.name = name
        self.breed = breed
        self.age = age
        self.owner_first = owner_first
        self.owner_last = owner_last
        self.owner_phone = owner_phone
        self.expenses = expenses


# Create an array to store pet information
pet_database = []


# Function to input pet information
def input_pet_info():
    name = input("Enter pet name: ")
    breed = input("Enter breed: ")
    age = input("Enter age: ")
    owner_first = input("Enter owner first name: ")
    owner_last = input("Enter owner last name: ")
    owner_phone = input("Enter owner phone number: ")
    expenses = []
    while True:
        expense = input("Enter an expense (or press enter to stop): ")
        if expense == "":
            break
        expenses.append(expense)
    pet = Pet(name, breed, age, owner_first, owner_last, owner_phone, expenses)
    pet_database.append(pet)


# Function to display pet information
def display_pet_info(pet_number):
    pet = pet_database[pet_number - 1]
    print("Pet Name:", pet.name)
    print("Breed:", pet.breed)
    print("Age:", pet.age)
    print("Owner:", pet.owner_first, pet.owner_last)
    print("Phone:", pet.owner_phone)
    print("Expenses:", ", ".join(pet.expenses))


# Function to search pet information by name or breed
def search_pet(search_query):
    results = []
    for i, pet in enumerate(pet_database):
        if search_query in pet.name or search_query in pet.breed:
            results.append((i + 1, pet.name))
    return results


# Text-based user interface
while True:
    print("Pet Database")
    print("1. Input pet information")
    print("2. Display pet information")
    print("3. Search pet")
    print("4. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        input_pet_info()
    elif choice == "2":
        pet_number = int(input("Enter pet number: "))
        display_pet_info(pet_number)
    elif choice == "3":
        search_query = input("Enter search query: ")
        results = search_pet(search_query)
        if results:
            print("Results:")
            for i, result in results:
                print(i, result)
        else:
            print("No results found.")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.")
