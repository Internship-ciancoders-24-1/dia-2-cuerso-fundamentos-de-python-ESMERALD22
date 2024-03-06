
import os
import csv 
from clients.models import Client
class ClientService:
    def __init__(self, table_name):
        self.table_name = table_name

    def get_client(self, client_uid):
        clients = self.list_clients()
        for client in clients:
            if client['uid'] == client_uid:
                return client
        return None
    
    def create_client(self,client):
        with open(self.table_name, mode ='a') as f:
            writer = csv.DictWriter(f, fieldnames= Client.schema())
            writer.writerow(client.to_dict())

    def list_clients(self):
        with open(self.table_name, mode ='r') as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())
            return list(reader)

    def update_client(self, updated_client):
        clients = self.list_clients()
        
        updated_clients = []
        for client in clients:
            if client['uid'] == updated_client.uid:  # Comparando el uid directamente
                updated_clients.append(updated_client.to_dict()) 
            else:
                updated_clients.append(client)

        self._save_to_disk(updated_clients)


    def _save_to_disk(self,clients):
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name, 'w', newline ='') as f:
            writer = csv.DictWriter(f, fieldnames= Client.schema())
            writer.writerows(clients)
    
        if os.path.exists(tmp_table_name):
            os.remove(self.table_name)
            os.rename(tmp_table_name, self.table_name)
        else:
            print("El archivo temporal no existe.")
        

    def delete_client(self, client):
        clients = self.list_clients()
        updated_clients = [c for c in clients if c['uid'] != client['uid']]
        self._save_to_disk(updated_clients)