Этот проект представляет собой простую утилиту для управления финансовыми записями в формате XML.

Функциональность

Добавление записи: Позволяет пользователю добавить новую финансовую запись, указав категорию (доход или расход), сумму и описание.
Изменение записи: Позволяет пользователю изменить существующую запись по идентификатору, обновив категорию, сумму и описание. (редактирование происходит по id записи)
Получение баланса: Позволяет пользователю получить текущий баланс, подсчитав сумму доходов и расходов.

Запуск утилиты:
Перейдите в каталог проекта и запустите файл main.py

Структура проекта
cli.py: Файл с функциями для взаимодействия с пользователем через командную строку.
common_func.py: Файл с общими функциями, используемыми несколькими модулями.
main.py: Главный файл для запуска утилиты.
wallet.xml: XML-файл для хранения финансовых записей. (Создаётся автоматически если файла нет)

Функция add_record_cli() добавляет запись в xml файл

Функция modify_record() изменяет запись пользователя (прежде чем изменить запись нужно ввести ид изменяемой записи)

Функция get_balance() выводит пользователю его текущий баланс

Функция get_records_by_criteria() получает данные по критерии которую выберет пользователь
    Если выбрана дата то ищет на текущий день

Все консольные команды не привязаны к регистру букв:
    Например команда "Добавить" == "ДобАвить" == "добавить" (можно писать буквы в любом регистре)