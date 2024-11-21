from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector

app = Flask(__name__)

# Conexión a la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",         
    password="",  
    database="capesa"
)
cursor = db.cursor(dictionary=True)

# Carrito en memoria (puede mejorarse con sesiones o base de datos)
carrito = []

@app.route('/')
def index():
    # Obtener productos de la base de datos
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    return render_template('index.html', productos=productos)

@app.route('/agregar_al_carrito', methods=['POST'])
def agregar_al_carrito():
    producto_id = int(request.form['producto_id'])
    cantidad = int(request.form['cantidad'])

    # Obtener información del producto
    cursor.execute("SELECT * FROM productos WHERE id = %s", (producto_id,))
    producto = cursor.fetchone()

    if producto:
        # Agregar al carrito
        carrito.append({
            "id": producto["id"],
            "nombre": producto["nombre"],
            "precio": producto["precio"],
            "cantidad": cantidad
        })
    return redirect(url_for('ver_carrito'))

@app.route('/carrito')
def ver_carrito():
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    return render_template('carrito.html', carrito=carrito, total=total)

@app.route('/eliminar_del_carrito/<int:producto_id>')
def eliminar_del_carrito(producto_id):
    global carrito
    carrito = [item for item in carrito if item["id"] != producto_id]
    return redirect(url_for('ver_carrito'))

@app.route('/finalizar_compra')
def finalizar_compra():
    if not carrito:
        return "El carrito está vacío", 400

    # Aquí podrías implementar lógica para guardar la compra en la base de datos.
    carrito.clear()
    return "¡Compra finalizada con éxito! Si necesita mas ayuda (https://wa.me/3137755038)"

if __name__ == '__main__':
    app.run(debug=True)
