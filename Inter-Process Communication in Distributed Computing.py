import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 12345))
while True:
message = input("Send message to server: ")
try:
if message.lower().strip() != 'exit':
client_socket.send(message.encode())
data = client_socket.recv(1024).decode()
print(f"Message received from server: {data}")
else:
break
except ConnectionAbortedError as e:
print(e)
client_socket.close()

import socket
client2.py
server2.py
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 12345))
server_socket.listen()
client_socket, addr = server_socket.accept()
print(f"Connected {client_socket} on {addr}")
while True:
message = client_socket.recv(1024).decode()
try:
if not message:
print("No message received. Client may have closed the connection.")
break
if message.lower().strip() == 'exit':
print("Received 'exit' message. Closing connection.")
break
print(f"Message received from client: {message}")
list1 = message.split()
total_sum = 0
for i in list1:
total_sum += int(i)
response = client_socket.send(str(total_sum).encode())
print(f"Sending data {total_sum} to client")
except ConnectionAbortedError as e:
print(e)
client_socket.close()
server_socket.close()

client2
import socket
import pickle
class DataObject:
def init (self, name, values):
self.name = name
self.values = values
def str (self):
return f"DataObject(name={self.name}, values={self.values})"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 12345))
name = input("Enter name: ")
values = eval(input("Enter list of values: "))
data_to_send = DataObject(name=name, values=values)
print(f"Sending object: {data_to_send}")
serialized_data = pickle.dumps(data_to_send)
client_socket.send(serialized_data)
response = client_socket.recv(1024).decode()
print(f"Received response from server: {response}")
client_socket.close()

server2
import socket
import pickle
class DataObject:
def init (self, name, values):
self.name = name
self.values = values
def str (self):
return f"DataObject(name={self.name}, values={self.values})"
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 12345))
server_socket.listen()
client_socket, addr = server_socket.accept()
print(f"Connected to {addr}")
while True:
try:
received_data = client_socket.recv(1024)
if not received_data:
print("No data received. Closing connection.")
break
data_object = pickle.loads(received_data)
print(f"Received object from client: {data_object}")
total_sum = sum(data_object.values)
response = f"Server: Received {data_object.name}'s data. Sum = {total_sum}"
client_socket.send(response.encode())
except Exception as e:
print(f"Error: {e}")
break
client_socket.close()
server_socket.close()
