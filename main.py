from services import *

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 6000)
server_socket.bind(server_address)
server_socket.listen(5)


def handle_client(client):
    while True:
        try:
            d = client.recv(1024)
            if not d:
                break
            message: str = d.decode('utf-8')
            message: dict = json.loads(message)
            data: dict = message.get("data")
            if message.get("model") == "User":
                if message.get("type") == "create":
                    UserService().create(*data.values())
            elif message.get("model") == "Task":
                if message.get("type") == "create":
                    TaskService().create(*data.values())
                elif message.get("type") == "delete":
                    TaskService().deleteById(data.get("id"))
        except Exception as e:
            print(f"Ошибка при обработке сообщения: {e}")
            break

    client.close()


while True:
    client_socket, client_address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
