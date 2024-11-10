from flask import Flask
from controller. user_controller import China
app = Flask(__name__)
obj = China()

@app.route("/home")
def home():
    return obj.user_signup()









































































if __name__ == '__main__':
    app.run(debug=True)