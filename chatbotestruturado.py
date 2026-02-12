import re
import random
import time

# Função para simular digitação

def digitar(texto):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(0.04)
    print()

# Lembrar a conversa

ultimo_assunto = None
 

# Função principal de resposta

def responder(entrada):
    global ultimo_assunto

    respostas_ola = [
        "Olá! Como posso ajudar você hoje?",
        "Oi! Em que posso te ajudar?",
        "E aí! Tudo bem? 😊"
    ]

    if re.search(r"\b(olá|oi|ola|oii|eai)\b", entrada):
        ultimo_assunto = "saudacao"
        return random.choice(respostas_ola)

    elif re.search(r"\b(fome|comida|alimento|comer)\b", entrada):
        ultimo_assunto = "comida"
        return "Você prefere doce ou salgado?"

    elif ultimo_assunto == "comida" and re.search(r"\b(doce)\b", entrada):
        return "Que tal um bolo de chocolate? 🍫"

    elif ultimo_assunto == "comida" and re.search(r"\b(salgado)\b", entrada):
        return "Que tal uma coxinha ou uma pizza? 🍕"

    return "Desculpe, não entendi. Pode reformular sua pergunta?"


# Início do chatbot

nome = input("Chatbot: Olá! Qual é o seu nome? ")
digitar(f"Chatbot: Prazer em conhecê-lo, {nome}!")
digitar("Digite 'sair' para encerrar a conversa.\n")


# Loop principal

while True:
    entrada_usuario = input("Você: ").lower()

    if entrada_usuario == "sair":
        digitar("Chatbot: Me chame se precisar de ajuda novamente. Até mais!")
        break

    digitar("Chatbot está pensando...")
    resposta = responder(entrada_usuario)
    digitar(f"Chatbot: {resposta}")
    
