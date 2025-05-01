from flask import Flask
import sys
sys.path.append(r"D:\program\program")
from my_app import page
app=Flask(__name__)
app.register_blueprint(page.dp)
if __name__ == "__main__":
    app.run(debug=True)