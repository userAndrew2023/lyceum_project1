from peewee import *

db = SqliteDatabase('database.db')


class User(Model):
    name = TextField()
    password = TextField()
    role = TextField()

    class Meta:
        database = db


class Task(Model):
    title = TextField()
    assigner_id = ForeignKeyField(User, related_name='task')
    performer_id = ForeignKeyField(User, related_name='task')

    class Meta:
        database = db
