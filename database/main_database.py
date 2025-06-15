import sqlite3
from abc import ABC, abstractmethod
from contextlib import contextmanager


class BaseCRUD(ABC):
    def __init__(self, path_db = None, table_name = None):
        self.path_db = path_db or "database/database.db"
        self.table_name = table_name or self.__class__.__name__.lower()

    @contextmanager
    def get_connection(self):
        connection = sqlite3.connect(self.path_db)
        try:
            yield connection
        finally:
            connection.close()

    def handle_db_operation(self, operation_func, *args, **kwargs):
        try:
            return operation_func(*args, **kwargs)
        except sqlite3.OperationalError as e:
            if 'no such table' in str(e).lower() or 'unable to open' in str(e).lower():
                self.migrate()
                return operation_func(*args, **kwargs)
            else:
                raise

    @abstractmethod
    def migrate(self):
        """Bazani yaratish uchun metod — subclasslar majburan implementatsiya qilishlari kerak"""
        pass

    def _insert(self, *args, **kwargs):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            columns = ', '.join(kwargs.keys())
            placeholders = ', '.join('?' for _ in kwargs)
            query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
            cursor.execute(query, tuple(kwargs.values()))
            connection.commit()
            return cursor.lastrowid

    def create(self,*args, **kwargs):
        return self.handle_db_operation(self._insert, *args, **kwargs)

    def _get_all(self):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)
            return cursor.fetchall()

    def get_all(self):
        return self.handle_db_operation(self._get_all)

    def _get(self, id, id_column="id", all=False):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            query = f"SELECT * FROM {self.table_name} WHERE {id_column}=?"
            cursor.execute(query, (id,))
            return cursor.fetchall() if all else cursor.fetchone()

    def get(self, *args, **kwargs):
        return self.handle_db_operation(self._get, *args, **kwargs)

    def _update(self, id, id_column="id", **kwargs):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            columns = ', '.join(f"{key}=?" for key in kwargs)
            query = f"UPDATE {self.table_name} SET {columns} WHERE {id_column}=?"
            cursor.execute(query, (*kwargs.values(), id))
            connection.commit()
            return True

    def update(self,*args, **kwargs):
        return self.handle_db_operation(self._update, *args, **kwargs)

    def _delete(self, id, id_column="id"):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            query = f"DELETE FROM {self.table_name} WHERE {id_column}=?"
            cursor.execute(query, (id,))
            connection.commit()
            return True

    def delete(self, *args, **kwargs):
        return self.handle_db_operation(self._delete, *args, **kwargs)
