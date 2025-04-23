from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = '33332008'  # Para usar flash messages

# Configurações do servidor de e-mail (exemplo com Gmail)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'andrelacerda.ti@gmail.com'
app.config['MAIL_PASSWORD'] = 'fcbs imyq ezfc inxl'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "Online"}), 200

@app.route("/email", methods=["GET", "POST"])
def email():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        telefone = request.form["telefone"]
        mensagem = request.form["mensagem"]

        msg = Message(
            subject=f"Cabine037 - Cotação para {nome}",
            sender=app.config['MAIL_USERNAME'],
            recipients=["andrelacerda.ti@gmail.com"],  # quem recebe
            body=f"Nome: {nome}\nEmail: {email}\nTelefone: {telefone}\nMensagem: {mensagem}"
        )
        
        try:
            mail.send(msg)
            return jsonify({"status": "success", "message": "E-mail enviado com sucesso!"})
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
    
if __name__ == '__main__':
    app.run()
