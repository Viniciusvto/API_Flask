from datetime import datetime
from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"mensagem": "API ativa!", "status": "sucesso"})


@app.route("/fatos/hoje")
def fatos_hoje():
    agora = datetime.now()
    dia = agora.day
    mes = agora.month

    url = f"https://en.wikipedia.org/api/rest_v1/feed/onthisday/events/{mes}/{dia}"
    headers = {"User-Agent": "MinhaApiDeFatosHistoricos/1.0"}

    try:
        resposta = requests.get(url, headers=headers)
        if resposta.status_code == 200:
            dados = resposta.json()
            eventos_brutos = dados.get("events", [])

            eventos_formatados = []
            for item in eventos_brutos[:1]:
                eventos_formatados.append(
                    {"ano": item.get("year"), "fato": item.get("text")}
                )

            return jsonify(
                {
                    "data": f"{dia:02d}/{mes:02d}",
                    "total_fatos": len(eventos_formatados),
                    "fatos": eventos_formatados,
                }
            )
        else:
            return jsonify({"erro": "Falha ao buscar dados"}), 500
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
