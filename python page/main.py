from flask import Flask, render_template, request
import random

app = Flask(__name__)

facts_list = [
    "La tecnología puede ser muy útil, pero es importante usarla con moderación.",
    "Tomar descansos de las pantallas puede ayudar a reducir el estrés.",
    "Pasar tiempo con familiares y amigos puede ayudar a reducir la dependencia tecnológica.",
    "Los videojuegos y las redes sociales pueden hacer que pasemos demasiado tiempo frente a una pantalla.",
    "Es importante tener actividades que no dependan de la tecnología."
]


@app.route("/", methods=["GET", "POST"])
def inicio():
    resultado = ""

    if request.method == "POST":
        num1 = int(request.form.get("num1"))
        num2 = int(request.form.get("num2"))
        op = request.form.get("operacion")

        if op == "suma":
            resultado = num1 + num2

        if op == "resta":
            resultado = num1 - num2

        if op == "multi":
            resultado = num1 * num2

        if op == "division":
            resultado = num1 / num2

    return render_template("index.html", resultado=resultado)


@app.route("/random_fact")
def random_fact():
    fact = random.choice(facts_list)
    return render_template("random_fact.html", fact=fact)


app.run(debug=True)
