import shelve
from SQLighter import SQLighter
from config import shelve_name, database_name


def count_rows():
    # метод считает общее число строк в БД и сохраняет в хранилище.
    # Далее из него выбирается музыка
    db = SQLighter(database_name)
    rowsum = db.count_rows()
    with shelve.open(shelve_name) as storage:
        storage['row_counts'] = rowsum


def get_rows_count():
    # Получаем из хранилища число строк в БД (:return: (int))
    with shelve.open(shelve_name) as storage:
        rowsum = storage['rows_count']
    return rowsum

def set_user_game(chat_id, estimated_answers):
    # записываем пользователя в игроки и запоминаем ответ
    with shelve.open(shelve_name) as storage:
        storage[str(chat_id)] = estimated_answers

def finish_user_game(chat_id):
    # заканчиваем игру
    with shelve.open(shelve_name) as storage:
        del storage[str(chat_id)]

def get_answer_for_user(chat_id):
    # получаем правильный ответ от пользователя
    with shelve.open(shelve_name) as storage:
        try:
            answer = storage[str(chat_id)]
            return answer

        except KeyError:
            return None