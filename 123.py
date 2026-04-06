import json # Подключаем инструмент для работы с файлами формата .json

balance = 1000 # Создаем кошелек, в котором в начале лежит 1000 денег
def delete_items(items):
    name_to_delet=input("введите название товара, который хотите удалить ")
    for item in items: # Перебираем все товары в списке
        if item['name'].lower() == name_to_delet.lower(): # Проверяем, совпадает ли имя (игнорируя большие буквы)
            items.remove(item)
            save_goods(items)
            return
    print("неправильно")
def add_items (items):
    name= input("введите название товара ")
    price=int (input("введите цену товара "))
    count=int (input("введите кол-во товара "))
    new_product={"name":name,"price":price,"count":count}
    items.append(new_product)
    save_goods(items)
    print("успешно сохранил")
def save_goods (items):
    with open('database.json', 'w', encoding='utf-8') as f: # Открываем файл на чтение
        data = {"products":items}
        json.dump(data,f,ensure_ascii=False,indent=3) # Отдаем только список продуктов
# Функция для покупки товара
def buy_item(items, item_name):
    global balance # Говорим функции, что будем менять внешнюю переменную денег
    for item in items: # Перебираем все товары в списке
        if item['name'].lower() == item_name.lower(): # Проверяем, совпадает ли имя (игнорируя большие буквы)
            if item['count'] > 0: # Смотрим, есть ли товар на складе
                if balance >= item['price']: # Проверяем, хватит ли у нас денег
                    item['count'] -= 1 # Уменьшаем количество товара в магазине
                    balance -= item['price'] # Вычитаем цену из нашего кошелька
                    save_goods(items)
                    print(f"Куплено, молодец, ваш баланс: {balance}")
                    return # Выходим из функции, так как дело сделано
                else:
                    print("Не хватает средств")
                    return
            else:
                print("Товар закончился")
                return
    print ("Товар не найден")

# Функция для продажи товара магазину
def sell_item(items, item_name):
    global balance 
    for item in items:
        if item['name'].lower() == item_name.lower(): # Ищем товар по имени
            sell_price = int(item['price'] * 0.8) # Считаем цену выкупа (80% от стоимости)
            item['count'] += 1 # Добавляем товар обратно на склад магазина
            balance += sell_price # Добавляем деньги в наш кошелек
            save_goods(items)
            print(f"Вы что-то продали магазину, ваш новый баланс: {balance}")
            return
        print("Товар не найден") # Эта строка сработает, если имя не подошло

# Функция загрузки данных из файла
def load_goods():
    with open('database.json', 'r', encoding='utf-8') as f: # Открываем файл на чтение
        data = json.load(f) # Превращаем текст из JSON в понятный Python словарь
        return data['products'] # Отдаем только список продуктов

# Функция для отрисовки меню
def menu(items):
        print(f"\nДобро пожаловать! Наш баланс: {balance} руб.") # Показываем деньги
        print("--- Ассортимент ---")
        for i, item in enumerate(items): # Цикл, который нумерует товары (1, 2, 3...)
            print(f"{i+1}. {item['name']} | Цена: {item['price']} | В наличии: {item['count']}")
        return True

goods = load_goods() # Загружаем товары из файла в переменную goods перед стартом

try: # Начало блока проверки на ошибки
    while True: # Бесконечный цикл, чтобы программа не закрылась сразу
        menu(goods) # Вызываем меню, чтобы видеть товары и баланс
        print("\nДействия: 1 - Купить, 2 - Продать, 3 - Выход, 4 - добавить товар,5 - убрать товар")
        choice = input("Выберите действие: ") # Просим пользователя нажать кнопку
        
        if choice == "1":
            name = input("Что хотите купить? ")
            buy_item(goods, name) # Запускаем функцию покупки
        elif choice == "2":
            name = input("Что хотите продать? ")
            sell_item(goods, name) # Запускаем функцию продажи
        elif choice == "3":
            print("До свидания!")
            break # Выходим из цикла while, тем самым закрывая программу
        elif choice =="4":
            add_items(goods)
        elif choice=="5":   
            delete_items(goods)

        
            
except ValueError: # Если вместо цифр в меню что-то пойдет не так (хотя тут input строковый)
    print("Введите числовое значение!")
