import sqlite3

class DataBase:
    def __init__(self , db):
        self.connect = sqlite3.connect(db)
        self.cur = self.connect.cursor()

    def check_user(self , id):
        result = self.cur.execute("SELECT `id` FROM `users` WHERE `user_id` = ?" , (id,))
        return bool(len(result.fetchall()))
    
    def create(self , id , user_name):
        self.cur.execute("INSERT INTO `users` (`user_id` , `username`) VALUES (? , ?)" , (id, user_name,))
        return self.connect.commit()
    
    def data(self , id):
        result = self.cur.execute("SELECT * FROM users WHERE `user_id` = ?" , (id,)).fetchone()
        username = result[2]
        balance = result[3]
        return username , balance
    
    def close(self):
        """Закрывавем соединение с базой данных"""
        self.connect.close()