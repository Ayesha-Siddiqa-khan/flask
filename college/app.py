from flask import Flask
from controller.user_controller import Ahmad
app = Flask(__name__)
obj = Ahmad()


@app.route('/user')
def user():
    return obj.asia()





if __name__ == "__main__":
    app.run(debug = True , port = 5000)