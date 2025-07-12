# Импортируем нужные модули, объявляем переменные и очищаем экран
import time
import os
os.system('cls')
action = None
menu = "Меню:\n1 - добавить запись\n2 - посмотреть все записи\n3 - режим Гарри Поттера.\n"
# Запуск основного цикла
while action != 'выход':
    # Выводим меню и запрашиваем номер действия
    print(menu)
    action = input("Введите номер действия, которое Вы хотите выбрать: ")
    if action in ['1', '2', '3', "выход"]:
        if action == 'выход':
            # Выход
            print("Спасибо за использование нашей программы!")
            quit()
        if action == '1':
            # Добавление задачи
            # Принимаем текст заметки
            text = input("Введите текст записи:\n")
            a = 1
            # Считаем сколько записей в ежедневнике
            with open("diary.txt", 'r', encoding='utf-8') as txt_file:
                for line in txt_file:
                    a += 1
            # Сохраняем пункт в файле
            with open("diary.txt", 'a', encoding='utf-8') as txt_file:
                txt_file.write(f"{a}. {text}\n")
        if action == '2':
            # Вывод всех заданий
            a = 1
            with open("diary.txt", 'r', encoding='utf-8') as txt_file:
                for line in txt_file:
                    print(line, end="")
                    a += 1
        # Мини-тест по второй части Гарри Поттера
        if action == '3':
            os.system('cls')
            time.sleep(2)
            a = input("Какая была первая реплика Гарри Поттера в общении с дневником Редла? ")
            if a == "Меня зовут Гарри Поттер" or a == "My name is Harry Potter":
                time.sleep(0.5)
                print("Привет, Гарри Поттер, меня зовут Том Редл")
                a = input("Продолжайте разговор: ")
                if a == 'Тебе известно что-нибудь о Тайной комнате?' or 'Тебе известно что-нибудь о тайной комнате?' or 'Тебе известно что - нибудь о Тайной комнате?' or 'Тебе известно что - нибудь про тайной комнате?' or a == 'Do you know anything about the Chamber of Secret?':
                    time.sleep(1.5)
                    print('Да.')
                    a = input("Ваша очередь: ")
                    if a == 'Ты расскажешь мне?' or a == 'Can you tell me?':
                        time.sleep(1)
                        print('Нет.')
                        time.sleep(7)
                        print("Но я могу показать тебе")
                        time.sleep(5)
                        print("Давай, я перенесу тебя на 50 лет назад.\n\n\n13 июня")
                    else:
                        print('Неверно! "Ты расскажешь мне?" или "Can you tell me?".')
                else:
                        print('Неверно! "Тебе известно что-нибудь о Тайной комнате?" или "Do you know anything about the Chamber of Secret?".')
            else:
                print('Неверно! "Меня зовут Гарри Поттер" или "My name is Harry Potter".')
    # На случай если введен не номер действия
    else:
        print("Такого действия нет!")