from flask import Flask,render_template,request

app = Flask (__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    user = request.form.get('user')
    password = request.form.get('password')

    if user == "Alef" and password == "1234":
        return "ACESSO LIBERADO 😁, Aproveite sua aventura!"
    else:
        return "ACESSO NEGADO ❌, tente novamente"
    
if __name__== '__main__':
    app.run("0.0.0.0", port=8000)

