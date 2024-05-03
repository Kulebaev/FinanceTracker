from xml_utils import create_or_read_xml, write_to_xml
from datetime import datetime
import cummon_func

# Функция для добавления новой записи через CLI
def add_record_cli():
    # Создаем структуру XML или читаем существующий файл
    tree, root, loaded_data = create_or_read_xml("wallet.xml")

    category = cummon_func.get_valid_category_input()

    amount = cummon_func.get_valid_float_input()

    description = input("Введите описание: ")

    # Получаем текущую дату и время
    current_datetime = datetime.now()
    date_string = current_datetime.strftime("%d-%m-%Y %H:%M")

    # Ищем максимальный идентификатор записи
    max_id = max([int(record["id"]) for record in loaded_data], default=0) + 1

    # Создаем словарь с новой записью
    new_record_data = {"id": str(max_id + 1), "date": date_string, "category": category, "amount": amount, "description": description}

    # Добавляем новую запись в XML-файл
    write_to_xml(tree, root, [new_record_data])

    print("Новая запись успешно добавлена!")


def modify_record():
    # Создаем структуру XML или читаем существующий файл
    tree, root, loaded_data = create_or_read_xml("wallet.xml")

    record_id = cummon_func.get_valid_record_id(loaded_data)

    record_element = root.find(f"./record[@id='{record_id}']")

    if record_element is None:
        print("Элемент с указанным id не найден.")
        modify_record()
        return

    text = 'категории'
    if cummon_func.confirm_modification(text):
        category = cummon_func.get_valid_category_input()
        record_element.find("category").text = category

    text = 'суммы'
    if cummon_func.confirm_modification(text):
        text = ''
        amount = cummon_func.get_valid_float_input()
        record_element.find("amount").text = str(amount)

    text = 'описания'
    if cummon_func.confirm_modification(text):
        description = input("Введите новое описание: ")
        record_element.find("description").text = description

    # Перезаписываем данные в XML-файл
    tree.write("wallet.xml", encoding="utf-8")

    print("Запись успешно изменена!")


def get_balance():
    tree, _, _ = create_or_read_xml("wallet.xml")
    income_total = 0
    expense_total = 0

    # Проходим по всем записям и суммируем доходы и расходы
    for record in tree.findall("./record"):
        category = record.find("category").text.lower()
        amount = float(record.find("amount").text)
        if category == "доход":
            income_total += amount
        elif category == "расход":
            expense_total += amount

    # Вычисляем баланс
    balance = income_total - expense_total

    # Выводим результат с округлением до двух знаков после запятой
    print(f"Ваш баланс составляет: {balance:.2f}")


def get_records_by_criteria():
    # Создаем структуру XML или читаем существующий файл
    tree, root, loaded_data = create_or_read_xml("wallet.xml")

    print("Выберите критерий для поиска записей:")
    print("1. По дате")
    print("2. По идентификатору")
    print("3. По сумме")
    print("4. По категории")
    print("5. Вернуться в главное меню")

    choice = input("Введите номер критерия: ")

    while True:
        if choice == "1":
            cummon_func.get_records_by_date(loaded_data)
            break
        elif choice == "2":
            cummon_func.get_records_by_id(loaded_data)
            break
        elif choice == "3":
            cummon_func.get_records_by_amount(loaded_data)
            break
        elif choice == "4":
            cummon_func.get_records_by_category(loaded_data)
            break
        elif choice == "5":
            return
        else:
            print("Неверный выбор. Пожалуйста, выберите номер критерия из списка.")


