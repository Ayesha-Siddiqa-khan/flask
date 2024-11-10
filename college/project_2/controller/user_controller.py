import mysql.connector
class China():
    def __init__ (self):
        try:
            self.con = mysql.connector.connect(host = "localhost", user = "root", password = "qwerty.",database = "flask_learing")
            self.cur = self.con.cursor(dictionary=True)
            
            print("your connection is connected")
        
        except:
            print("connection is denied")    
           
   
    def user_signup(self):
         self.cur.execute("SELECT * FROM flask_learing.users")
         result = self.cur.fetchall()
        
         return result