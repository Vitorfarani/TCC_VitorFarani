from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

# Configure sua chave da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/calcular-pf", methods=["POST"])
def calcular_pf():
    data = request.get_json()
    descricao = data.get("descricao")

    # Simulação de cálculo (depois vamos usar a OpenAI aqui)
    palavras = descricao.split()
    pontos = len(palavras) * 2  # Exemplo simples: 2 PF por palavra

    return jsonify({"pontos_de_funcao": pontos})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
