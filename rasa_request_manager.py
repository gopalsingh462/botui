import requests
import config


def send_request_to_rasa(msg):
    payload = {"text": msg}
    headers = {'content-type': 'application/json'}
    response = requests.post(config.rasa_server_url, json=payload, headers=headers)
    result = response.json()
    return result


def get_intent_from_rasa_response(response):
    intent = response['intent']['name']
    return intent


def get_entities_from_rasa_response(response):
    entities = response['entities']
    return entities


def get_entity_name_value_from_entity(entity):
    return entity['entity'], entity['value']
