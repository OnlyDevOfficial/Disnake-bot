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
        level = result[4]
        exp = result[5]
        return username , balance , level , exp
    
    # def test(self , id):
    #     money_data = self.cur.execute("SELECT money FROM users WHERE user_id = ?" , (id,)).fetchone()
    #     money_int = money_data[0]
    #     money = money_int + 10
    #     return money

    def casino(self , id , money , result):
        money_data = self.cur.execute("SELECT money FROM users WHERE user_id = ?" , (id,)).fetchone()
        money_user = money_data[0]
        if result == True:
            win = money_user + money
            self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?)" , (win , id,))
            self.connect.commit() 

        else:
            win = money_user - money
            self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?)" , (win , id,))
            self.connect.commit()
    
    def work(self , win , id):
        money_data = self.cur.execute("SELECT money FROM users WHERE user_id = ?" , (id,)).fetchone()
        money = money_data[0]
        result = money + win
        self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?)" , (result , id,))
        self.connect.commit()

    def add_item(self , name , price , role):
        self.cur.execute("INSERT INTO shop (`name` , `price` , `role`) VALUES (? , ? , ?)" , (name , price , role,))
        self.connect.commit()

    def shop(self):
        result = self.cur.execute("SELECT * FROM shop").fetchall()
        return result
    
    def buy(self , name , id):
        result = self.cur.execute("SELECT role FROM shop WHERE name = ?" , (name,)).fetchone()
        price_data = self.cur.execute("SELECT price FROM shop WHERE name = ?" , (name,)).fetchone()
        price = price_data[0]
        money_user_data = self.cur.execute("SELECT money FROM users WHERE user_id = ?" , (id,)).fetchone()
        money_user = money_user_data[0]
        if money_user >= price:
            money_result = money_user - price
            self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?)" , (money_result , id,))
            self.connect.commit()
            return result[0]
        
        else:
            return "На вашем счету недостаточно средств!"
        
    def guess(self , id , bet , bool):
        money_data = self.cur.execute("SELECT money FROM users WHERE user_id = ?" , (id,)).fetchone()
        money_user = money_data[0]
        if bool == True:
            win = bet * 4
            win_user = money_user + win
            self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?" , (win_user , id,))
            self.connect.commit()

        else:
            win_user = money_user - bet
            self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?)" , (win_user , id,))
            self.connect.commit()

    def exp(self , id , exp):
        user_exp_data = self.cur.execute("SELECT exp FROM users WHERE user_id = ?" , (id,)).fetchone()
        user_exp = user_exp_data[0]
        add_exp = user_exp + exp
        self.cur.execute("UPDATE users SET exp = (?) WHERE user_id = (?)" , (add_exp , id,))
        self.connect.commit()
        
    def level_up(self , id):
        user_exp_data = self.cur.execute("SELECT exp FROM users WHERE user_id = ?" , (id,)).fetchone()
        user_level_data = self.cur.execute("SELECT level FROM users WHERE user_id = ?" , (id,)).fetchone()
        user_exp = user_exp_data[0]
        user_level = user_level_data[0]
        if user_exp >= 300:
            level = user_level + 1
            self.cur.execute("UPDATE users SET exp = (?) WHERE user_id = (?)" , (0 , id,))
            self.cur.execute("UPDATE users SET level = (?) WHERE user_id = (?)" , (level , id,))
            self.connect.commit()
            return True
        
        else:
            return False

    
    def close(self):
        """Закрывавем соединение с базой данных"""
        self.connect.close()