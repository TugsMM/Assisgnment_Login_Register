from flask_app import app
from flask_app.controllers import users_controller
            
if __name__ == "__main__":
    app.run(debug=True,port=5001,host="0.0.0.0")