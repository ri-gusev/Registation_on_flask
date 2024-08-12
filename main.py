from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['Post','Get'])
def index():
    courses = ['Математика','Русский язык','Информатика','Биология','Химия']
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        surname = request.form.get('surname')
        courses = request.form.get('courses')
        gender = request.form['options']
        agree = request.form.get('agree')
        return render_template('result.html', email=email,courses=courses,password=password,name=name,surname=surname,gender=gender,agree=agree)
    return render_template('form.html',courses=courses)

app.run(debug=True)
