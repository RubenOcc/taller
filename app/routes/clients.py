from flask import Blueprint, jsonify, request
from app.services.client import ClientService

client = Blueprint('client', __name__, url_prefix='/api/client')

@client.route('/register', methods=['POST'])
def register():
    # Obtener los datos del cliente desde la solicitud JSON
    data = request.get_json()
    
    # Llamar al servicio para registrar el cliente
    try:
        # Llamas a ClientService para registrar al cliente
        ClientService.register_client(data)
        return jsonify({'message': 'Cliente registrado correctamente'}), 201
    except Exception as e:
        print(f"Error al registrar cliente: {str(e)}")
        return jsonify({'message': f'Error al registrar cliente: {str(e)}'}), 400

@client.route('/list', methods=['GET'])
def list_clients():
    try:
        # Llamar al servicio para obtener la lista de clientes
        clients = ClientService.get_all_clients()

        # Convertir los objetos Client a un formato JSON adecuado
        clients_list = [{
            'client_id': client.client_id,
            'first_name': client.first_name,
            'last_name_father': client.last_name_father,
            'last_name_mother': client.last_name_mother,
            'phone': client.phone,
            'address': client.address,
            'reference': client.reference,
            'district': client.district,
            'created_at': client.created_at
        } for client in clients]
        print(clients_list)
        return jsonify(clients_list), 200
    except Exception as e:
        return jsonify({'message': f'Error al obtener la lista de clientes: {str(e)}'}), 400