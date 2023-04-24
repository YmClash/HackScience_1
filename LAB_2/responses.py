import random


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'Hello':
        return 'hey'

    if p_message =='roll':
        return str(random.randint(1,6))

    if p_message == 'je suis la':
        return "ou sa ???"