from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/infor')
def infor(): 
    return render_template('infor.html')

@app.route('/saludo')
def saludo(): 
    return render_template('saludo.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        print(f'Recibido: Nombre={name}, Email={email}') 
        return f'Bienvenido, {name} ({email}), Gracias por estar Visitando Nuestra Pagina... "TE ESPERAMOS PRONTO"'
    



if __name__ == '__main__': 
    app.run(debug=True) 

 