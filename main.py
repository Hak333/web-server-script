import socket

HOST = '127.0.0.1'  # IP-адрес хоста
PORT = int(input("Specify port: "))  # Порт сервера

# Открываем файл index.html и считываем его содержимое
with open('index.html', 'r') as f:
    response_body = f.read()

# Формируем HTTP-ответ, включая заголовки и содержимое
response = """HTTP/1.1 200 OK\r\nContent-Length: {0}\r\n\r\n{1}""".format(len(response_body), response_body)

# Создаем TCP-сокет
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Назначаем адрес и порт сервера
    s.bind((HOST, PORT))
    # Слушаем входящие подключения
    s.listen()
    print('Server listening on', HOST, PORT)
    while True:
        # Принимаем входящее соединение
        conn, addr = s.accept()
        print('Connected by', addr)
        with conn:
            # Получаем данные от клиента
            data = conn.recv(1024)
            # Печатаем полученные данные
            print('Received', data)
            # Отправляем HTTP-ответ клиенту
            conn.sendall(response.encode())
