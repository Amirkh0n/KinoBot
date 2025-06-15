from .main_database import BaseCRUD


class Users(BaseCRUD):
    def migrate(self):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    user_id INTEGER PRIMARY KEY NOT NULL,
                    name TEXT
                );
            ''')
            connection.commit()