import requests
from bottle import (
    run, post, response, request as bottle_request
)

BOT_URL = 'https://api.telegram.org/bot1253996436:AAGrpiWPb7pBDKy3ejZsTIyRBiJ-MqYe5tM/'

def get_chat_id(data):
    chat_id = data['message']['chat']['id']

    return chat_id

def get_message(data):
    message_text = data['message']['text']
    return message_text

def send_message(prepared_data):
    message_url = BOT_URL + 'sendMessage'
    requests.post(message_url, json=prepared_data)

def change_text_message(text):
    return text[::-1]

def prepare_data_for_answer(data):
    answer = change_text_message(get_message(data))

    json_data = {
        "chat_id": get_chat_id(data),
        "text": answer,
    }

    return json_data


@post('/')
def main():
    data = bottle_request.json
    
    answer_data = prepare_data_for_answer(data)
    send_message(answer_data)

    return response


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)