import cli

# Функция для выполнения действия, выбранного пользователем
def perform_action(action):
    # Приводим действие к нижнему регистру
    action = action.lower()
    
    if action == "выход":
        return

    actions = {
        "добавить": cli.add_record_cli,
        "изменить": cli.modify_record,
        "получить баланс": cli.get_balance,
        "получить записи": cli.get_records_by_criteria
    }
    
    chosen_action = actions.get(action)
    
    if not chosen_action:
        print("Неверное действие!")
        start_cli()
        return
       
    chosen_action()
    start_cli()


def start_cli():
    action = input("Что вы хотите сделать? (Добавить/Изменить/Получить баланс/Получить записи/Выход): ")

    # Выполняем выбранное действие
    perform_action(action)

# Пример использования
if __name__ == "__main__":
    # Запрашиваем у пользователя выбранное действие
    start_cli()
