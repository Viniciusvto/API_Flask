from flask import Flask, jsonfy # essa bilioteca converte dicionarios e objetos python em respostas json

#vou criar uma instancia da aplicação Flask
app = Flask(__name__)

#defino uma rota para a aplicação
@app.route('/') # é a rota é o endereço que o usuário vai acessar para ver a resposta da aplicação
def home():
    #jsonfy transforma um dicionario python no formato json
    return jsonfy({
        "mensagem": "API de fatos Historicos ativa!",
        "status": "sucesso"
    })

#executa o servidor apenas se o arquivo for executado diretamente
if __name__ == '__main__':
    app.run(debug=True) #debug=True significa que o servidor vai reiniciar automaticamente quando houver alterações no código
