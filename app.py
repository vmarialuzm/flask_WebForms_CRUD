from flask import Flask,render_template,flash,redirect,url_for
from config import Config
from admin.loginForm import LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
app.config.from_object(Config)

db=SQLAlchemy(app)
migrate=Migrate(app,db)

@app.route('/')
def index():
    return render_template("index.html")
    #return 'Hola'

@app.route('/cliente')
def index_cliente():
    data=["Jorge","Curioso","Bob"]
    return render_template("/cliente/index.html",lista=data)

@app.route('/cliente/add')
def add_cliente():
    return render_template("/cliente/add.html")

@app.route('/usuario')
def index_usuario():
    data=["Hugo","Paco","Luis"]
    return render_template("/usuario/index.html",lista=data)

@app.route('/usuario/add')
def add_usuario():
    return render_template("/usuario/add.html")

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm() #instanciando un objeto
    if form.validate_on_submit():
        flash('Inicio de sesión solicitada por {}, ¿Recordar?={}'.format(
            form.username.data,form.remember_me.data))
        return redirect(url_for('index_css'))
    
    return render_template('login.html',form=form)

@app.route('/css')
def index_css():
    return render_template('indexCss.html')

if __name__ == '__main__':
    app.run(port=3000,debug=True)