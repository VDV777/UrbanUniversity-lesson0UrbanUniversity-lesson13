# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
calls: int = 0


def count_calls() -> None:
    global calls
    calls += 1


# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
def string_info(string: str) -> tuple:
    count_calls()
    return string.__len__(), string.upper(), string.lower()


# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
def is_contains(string: str, list_to_search: list[str]) -> bool:
    count_calls()
    lowercase_words = [word.lower() for word in list_to_search]
    return string.lower() in lowercase_words


# Пункты задачи:
# Создать переменную calls = 0 вне функций.
# Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# Вывести значение переменной calls на экран(в консоль).
string_info('Hello')
string_info('World')

is_contains('One', ['One', 'Two', 'Four'])
is_contains('Cat', ['Dog', 'Monkey', 'Wale'])

print(calls)
