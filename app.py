from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nome")
        finalidade = request.form.get("finalidade")
        peso = int(request.form.get("peso"))
        dias_treino = int(request.form.get("dias_treino"))
        minutos_treino = float(request.form.get("minutos_treino"))

        perda_peso = (peso * 2 / 100) + (dias_treino * minutos_treino)

        return render_template("index.html", resultado=perda_peso, nome=nome, finalidade=finalidade)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)