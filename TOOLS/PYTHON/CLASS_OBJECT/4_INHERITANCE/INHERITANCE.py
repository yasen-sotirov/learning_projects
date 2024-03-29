"INHERITANCE"   # наследява атрибути и методи
                # може да дефинира нови атрибути и методи, а съществуващите да бъдат променени
                # полза: преизползване на код
                # super - извиква атрибутите на базовия клас
                # IS-A връзка: Мениджърът Е Служител
                # ВАЖНО за SUPER()   https://realpython.com/python-super/


class Employee:         # super, parent, base class
    COMPANY = "DSK"
    #          параметри ↓
    def __init__(self, name: str, salary: int, department: str):
        self.name = name
        self.salary = salary                    # атрибути / пропъртита на инстанцията
        self.department = department

    def public_info(self):
        return f'{self.name} {self.department}'

    def _private_info(self):
        return f'Private info: \nname: {self.name}, department: {self.department}, salary: {self.salary}'



"НАСЛЕДЯВАНЕ НА КЛАС"   # НАСЛЕДЯВА ВСИЧКО КОЕТО НЕ Е ПРЕНАПИСАНО
class CustomerSupport(Employee):
    # sub, child, derived class
    def __init__(self, name, salary, department, email: str, phone_number: int):
        # разширяваме, като допълваме с параметри
        super().__init__(name, salary, department)
        # наследява init-a na супер класа
        self.email = email
        self.phone_number = phone_number

    def contacts(self):
        return f'{self.name}, {self.email}, {self.phone_number}'



"НАСЛЕДЯВАНЕ НА КЛАС"
class Manger(Employee):
    def __init__(self, name, salary, department, bonus: int):       # не подавам нови атрибути
        super().__init__(name, salary, department)     # наследява __init + атрибутите
        self.bonus = bonus
        self.employees_list = []

    def add_employee(self, new_employee):
        self.employees_list.append(new_employee)



"ИНСТАНЦИИ"                 # аргументи ↓
support_1 = CustomerSupport("Jordan", 3000, "sales", "example@mail.com", 359888123456)
print(support_1.contacts())

manager_1 = Manger("Todor", 4000, "managers", 300)
manager_1.add_employee(support_1.name)
print(manager_1.employees_list)


"ACCESS PROTECTED METHOD"
# print(manager_1._private_info())


"MIXIN"
# клас който не може да работи самостоятелно
# Използва се за да добави функционалност чрез множествено наследяване.

# class CEO:
#     def fire_employee(self, employee):
#         return f"{employee.name} was fired."
#         del employee
#
#
# class TopManager(Manger, CEO):
#     def __init__(self, name, salary, department, bonus):
#         super().__init__(name, salary, department, bonus)
#
# ceo_1 = TopManager('Georgiev', 5000, 'managers', 500)
# ceo_1.fire_employee(support_1)
# print(support_1)





"МНОЖЕСТВЕНО НАСЛЕДЯВАНЕ НА  МЕТОДИ"
# class Father:
#     def skills(self):
#         print('gardening')
#
# class Mother:
#     def skills(self):
#         print('cooking')
#
# class Child(Father, Mother):
#     def skills(self):
#         Father.skills(self)
#         Mother.skills(self)
#         print('sport')
#
#
# child = Child()
# child.skills()


# nums = [1, 2, 3]
#
# for el in nums:
#     square = el ** 2
#     print(el)


