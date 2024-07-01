# app.py

from flask import Flask, render_template, request, redirect, url_for
from models import Roupa

app = Flask(__name__)

# Lista global para armazenar roupas
roupas = []

@app.route('/')
def index():
    return render_template('index.html', roupas=roupas)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_roupa():
    if request.method == 'POST':
        nome = request.form['nome']
        categoria = request.form['categoria']
        tamanho = request.form['tamanho']
        
        nova_roupa = Roupa(nome, categoria, tamanho)
        roupas.append(nova_roupa)
        return redirect(url_for('index'))
    
    return render_template('add_item.html')

if __name__ == '__main__':
    app.run(debug=True)

