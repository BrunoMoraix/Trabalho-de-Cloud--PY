import sqlite3
from flask import Flask, request, jsonify

app_contatos = Flask(__name__)

def get_db():
    db = sqlite3.connect('contatos.db')
    db.execute('CREATE TABLE IF NOT EXISTS contatos (id INTEGER PRIMARY KEY, nome TEXT NOT NULL, telefone TEXT NOT NULL, email TEXT NOT NULL)')
    return db

@app_contatos.route('/contatos', methods=['POST'])
def adicionar_contato():
    data = request.json
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)', (data['nome'], data['telefone'], data['email']))
    db.commit()
    return jsonify({'id': cursor.lastrowid}), 201

@app_contatos.route('/contatos', methods=['GET'])
def listar_contatos():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM contatos')
    contatos = [{'id': row[0], 'nome': row[1], 'telefone': row[2], 'email': row[3]} for row in cursor.fetchall()]
    return jsonify(contatos)

if __name__ == '__main__':
    app_contatos.run(port=5000)