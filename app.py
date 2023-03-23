from flask import Flask,render_template

app=Flask(__name__)
app.secret_keys='llavesecreta'

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

if __name__ == '__main__':
    app.run(port=3000,debug=True)