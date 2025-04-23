from flask import Flask, request, jsonify
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json

    nome = data.get('nome')
    email_remetente = data.get('email')
    telefone = data.get('telefone')
    mensagem = data.get('mensagem')

    msg = EmailMessage()
    msg['Subject'] = f'Nova mensagem de {nome}'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS  # Pode ser um e-mail fixo seu
    msg.set_content(f"Nome: {nome}\nEmail: {email_remetente}\nTelefone: {telefone}\nMensagem:\n{mensagem}")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return jsonify({"status": "success", "message": "E-mail enviado com sucesso!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
if __name__ == '__main__':
    app.run()
