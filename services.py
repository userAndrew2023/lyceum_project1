import hashlib
import json
import socket
import threading
import sqlite3

con = sqlite3.connect("database.db")
con.row_factory = sqlite3.Row


class UserService:
    def create(self, name: str, password: str, role: str):
        password = hashlib.md5(password.encode()).hexdigest()
        with con.cursor() as cursor:
            cursor.execute(f"INSERT INTO users (name, password, role) VALUES ('{name}', '{password}', '{role}')")
            con.commit()
        sync(json.dumps({
            "type": "create",
            "model": "User",
            "data": {
                "name": name,
                "password": password,
                "role": role
            }
        }))

    def findById(self, id_: int):
        with con.cursor() as cursor:
            cursor.execute(f"SELECT * FROM users WHERE id = {id_}")
            return cursor.fetchone()

    def findAll(self):
        with con.cursor() as cursor:
            cursor.execute(f"SELECT * FROM users")
            return cursor.fetchall()


class TaskService:
    def create(self, title: str, assigner_id: int, performer_id: int, status: str):
        with con.cursor() as cursor:
            cursor.execute(f"INSERT INTO tasks (title, assigner_id, performer_id, status) "
                           f"VALUES ('{title}', '{assigner_id}', '{performer_id}', '{status}')")
            con.commit()
        sync(json.dumps({
            "type": "create",
            "model": "User",
            "data": {
                "title": title,
                "assigner_id": assigner_id,
                "performer_id": performer_id,
                "status": status,
            }
        }))

    def findById(self, id_: int):
        with con.cursor() as cursor:
            cursor.execute(f"SELECT * FROM tasks WHERE id = {id_}")
            return cursor.fetchone()

    def findAll(self):
        with con.cursor() as cursor:
            cursor.execute(f"SELECT * FROM tasks")
            return cursor.fetchall()

    def deleteById(self, id: int):
        with con.cursor() as cursor:
            cursor.execute(f"DELETE FROM tasks WHERE id = '{id}'")
            con.commit()
        sync(json.dumps({
            "type": "delete",
            "model": "Task",
            "data": {
                "id": id
            }
        }))


def sync(message: str):
    for port in range(5001, 6000):
        threading.Thread(target=connect_and_send_message, args=[port, message]).start()


def connect_and_send_message(port, message: str):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("localhost", port))
        client_socket.send(message.encode('utf-8'))
        client_socket.close()
    except Exception:
        pass
