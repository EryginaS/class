# coding=utf-8


class PrintEditor():
    biblioteka = ['Пушкин', 'Лермантов', 'Толстой', 'Маяковский']

    def __init__(self, name):
        """
        Функция инициализации родительского класса
        :param name: установка имени для экземпляра класса
        """
        self.name = name

    def set_info_about_print_edotors(self, count_str, year, author):
        """
        Функция установки свойств для экземпляров класса
        :param count_str: количество страниц
        :param year: год издания
        :param author: автор
        :return:
        """
        self.count_str = count_str
        self.year = year
        self.author = author

    def this_author_is_legend(self):
        """
        Функция, отображающая является ли автор данного петаного издания
        легендарным.
        :return:
        """
        if self.author in self.biblioteka:
            print(self.author + " являетя легендарным писателем.")
        else:
            print(self.author + " не является легендарным писателем.")

    def get_info(self):
        """
        Функция, отображающая информацию о печатном издании
        :return:
        """
        try:
            print("Печатное издание: ", self.name, ',',  self.year, "года", ',',
            "Количество страниц:", self.count_str)
        except:
            print("Не удалось получить информацию о печатном издании.")


# Класс Журнал наследует все методы и свойства класса Печатное издание
class Magazine(PrintEditor):
    editors = []

    def __init__(self, name):
        """
        Перегрузка родительского метода __init__
        :param name:
        """
        self.name = "Журнал "+"'"+name+"'"

    def set_editors(self, editors):
        self.editors = editors

    def get_info_about_magazins(self):
        try:
            print("Название: ", self.name)
        except:
            print("Не удалось найти информацию о журнале.")
        try:
            print("Автор: ", self.author)
        except:
            print("не удалось найти информацию об авторе этого журнала.")
        try:
            print("Список редакторов:")
            for i in self.editors:
                print(i)
        except:
            print("Не удалось получить информацию о редакторах журнала.")


class Book(PrintEditor):
    genre = ''
    author = ''
    iz = []

    def __init__(self, name):
        self.name = "Книга "+"'"+name+"'"

    def set_inf(self, gr, au):
        self.genre = gr
        self.author = au

    def izdaniy(self, a):
        self.iz = a

    def get_info_about_book(self):
        try:
            print("Название ", self.name)
        except:
            print("Не удалось найти информацию о названии  книги.")
        try:
            print("Автор ", self.author)
        except:
            print("Не удалось найти информацию об авторе  книги.")
        try:
            print("Жанр: ", self.genre)
        except:
            print("Не удалось найти информацию о жанре этой книги.")
        try:
            print("Количество страниц :", self.count_str)
        except:
            print("Не удалось найти информацию о количестве страниц.")
        try:
            print("Существующие издания:")
            for i in self.iz:
                print(i)
        except:
            print("Не удалось найти информацию о количестве изданий.")


class StudentBook(PrintEditor):
    thing = ''

    def __init__(self, name):
        self.name = "Учебник "+"'"+name+"'"

    def set_info_about_st_book(self, th, str, aut):
        self.thing = th
        self.str = str
        self.author = aut

    def get_info_about_st_book(self):
        try:
            print("Название ", self.name)
        except:
            print("Не удалось найти информацию о названии  учебника.")
        try:
            print("Автор ", self.author)
        except:
            print("Не удалось найти информацию об авторе этого учебника.")
        try:
            print("Предмет: ", self.thing)
        except:
            print("Не удалось найти информацию о предмете учебника.")
        try:
            print("Количество страниц :", self.count_str)
        except:
            print("Не удалось найти информацию о количестве страниц.")


print('______________________________________________________')
print('метод __init__ у родительского класса:')
iz = PrintEditor("PB")
print(iz.name)
print('пеегруженный __init__ у:')
mag = Magazine("Издание")
print(mag.name)
bk = Book("Капитанская дочка")
print(bk.name)
st = StudentBook('Сложная арифметика')
print(st.name)
print('______________________________________________________')
print("Родительский метод")
bk.author = "Пушкин"
mag.author = "Перник"
st.author = "Цыбулько"
bk.this_author_is_legend()
mag.this_author_is_legend()
st.this_author_is_legend()
print('______________________________________________________')
print("Оригинальные методы")
print('______________________________________________________')
bk.set_inf("Классика", "Пушкин")
bk.count_str = 230
bk.izdaniy([1987, 2000, 2007, 2018])
bk.get_info_about_book()
print('______________________________________________________')
mag.set_editors(['Коваль', "Пунков"])
mag.get_info_about_magazins()
print('______________________________________________________')
st.thing = "Математика"
st.get_info_about_st_book()
