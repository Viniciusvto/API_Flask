from datetime import datetime  # pega a data e hora atual
from flask import (
    Flask,
    render_template,
)  # cria a API e retorna os dados em formato JSON
import requests  # faz requisições HTTP para buscar dados de uma API externa

app = Flask(__name__)  # cria a instância da aplicação Flask


@app.route("/")  # eota para buscar fatos históricos do dia atual
def fatos_hoje():  # cria a função que trata a rota de fatos históricos do dia atual
    agora = datetime.now()  # define a variável agora como a data e hora atual
    dia = agora.day  # define a variável dia como o dia atual
    mes = agora.month  # define a variável mes como o mês atual

    url = f"https://pt.wikipedia.org/api/rest_v1/feed/onthisday/events/{mes}/{dia}"  # define a variável url como a URL da API externa que retorna fatos históricos do dia atual
    headers = {
        "User-Agent": "MinhaApiDeFatosHistoricos/1.0"
    }  # me identifica para a API externa que estou fazendo a requisição

    try:  # faz a requisição para a API externa e trata a resposta
        resposta = requests.get(
            url, headers=headers
        )  # faço uma requisição GET para a URL enviando juntos os dados que me identificam
        if (
            resposta.status_code == 200
        ):  # se a resposta for bem sucedida (código 200), então pego os dados retornados
            dados = (
                resposta.json()
            )  # converto os dados retornados em formato JSON para um dicionário Python
            eventos_brutos = dados.get(
                "events", []
            )  # pego a lista de eventos históricos do dicionário retornado, se não houver eventos, retorna uma lista vazia

            eventos_formatados = (
                []
            )  # cria uma lista vazia para armazenar os eventos formatados
            for item in eventos_brutos[
                :2
            ]:  # percorro a lista de eventos históricos, mas pego apenas os dois primeiros eventos ([:2]) para não sobrecarregar a resposta da API
                eventos_formatados.append(  # acresenta eventos formatados na lista de eventos formatados
                    {
                        "ano": item.get("year"),
                        "fato": item.get("text"),
                    }  # acresenta o ano e o fato histórico do evento no dicionário que será retornado na resposta da API
                )

            return render_template(
                "fatos.html",
                data=f"{dia:02d}/{mes:02d}",
                total_fatos=len(eventos_formatados),
                fatos=eventos_formatados,
            )

        else:
            return render_template("erro.html", mensagem="Falha ao buscar dados"), 500
    except Exception as e:
        return render_template("erro.html", mensagem=str(e)), 500


if __name__ == "__main__":
    app.run(debug=True)
