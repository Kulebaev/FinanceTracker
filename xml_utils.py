import xml.etree.ElementTree as ET
import os

# Функция для создания XML-структуры, если файл пустой или его нет
def create_or_read_xml(filename):
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        tree, root = create_xml_structure()
        tree.write(filename, encoding="utf-8")  # Записываем данные в XML-файл с указанием кодировки UTF-8
        return tree, root, []  # Возвращаем пустой список данных
    else:
        tree = ET.parse(filename)  # Парсим XML-файл
        root = tree.getroot()  # Получаем корневой элемент
        data = read_from_xml(tree)
        return tree, root, data

# Функция для создания XML-документа с заданной структурой данных
def create_xml_structure():
    root = ET.Element("wallet")  # Создаем корневой элемент "wallet"
    tree = ET.ElementTree(root)  # Создаем объект ElementTree с корневым элементом
    return tree, root

# Функция для записи данных в XML-файл
def write_to_xml(tree, root, data):
    for record_data in data:
        record = ET.SubElement(root, "record", id=str(record_data["id"]))  # Создаем элемент "record" с идентификатором
        for key, value in record_data.items():
            if key == "amount":
                # Форматируем значение суммы с двумя знаками после запятой
                formatted_amount = "{:.2f}".format(float(value))
                ET.SubElement(record, key).text = formatted_amount
            else:
                ET.SubElement(record, key).text = str(value)  # Добавляем дочерние элементы с данными, если это не сумма
    tree.write("wallet.xml", encoding="utf-8")  # Записываем данные в XML-файл с указанием кодировки UTF-8

# Функция для чтения данных из XML-файла
def read_from_xml(tree):
    root = tree.getroot()  # Получаем корневой элемент
    data = []
    for record in root.findall("record"):  # Итерируемся по всем элементам "record"
        record_data = {}  # Создаем словарь для хранения данных одной записи
        for elem in record:
            record_data[elem.tag] = elem.text  # Добавляем данные в словарь
        data.append(record_data)  # Добавляем словарь с данными в список
    return data
