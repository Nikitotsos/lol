
import os

def add_contact():
    name = input("Введіть ім'я: ")
    phone = input("Введіть номер телефону: ")
    email = input("Введіть електронну пошту: ")
    
    with open("contacts.txt", "a") as file:
        file.write(f"Ім'я: {name}, Телефон: {phone}, Електронна пошта: {email}\n")

def view_contacts():
    if os.path.exists("contacts.txt"):
        with open("contacts.txt", "r") as file:
            print(file.read())
    else:
        print("Контакти відсутні.")

def main():
    while True:
        print("\n1. Додати новий контакт\n2. Переглянути список контактів\n3. Вийти")
        choice = input("Ваш вибір: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            break

if __name__ == "__main__":
    main()
