from queue import Queue
import random

queue = Queue()

def generate_request():
    request = f"Request-{random.randint(1, 1000)}"
    queue.put(request)
    print(f"Заявка {request} додана до черги.")

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f'Заявка {request} обробляється')
    else:
        print('Черга пуста.')

if __name__ == '__main__':
    while True:
        action = input("Введіть 'g' для генерації заявки, 'p' для обробки заявки, або 'q' для виходу: ")
        if action == 'g':
            generate_request()
        elif action == 'p':
            process_request()
        elif action == 'q':
            print("Програма завершує роботу.")
            break
        else:
            print("Невірна команда. Будь ласка, спробуйте знову.")