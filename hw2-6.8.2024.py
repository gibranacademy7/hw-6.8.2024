def perform_action(action):
    match action:
        case 'add':
            return 'Adding item'
        case 'delete':
            return 'Deleting item'
        case 'update':
            return 'Updating item'
        case _:
            return 'Unknown action'

result = perform_action('add')
print(result)
#-------------------------: # using 'dict' instead 'mach case':

def perform_action(action):
    actions_dict = {
        'add': 'Adding item',
        'delete': 'Deleting item',
        'update': 'Updating item',
        '_': "Unknown action"
    }
    return actions_dict.get(action, 'Unknown action');

result = perform_action('add');
print(result);
