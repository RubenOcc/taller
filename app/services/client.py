from app.repositories.client import ClientRepository

class ClientService:
    @staticmethod
    def register_client(data):
        return ClientRepository.register_client(data)

    @staticmethod
    def get_all_clients():
        return ClientRepository.get_all_clients()
