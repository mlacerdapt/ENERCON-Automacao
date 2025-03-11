import requests
import socket

socket.setdefaulttimeout(10)  # Tempo limite de 10 segundos
socket.getaddrinfo = lambda *args, **kwargs: [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]


from deep_translator import LingueeTranslator

traducao = LingueeTranslator(source="english", target="portuguese").translate("Hello, how are you?")
print(traducao)
