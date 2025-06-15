from .main_database import BaseCRUD


class Movies(BaseCRUD):
    def migrate(self):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {self.table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    description TEXT,
                    short_video_id TEXT,
                    full_video_id TEXT,
                    code TEXT UNIQUE NOT NULL,
                    view_count INTEGER DEFAULT 0
                );
            ''')
            connection.commit()
            
    def view(self, id,):
        self.update(id, id_column)