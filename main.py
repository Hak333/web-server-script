import socket

HOST = '0.0.0.0'
PORT = int(input("Specify port: "))

with open('index.html', 'r') as f:
    response_body = f.read()

response = """HTTP/1.1 200 OK\r\nContent-Length: {0}\r\n\r\n{1}""".format(len(response_body), response_body)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Server listening on', HOST, PORT)
    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        with conn:
            data = conn.recv(1024)
            print('Received', data)
            conn.sendall(response.encode())
