import sqlite3

class DataBase:
    def __init__(self , db):
        self.connect = sqlite3.connect(db)
        self.cur = self.connect.cursor()


    def check_commands(self , guild):
        result = self.cur.execute("SELECT `command` FROM `commands` WHERE `guild` = ?" , (guild,)).fetchone()
        return result
    
    def check_embed(self , guild , command , option):
        result = self.cur.execute("SELECT ? FROM embed WHERE (guild = ? AND command = ?)" , (option , guild , command)).fetchone()
        if result[0]:
            return result[0]
        
        else:
            return False
    
    def check_button(self , guild , command):
        result = self.cur.execute("SELECT button FROM commands WHERE (guild = ? AND command = ?)" , (guild , command)).fetchone()
        if result[0] == True:
            return True
        
        else:
            return False

    def check_user(self , id):
        result = self.cur.execute("SELECT `id` FROM `users` WHERE `user_id` = ?" , (id,))
        return bool(len(result.fetchall()))
    
    def create(self , id , user_name , guild):
        self.cur.execute("INSERT INTO `users` (`user_id` , `username` , `guild`) VALUES (? , ? , ?)" , (id, user_name, guild,))
        return self.connect.commit()
    
    def data(self , id):
        result = self.cur.execute("SELECT * FROM users WHERE `user_id` = ?" , (id,)).fetchone()
        username = result[2]
        bank = result[3]
        balance = result[4]
        level = result[5]
        work = result[7]
        return username , balance , level , bank , work
    
    def exp_check(self , id):
        result = self.cur.execute("SELECT * FROM users WHERE `user_id` = ?" , (id,)).fetchone()
        exp = result[6]
        return exp
    
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

    def add_item(self , name , price , role , guild):
        self.cur.execute("INSERT INTO shop (`name` , `price` , `role` , `guild`) VALUES (? , ? , ?)" , (name , price , role, guild,))
        self.connect.commit()

    def shop(self , guild):
        result = self.cur.execute("SELECT * FROM shop WHERE guild = ?" , (guild,)).fetchall()
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
        

    def russian(self , id , win , bool):
        user_money_data = self.cur.execute("SELECT money FROM users WHERE user_id = ?" , (id,)).fetchone()
        user_money = user_money_data[0]
        if bool == True:
            money = user_money + win
            self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?)" , (money , id,))
            self.connect.commit()

        else:
            money = user_money - win
            self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?)" , (money , id,))
            self.connect.commit()

    def debiting(self , id , quantity):
        user_money_data = self.cur.execute("SELECT money FROM users WHERE user_id = ?" , (id,)).fetchone()
        user_money = user_money_data[0]
        money = user_money - quantity
        self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?)" , (money , id,))
        self.connect.commit()

    def bank(self , id , bet):
        user_money_data = self.cur.execute("SELECT money FROM users WHERE user_id = ?" , (id,)).fetchone()
        user_bank_data = self.cur.execute("SELECT bank FROM users WHERE user_id = ?" , (id,)).fetchone()
        user_money = user_money_data[0]
        money_bank = user_bank_data[0]
        money_user = user_money - bet
        bank_user = money_bank + bet
        self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?)" , (money_user , id,))
        self.cur.execute("UPDATE users SET bank = (?) WHERE user_id = (?)" , (bank_user , id,))
        self.connect.commit()

    def take(self , id , bet):
        user_money_data = self.cur.execute("SELECT money FROM users WHERE user_id = ?" , (id,)).fetchone()
        user_bank_data = self.cur.execute("SELECT bank FROM users WHERE user_id = ?" , (id,)).fetchone()
        user_money = user_money_data[0]
        money_bank = user_bank_data[0]
        money_user = user_money + bet
        bank_user = money_bank - bet
        self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?)" , (money_user , id,))
        self.cur.execute("UPDATE users SET bank = (?) WHERE user_id = (?)" , (bank_user , id,))
        self.connect.commit()

    def transfer(self , id , member , money):
        user_money_data = self.cur.execute("SELECT money FROM users WHERE user_id = ?" , (id,)).fetchone()
        user_money_tranfer_data = self.cur.execute("SELECT money FROM users WHERE user_id = ?" , (member,)).fetchone()
        user_money = user_money_data[0]
        user_money_tranfer = user_money_tranfer_data[0]
        if user_money >= money:
            transfer = user_money_tranfer + money
            member_money = user_money - money
            self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?)" , (member_money , id,))
            self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?)" , (transfer , member,))
            self.connect.commit()

        else:
            return "Error"
     
    def steal(self , id , user , win):
        user_money_data = self.cur.execute("SELECT money FROM users WHERE user_id = ?" , (id,)).fetchone()
        user_money_data_steal = self.cur.execute("SELECT money FROM users WHERE user_id = ?" , (user,)).fetchone()
        user_money = user_money_data[0]
        user_money_steal = user_money_data_steal[0]
        if user_money_steal > 4000:
            win_user = user_money + win
            steal = user_money_steal - win
            self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?)" , (win_user , id,))
            self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?)" , (steal , user,))
            self.connect.commit()

        else:
            return "На счету жертвы не больше 4000🍬"

    def hire(self , id , work):
        user_money_data = self.cur.execute("SELECT money FROM users WHERE user_id = ?" , (id,)).fetchone()
        user_money = user_money_data[0]
        if work == "Кассир":
            money = user_money - 30000
            self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?)" , (money , id,))
            self.cur.execute("UPDATE users SET work = (?) WHERE user_id = (?)" , ("Кассир" , id,))
            self.connect.commit()

        elif work == "Телеведущий":
            money = user_money - 100000
            self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?)" , (money , id,))
            self.cur.execute("UPDATE users SET work = (?) WHERE user_id = (?)" , ("Телеведущий" , id,))
            self.connect.commit()


        elif work == "Банкир":
            money = user_money - 300000
            self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?)" , (money , id,))
            self.cur.execute("UPDATE users SET work = (?) WHERE user_id = (?)" , ("Банкир" , id,))
            self.connect.commit()

    def settings(self , id , name):
        if name == "Piar":
            result = self.cur.execute("SELECT piar_id FROM settings")
            result = bool(len(result.fetchall()))
            if result == False:
                self.cur.execute("INSERT INTO settings (piar_id) VALUES (?)" , (id,))

            else:
                self.cur.execute("UPDATE settings SET piar_id = (?)" , (id,))

            self.connect.commit()                

        elif name == "Nav":
            result = self.cur.execute("SELECT nav_id FROM settings")
            result = bool(len(result.fetchall()))
            if result == False:
                self.cur.execute("INSERT INTO settings (nav_id) VALUES (?)" , (id,))

            else:
                self.cur.execute("UPDATE settings SET nav_id = (?)" , (id,))

            self.connect.commit()

    def settings_data(self , name):
        if name == "Nav":
            result = self.cur.execute("SELECT nav_id FROM settings").fetchone()
            return result[0]
        
        elif name == "Piar":
            result = self.cur.execute("SELECT piar_id FROM settings").fetchone()
            return result[0]
        

    def leaderboard(self , guild):
        result = self.cur.execute("SELECT * FROM users WHERE guild = ?" , (guild,)).fetchall()
        return result
    
    def crime(self , id , win , bool):
        user_money_data = self.cur.execute("SELECT money FROM users WHERE user_id = ?" , (id,)).fetchone()
        user_money = user_money_data[0]
        if bool == True:
            win = user_money + win
            self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?)" , (win , id,))

        else:
            win = user_money - win
            self.cur.execute("UPDATE users SET money = (?) WHERE user_id = (?)" , (win , id,))
        
        self.connect.commit()
        
    def settings(self , guild , command , update):
        if command == "Модерация":
            self.cur.execute("UPDATE settings SET admin_commands = ? WHERE guild = ?" , (update , guild,))
            
        elif command == "Экономика":
            self.cur.execute("UPDATE settings SET economy_commands = ? WHERE guild = ?" , (update , guild,))
            
        elif command == "Музыка":
            self.cur.execute("UPDATE settings SET music = ? WHERE guild = ?" , (update , guild,))
            
        elif command == "Приветствие":
            self.cur.execute("UPDATE settings SET greeting = ? WHERE guild = ?" , (update , guild,))
            
        elif command == "Прощание":
            self.cur.execute("UPDATE settings SET farewell = ? WHERE guild = ?" , (update , guild,))
            
        elif command == "Уровни":
            self.cur.execute("UPDATE settings SET exp = ? WHERE guild = ?" , (update , guild,))
            
        elif command == "Пользовательские команды":
            self.cur.execute("UPDATE settings SET user_commands = ? WHERE guild = ?" , (update , guild,))
            
        elif command == "Комнаты":
            self.cur.execute("UPDATE settings SET rooms = ? WHERE guild = ?" , (update , guild,))
    
        elif command == "id категории":
            self.cur.execute("UPDATE settings SET music_category = ? WHERE guild = ?" , (update , guild,))
            
        self.connect.commit()
        
    def setup_settings(self , guild):
        self.cur.execute("INSERT INTO settings (`guild` , `admin_commands` , `economy_commands` , `greeting` , `farewell` , `exp` , `rooms` , `music_category`) VALUES (? , ? , ? , ? , ? , ? , ? , ?)" , (guild, "False", "False", "False", "False", "False", "False", "None",))
        self.connect.commit()
        
    def check_settings(self , guild):
        result = self.cur.execute("SELECT `guild` FROM `settings` WHERE `guild` = ?" , (guild,))
        return bool(len(result.fetchall()))

    def check_settings_true_module(self , guild , module):
        result = self.cur.execute(f"SELECT {module} FROM settings WHERE `guild` = ?" , (guild,)).fetchone()
        if result:
            if result[0] != "False" or result[0] != "None":
                return True
        
            else:
                return False
        
    def check_id_channel(self , guild , option):
        result = self.cur.execute(f"SELECT {option} FROM `settings` WHERE `guild` = ?" , (guild,)).fetchone()
        if result[0] == "False":
            return "False"
        
        else:
            return result[0]
        
    def command(self , guild , name):
        result = self.cur.execute("SELECT command FROM commands WHERE (guild = ? AND command = ?)" , (guild, name,))
        result = bool(len(result.fetchall()))
        
        if result == False:
            self.cur.execute("INSERT INTO commands (`guild` , `command` , `embed` , `button` , `menu`) VALUES (? , ? , ? , ? , ?)" , (guild, name, "False", "False", "False",))
            self.connect.commit()
            
        else:
            return
        
    def activate(self , guild , command , option):
        if option == "embed":
            self.cur.execute("UPDATE commands SET embed = ? WHERE (guild = ? AND command = ?)" , ("True" , guild , command))
            self.connect.commit()
            
        elif option == "button":
            self.cur.execute("UPDATE commands SET button = ? WHERE (guild = ? AND command = ?)" , ("True" , guild , command))
            self.connect.commit()
            
        elif option == "menu":
            self.cur.execute("UPDATE commands SET menu = ? WHERE (guild = ? AND command = ?)" , ("True" , guild , command))
            self.connect.commit()
            
    def create_button(self , guild , name):
        self.cur.execute("INSERT INTO buttons (`guild` , `command` , `value` , `style` , `action` , `role_id`) VALUES (? , ? , ? , ? , ? , ?)" , (guild, name, "False", "False", "False" , "None"))
        self.connect.commit()
            
    def button(self , guild , name , option , value , role_id = None):
        if option == "value":
            self.cur.execute("UPDATE buttons SET value = ? WHERE (guild = ? AND command = ?)" , (value, guild, name,))
            self.connect.commit()
            
        elif option == "style":
            self.cur.execute("UPDATE buttons SET style = ? WHERE (guild = ? AND command = ?)" , (value, guild, name,))
            self.connect.commit()
            
        elif option == "action":
            if value == "role":
                self.cur.execute("UPDATE buttons SET action = ? WHERE (guild = ? AND command = ?)" , (value, guild, name,))
                self.cur.execute("UPDATE buttons SET role_id = ? WHERE (guild = ? AND command = ?)" , (role_id, guild, name,))
                self.connect.commit()
                
    def create_select(self , guild , name):
        self.cur.execute("INSERT INTO options (`guild` , `command` , `label` , `description` , `action` , `role`) VALUES (? , ? , ? , ? , ? , ?)" , (guild, name, "False", "False", "False" , None))
        self.connect.commit()
            
    def select(self , guild , name , option , value  , role = None):
        if option == "name":
            self.cur.execute("UPDATE options SET label = ? WHERE (guild = ? AND command = ?)" , (value, guild, name,))
            self.connect.commit()
            
        elif option == "description":
            self.cur.execute("UPDATE options SET description = ? WHERE (guild = ? AND command = ?)" , (value, guild, name,))
            self.connect.commit()
            
        elif option == "action":
            if value == "role":
                self.cur.execute("UPDATE options SET action = ? WHERE (guild = ? AND command = ?)" , (role, guild, name,))
                self.connect.commit()
            
    def create_embed(self , guild , name):
        self.cur.execute("INSERT INTO embed (`guild` , `command` , `title` , `description` , `image`) VALUES (? , ? , ? , ? , ?)" , (guild, name, "False", "False", "False"))
        self.connect.commit()

    def embed(self , guild , name , option , value):
        if option == "title":
            self.cur.execute("UPDATE embed SET title = ? WHERE (guild = ? AND command = ?)" , (value, guild, name,))
            self.connect.commit()
            
        elif option == "description":
            self.cur.execute("UPDATE embed SET description = ? WHERE (guild = ? AND command = ?)" , (value, guild, name,))
            self.connect.commit()
            
        elif option == "image":
            self.cur.execute("UPDATE embed SET image = ? WHERE (guild = ? AND command = ?)" , (value, guild, name,))
            self.connect.commit()

    def close(self):
        """Закрывавем соединение с базой данных"""
        self.connect.close()