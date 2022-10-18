import sqlite3


class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def select_all(self):
        # получаем все строки
        with self.connection:
            return self.cursor.execute('SELECT * FROM music').fetchall()

    def select_single(self, rownum):
        # получаем одну строку с номером rownum
        with self.connection:
            return self.cursor.execute('SELECT * FROM music WHERE id = ?', (rownum,)).fetchall()[0]

    def count_rows(self):
        # считаем количество строк
        with self.connection:
            result = self.cursor.execute('SELECT * FROM music').fetchall()
            return len(result)

    def close(self):
        # закрываем соединение с БД
        self.connection.close()
