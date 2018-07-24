import MySQLdb
import MySQLdb.cursors
import logging


class MySql:
    TABLE = ""

    @staticmethod
    def connect_to_db():
        return MySQLdb.connect(
            "localhost", "root", "", "trimm-api",
            cursorclass=MySQLdb.cursors.DictCursor)

    @staticmethod
    def simpe_query(query, params=None):
        db = MySql.connect_to_db()
        cursor = db.cursor()
        cursor.execute(query, params)
        db.commit()
        db.close()

    @staticmethod
    def fetchall_query(query, params=None):
        db = MySql.connect_to_db()
        cursor = db.cursor()
        cursor.execute(query, params)
        data = cursor.fetchall()
        db.close()
        return data

    @classmethod
    def insert_into(cls, **kwargs):
        keys = kwargs.keys()
        query = "INSERT INTO {} ({}) VALUES({})".format(
            cls.TABLE, ', '.join(keys), ', '.join(['%s'] * len(keys)))
        MySql.simpe_query(query, kwargs.values())

    @classmethod
    def select_where(cls, field, value):
        query = "SELECT * FROM {} WHERE {}=%s".format(cls.TABLE, field)
        return MySql.fetchall_query(query, (value, ))

    @classmethod
    def delete_where(cls, field, value):
        query = "DELETE FROM {} WHERE {}=%s".format(cls.TABLE, field)
        MySql.simpe_query(query, (value, ))

    @classmethod
    def update_where(cls, field, value, **kwargs):
        """
        Updates stuff in the database.
            :param field: field where update is mage
            :param value: value to compare it against
            :param kwargs: the fields and their values that
            need updating
        """
        fields = []

        for key in kwargs:
            fields.append(key + '=%s')
        
        query = "UPDATE {} SET {} WHERE {}=%s".format(
            cls.TABLE, ', '.join(fields), field)
        MySql.simpe_query(query, (*kwargs.values(), value))


class Users(MySql):
    TABLE = "users"


class Spending(MySql):
    TABLE = "spending"


class Categories(MySql):
    TABLE = "categories"
