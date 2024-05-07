import socket

def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1',2000))
        server.listen(4)
        print('Working...')

        while True:
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode('utf-8')
            print(data)

            HDRS = 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n'.encode('utf-8')
            content = load_page_from_get_request(data)
            client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)

    except KeyboardInterrupt:
        server.close()
        print('Shutting down the server...')

def load_page_from_get_request(requested_data):
    HDRS = 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\n\n'
    HDRS_404 = 'HTTP/1.1 404 OK\nContent-Type: text/html; charset=utf-8\n\n'
    path = requested_data.split(' ')[1]
    response = ''

    try:
        with open('just_python/server'+path, 'rb') as file:
            response = file.read()
            return HDRS.encode('utf-8') + response
    except FileNotFoundError:
        return (HDRS_404 + 'Sorry, page not found :(').encode('utf-8')
    
if __name__ == "__main__":
    start_server()


