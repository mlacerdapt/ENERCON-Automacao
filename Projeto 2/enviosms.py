from twilio.rest import Client

account_sid = "AC86f33712d5a6f4f21dbbb5db04077957"
auth_token = "a7aead4bf5289c0b7b1c1c555ed1c01e"

try:
    mensagem = cliente.messages.create(
        body="Sua mensagem aqui",
        from_="+14124597153",
        to="+351924089174",
        timeout=30  # Aumenta o tempo limite para 30 segundos
    )
except Exception as e:
    print(f"Erro ao enviar mensagem: {e}")