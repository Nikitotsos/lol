
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




# class Transport: 
#     def init(self, brand, model, year): 
#         self.brand = brand 
#         self.model = model 
#         self.year = year 
 
#     def get_info(self): 
#         return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}" 
 
#     def honk(self): 
#         return "Generic transport sound!" 
 
 
# class Car(Transport): 
#     def init(self, brand, model, year, fuel_type): 
#         super().init(brand, model, year) 
#         self.fuel_type = fuel_type 
 
#     def get_info(self): 
#         return f"{super().get_info()}, Fuel Type: {self.fuel_type}" 
 
#     def honk(self): 
#         return "Beep-beep!" 
 
 
# class Bicycle(Transport): 
#     def init(self, brand, model, year, gear_count): 
#         super().init(brand, model, year) 
#         self.gear_count = gear_count 
 
#     def get_info(self): 
#         return f"{super().get_info()}, Gear Count: {self.gear_count}" 
 
#     def honk(self): 
#         return "Ding-ding!" 
 
 
# if name == "main": 
  
#     car = Car("Mercedes-AMG", " CLE Coupe", 2024, "Gasoline") 
#     print(car.get_info())   
#     print(car.honk())       
 
#     bicycle = Bicycle("Giant", "Escape 3", 2022, 21) 
#     print(bicycle.get_info())   
#     print(bicycle.honk())