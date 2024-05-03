from datetime import datetime



def get_valid_float_input():
    while True:
        amount = input("Введите сумму: ")
        try:
            amount = float(amount.replace(",", "."))  # Заменяем запятую на точку и преобразуем в число с плавающей точкой
            return amount
        except ValueError:
            print("Сумма должна быть числом.")


def get_valid_category_input():

    while True:
        category = input("Введите новую категорию (Доход/Расход): ").lower()
        if category in ["доход", "расход"]:
            return category
        else:
            print("Неверная категория. Пожалуйста, введите 'Доход' или 'Расход'.")


def get_valid_record_id(loaded_data):
    while True:
        # Запрашиваем у пользователя id записи, которую он хочет изменить
        record_id = input("Введите id записи для изменения: ")
        if record_id.isdigit():
            record_id = int(record_id)
            # Проверяем, существует ли запись с указанным id
            record_index = None
            for i, record in enumerate(loaded_data):
                if int(record["id"]) == record_id:
                    record_index = i
                    return record_id
            if record_index is not None:
                break
            else:
                print("Запись с указанным id не найдена.")
        else:
            print("Id записи должен быть числом.")


def confirm_modification(text: str):
    while True:
        confirmation = input(f"Вы уверены, что хотите изменить данные {text}? (Y/N): ").strip().upper()
        if confirmation == "Y":
            return True
        elif confirmation == "N":
            return False
        else:
            print("Пожалуйста, введите 'Y' или 'N'.")


def validate_date_format(date_string):
    try:
        datetime.strptime(date_string, "%d-%m-%Y")
        return True
    except ValueError:
        return False
    

def get_records_by_date(loaded_data):
    while True:
        date = input("Введите дату в формате ДД-ММ-ГГГГ: ")
        validate_date_format = validate_date_format(date)
        if validate_date_format:
            records = [record for record in loaded_data if record["date"].startswith(date)]
            print_records(records)
            break
        else:
            print("Неверный формат даты. Пожалуйста, введите дату в формате ДД-ММ-ГГГГ.")

def get_records_by_id(loaded_data):
    while True:
        record_id = input("Введите идентификатор записи: ")
        if record_id.isdigit():
            records = [record for record in loaded_data if record["id"] == record_id]
            print_records(records)
            break
        else:
            print("Идентификатор записи должен быть целым числом.")

def get_records_by_amount(loaded_data):
    value = get_valid_float_input()
    amount = "{:.2f}".format(float(value))
    records = [record for record in loaded_data if record["amount"] == str(amount)]
    print_records(records)
    

def get_records_by_category(loaded_data):
    while True:
        category = input("Введите категорию (доход/расход): ").lower()
        if category in ["доход", "расход"]:
            records = [record for record in loaded_data if record["category"] == category]
            print_records(records)
            break
        else:
            print("Неверная категория. Пожалуйста, введите 'доход' или 'расход'.")


def print_records(records):
    if not records:
        print("Записей не найдено.")
    else:
        print("Найденные записи:")
        for record in records:
            print(f"ID: {record['id']}, Дата: {record['date']}, Категория: {record['category']}, Сумма: {record['amount']}, Описание: {record['description']}")