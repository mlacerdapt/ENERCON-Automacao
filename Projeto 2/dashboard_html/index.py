from flask import Flask, render_template

app = Flask(__name__)

#Criar a 1ªpagina do site

    #route -> o caminho depois do dominio

    #função -> o que vc quer exibir naquela pagina
@app.route("/")
def homepage():
    return "Esse é o meu primeiro site vamos mudar algumas coisas "

@app.route("/contatos")
def contatos():
    return "Nossos contatos são: email:123@gmail.com telefone: (21)9999-9999"

# Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
