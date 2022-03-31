import objects
import os
from flask import Flask, request, jsonify, flash, redirect, url_for, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "./recu"

CORS(app)

users = []
medicines = []
FILE=0




@app.route("/", methods=['GET', 'POST'])
def upload_file():
    return render_template('home.html')

@app.route("/uploader", methods=['GET', 'POST'])
def uploadader():
    if request.method == "POST":
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER', filename]))

        return "Archivo subido exitosamente"
    



@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    first_name = data["first_name"]
    last_name = data["last_name"]
    date = data["date"]
    gender = data["gender"]
    nickname = data["nickname"]
    password = data["password"]
    phone = data["phone"]
    valid_user = True
    for user in users:
        if user.nickname == nickname:
            valid_user = False
    if valid_user:
        users.append(objects.User(first_name, last_name,
                                  date, gender, nickname, password, phone))
        return jsonify(request.get_json()), 200
    else:
        return jsonify({"message": "nickname repeated"}), 400


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    nickname = data["nickname"]
    password = data["password"]
    for user in users:
        if user.nickname == nickname:
            if user.password == password:
                return jsonify({
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "date": user.date,
                    "gender": user.gender,
                    "nickname": user.nickname,
                    "password": user.password,
                    "phone": user.password
                }), 200
            else:
                return jsonify({"message": "bad credentials"}), 400
    return jsonify({"message": "bad credentials"}), 400





