import rasa_request_manager


def get_message_from_intent(intent, entities):
    if intent == '':
        entity = entities[0]
        name, value = rasa_request_manager.get_entity_name_value_from_entity(entity)
        return 'you want to perform "' + intent + '" with this param "' + name + '" with value "' + value+'"'
