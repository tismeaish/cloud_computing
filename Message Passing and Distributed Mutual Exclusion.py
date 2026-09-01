client
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(), 12345))
print("Connected to the server. Type 'exit' to disconnect.")
while True:
try:
message = input("Enter message: ")
client_socket.send(message.encode())
if message.lower().strip() == 'exit':
print('Closing connection')
break
response = client_socket.recv(1024).decode()
print(f"Message received: {response}")
except Exception as e:
print(f"Error: {e}")
client_socket.close()

server
import socket
import threading
def handle_client(client_socket, addr):
print(f"Connected to {addr}")
while True:
try:
message = client_socket.recv(1024).decode()
if not message or message.lower().strip() == 'exit':
print(f"Client {addr} disconnected...")
break
response = input(f'Enter message to client {addr}: ')
client_socket.send(response.encode())
except Exception as e:
print(f"Error: {e}")
print(f"Connection closed with {addr}")
client_socket.close()
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 12345))
server_socket.listen()
print("Server is listening...")
while True:
client_socket, addr = server_socket.accept()
client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
client_handler.start()

ricart-agarwala.py
import threading
import time
import random
class Process:
def init (self, id, total_processes):
self.id = id
self.total_processes = total_processes
self.timestamp = 0
self.requested = False
self.reply_count = 0
self.lock = threading.Lock()
self.request_limit = 3 # Limit the number of requests per process
self.request_count = 0 # Count how many requests have been made
def request_critical_section(self):
if self.request_count < self.request_limit:
self.timestamp += 1
self.requested = True
print(f"Process {self.id} requesting critical section at timestamp {self.timestamp}.")
for i in range(self.total_processes):
if i != self.id:
  processes[i].receive_request(self.id, self.timestamp)
while self.reply_count < self.total_processes - 1:
time.sleep(0.1)
self.enter_critical_section()
self.request_count += 1 # Increment the request count
else:
print(f"Process {self.id} has reached its request limit and will terminate.")
def receive_request(self, sender_id, sender_timestamp):
with self.lock:
if self.requested and self.timestamp < sender_timestamp:
print(f"Process {self.id} queuing request from Process {sender_id} at timestamp
{sender_timestamp}.")
return
else:
print(f"Process {self.id} sending reply to Process {sender_id}.")
processes[sender_id].receive_reply(self.id)
def receive_reply(self, sender_id):
with self.lock:
self.reply_count += 1
print(f"Process {self.id} received reply from Process {sender_id}.")
def enter_critical_section(self):
print(f"Process {self.id} entering critical section.")
time.sleep(random.uniform(1, 3)) # Simulate work in critical section
print(f"Process {self.id} exiting critical section.")
self.release_critical_section()
def release_critical_section(self):
self.requested = False
self.reply_count = 0
print(f"Process {self.id} released critical section.")
def process_runner(process):
while process.request_count < process.request_limit:
time.sleep(random.uniform(1, 2))
process.request_critical_section()
num_processes = 5
processes = [Process(i, num_processes) for i in range(num_processes)]
threads = []
for process in processes:
t = threading.Thread(target=process_runner, args=(process,))
threads.append(t)
t.start()
for t in threads:
t.join()
print("All processes have completed their requests.")


