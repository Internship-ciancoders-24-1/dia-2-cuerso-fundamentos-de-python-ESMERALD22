import sys

clients = [
    {
        'nombre': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'SOftware engineer'
    },
    {
        'nombre': 'Ricardo',
        'company': 'Facebook',
        'email': 'ricardo@facebook.com',
        'position': 'Data engineer'
    },

]

def crear_cliente(client):
    global clients
    if client not in clients:
        clients.append(client) 
    else:
        print(' already exists the client')

def list_clients():
    for idx, client in enumerate(clients):
        print('{uid}| {name}| {company}|{email}|{position}'.format(
            uid= idx,
            name=client['nombre'],
            company=client['company'],
            email=client['email'],
            position=client['position']
        ))

def update_client( client_name, clientUpdate):
    global clients
    e = False
    for client in clients:
            if(client['nombre'] == client_name):
                client['nombre'] = clientUpdate['nombre']
                client['company'] = clientUpdate['company']
                client['email'] = clientUpdate['email']
                client['position'] = clientUpdate['position']
                print('Client updated')
                e = True
                break
            else:
                continue
    
    if(e == False):
        print('Client does not exist')
       
def delete_client(client_name):
    global clients
    e= False
    for client in clients:
            if(client['nombre'] == client_name):
                clients.remove(client)
                print('Client deleted')
                e = True
                break
    if(e == False):
        print('Client does not exist')

def search_client(client_name):
    global clients
    e= False
    for client in clients:
            if(client['nombre'] == client_name):
                print(client)
                e = True
                break
    return e
def _print_wlecom():
    print('BIENVENIDOS A PLATZI VENTAS')
    print ('*'*50)
    print ('What would you like to do today? ')
    print ('[C]reate client')
    print ('[U]pdate client')
    print ('[D]eleate client')
    print ('[S]earch client')

def _get_client_field(field_name):
    field = None 
    while not field:
        field = input ('What is the client {}'. format(field_name))
    return field

def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('WHat is the client name? ')
        
        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
            sys.exit()
    
    return client_name
    
# punto de entrada, comienza código
if __name__ == '__main__':
    _print_wlecom()
    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'nombre': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        crear_cliente(client)
        list_clients()

    elif command == 'D':
        client_name= _get_client_name()
        delete_client(client_name)
        list_clients()

    elif command == 'U':
        client_name = input('WHat is the client name? ')
        client = {
            'nombre': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        update_client(client_name,client)
        list_clients()

    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('THe client is in the client\'s list')
        else:
            print('The client: {} is not in the client\'s list '.format(client_name))

    else:
        print('invalid command')
        
