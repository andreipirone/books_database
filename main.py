from flask import Flask, render_template, url_for, redirect, request
from biblioteca import BibliotecaCarti

app = Flask(__name__)
app.secret_key = 'phi'

db = BibliotecaCarti('carti.db')
db.init_db()

@app.route('/')
def index():
	lista = db.read_all()
	return render_template('index.html', lista=lista)

@app.route('/delete/<int:id>')
def delete(id):
	db.delete(id)
	return redirect(url_for('index'))

@app.route('/create', methods=['GET', 'POST',])
def create():
	return render_template('create.html')

@app.route('/generate', methods=['POST',])
def generate():
	titlu  = request.form['titlu']
	autor   = request.form['autor']
	editura = request.form['editura']
	db.create(titlu,autor,editura)
	return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit(id):
	lista = db.read_one(id)
	return render_template('edit.html', lista=lista)

@app.route('/change', methods=['POST',])
def change():
	titlu  = str(request.form['titlu'])
	autor   = str(request.form['autor'])
	editura = str(request.form['editura'])
	id   	= str(request.form['id'])
	db.update(id,titlu,autor,editura)
	return redirect(url_for('index'))
	
if __name__ == '__main__':
	app.run()
