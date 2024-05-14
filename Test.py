# # # 1. Создайте класс Person. В конструкторе он принимает name, surname, age.
# # # атрибут name должен быть приватным
# # # атрибут surname должен быть защищенным
# # # Создайте метод info, который возвращает name, surname, age. Создайте 3 экземпляра класса и вызовите методы.

# # # 2. Напишите класс Math. Используйте внутри класса магические методы __add__ и __sub__ для сложения и вычитания. После того вы все сделали, создайте экземпляр класса и выведите значения из класса.


# # # 3. Напишите класс Сonstructor, которое имитирует строительство жилого дома. В конструкторе мы передаем сколько этажей мы хотим построить. Затем делаем метод build, который строит наш дом пока мы не дойдем до этажа которую мы хотим построить. И также создайте магический метод __str__, для выведение данных нашего класса

# # # 4. Вам нужно улучшить задание №1:
# # # Данные должны попадать в БД

# 5. Создать заметки:
# Создать БД с полями для 
# Заголовок (title) - Заголовок задачи
# Описание ( description ) - Подробное описание задачи
# completed -  флаг, указывающий, завершена ли задача (по умолчанию False) Добавить возможность создание задачи и редактирование ( поставить True )

# 1 - задание
# class Person:
#     def __init__(self, name, surname, age):
#         self.__name = name
#         self._surname = surname
#         self.age = age
    
#     @property
#     def name(self):
#         return self.__name

#     def surname(self):
#         return self._surname

#     def info(self):
#         print(f"Имя - {self.__name}, Фамилия - {self._surname}, Возраст - {self.age}")

# user = Person("Nurdan", "Iskanov", 15)

# print(user.name)  
# print(user.surname())
# print(user.age)       
# user.info()       
# 2 - задания
# class Math:
#     def __init__(self, numbers_1, numbers_2):
#         self.numbers_1 = numbers_1
#         self.numbers_2 = numbers_2

#     def __add__(self, other):
#         result = self.numbers_1 + other.numbers_1
#         return f"Результат сложения: {result}"

#     def __sub__(self, other):
#         result = self.numbers_1 - other.numbers_1
#         return f"Результат сложения: {result}"

# num1 = Math(12, 12)
# num2 = Math(13, 12)
# print(num1 + num2)
# print(num1 - num2)

#3 - задание

# import time

# class Constructor:
#     def __init__(self, floors):
#         self.floors = floors

#     def __str__(self):
#         return f"Построено - {self.floors} этажей"

#     def build(self):
#         n = 0
#         while self.floors > n:
#             n += 1
#             print(f"Построен этаж {n}.")
#             time.sleep(2)  
#         print(f"Построено {self.floors} этажей. Закончено.")

# building = Constructor(5)

# print(building)

# building.build()

# 4 - задания
# import sqlite3

# connect = sqlite3.connect("user.db")
# cursor = connect.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS user(
#                id INTEGER PRIMARY KEY,
#                name VARCHAR (100) NOT NULL,
#                surname VARCHAR (100) NOT NULL,
#                age INTEGER NOT NULL
# )
# """)

# class Person:
#     def __init__(self):
#         self.name = None
#         self.surname = None
#         self.age = 0
    
#     def registr(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         cursor.execute(f"""INSERT INTO user (name, surname, age)
#         VALUES ('{name}','{surname}','{age}')""")
#         connect.commit()
    
#     def mein(self):
#         while True:
#             print("1 - зарегистрироваться", "2 - выйти")
#             command = int(input("Выберите действие: "))
#             if command == 1: 
#                 print("ЗАРЕГАЙТЕСЬ")
#                 name = input("Введите ваше имя: ")
#                 surname = input("Введите вашу фамилию: ")
#                 age = int(input("Введите ваш возраст: "))
#                 print("Регистрация прошла успешно")
#                 self.registr(name, surname, age)
            
#             elif command == 2:
#                 break
#             else:
#                 print("Неверный номер действия")

# pers = Person()    
# pers.mein()

# 5 - задания

# import sqlite3

# connect = sqlite3.connect("tasks.db")
# cursor = connect.cursor()

# cursor.execute("""CREATE TABLE IF NOT EXISTS tasks(
#                id INTEGER PRIMARY KEY,
#                title VARCHAR (100) NOT NULL,
#                description TEXT NOT NULL,
#                completed BOOLEAN DEFAULT 0
# )
# """)

# class TaskManager:
#     def __init__(self):
#         pass
    
#     def create_task(self, title, description):
#         cursor.execute(f"""INSERT INTO tasks (title, description) VALUES (?, ?)""", (title, description))
#         connect.commit()

#     def edit_task(self, task_id, completed):
#         cursor.execute("""UPDATE tasks SET completed= ? WHERE id= ?""", (completed, task_id))
#         connect.commit()

# task_manager = TaskManager()

# def create_and_edit_task():
#     print("Создание новой задачи...")
#     title = input("Введите название задачи: ")
#     description = input("Введите описание задачи: ")
#     task_manager.create_task(title, description)
#     print("Задача успешно создана!")

#     edit = input("Хотите пометить эту задачу как выполненную? (да/нет): ")
#     if edit == "Да":
#         task_id = cursor.lastrowid  
#         task_manager.edit_task(task_id, True)
#         print("Задача отмечена как выполненная.")

# while True:
#     print("1 - Создать новую задачу", "2 - выйти" "")
#     choice = input("Выбери действие: ")
#     if choice == 1:
#         create_and_edit_task()
#     elif choice == 2:
#         break
#     else:
#         print("неверный выбор. Пожалуйста, попробуйте еще раз.")

# connect.close()


   