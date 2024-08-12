class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    __file_name = "products.txt"
                                                        # Если файла нет, то создается файл products.txt
    file = open(__file_name, "a")                       # и открывается в режиме "a" (режим APPEND (добавление))
    file.close()                                        # Закрытие файла (обязательно)

    def get_products(self):
        file = open(self.__file_name, "r")             # Октрытие файла в режиме "r" (режим READ (чтение))
        f = file.read()                                # Сохранение содержимого файла в переменной f
        file.close()                                   # Закрытие файла (обязательно)
        return f

    def add(self, *products):
        for product in products:                              # Ищем продукт (product) в списке products
            if f"{product.name}" not in self.get_products():  # Если продукт не найден в файле,
                file = open(self.__file_name, "a")            # то окрываем файл в режиме "a" (режим APPEND (добавление))
                file.write(f"{product}\n")                    # Добавляем продукт в файл с переносом строки (\n)
                file.close()                                  # Закрытие файла (обязательно)
            else:
                print (f"Продукт {product.name} уже есть в магазине")   # Если продукт найден, выводим сообщение



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
