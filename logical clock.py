lamport clock
class LamportClock:
def init (self, process_id):
self.process_id = process_id
self.clock = 0
def event(self):
self.clock += 1
print(f"Process {self.process_id} - Internal event with Timestamp {self.clock}")
def send_message(self, receiver):
self.clock += 1
print(f"Process {self.process_id} sends a message to Process {receiver.process_id} with
Timestamp {self.clock}")
receiver.receive_message(self.process_id, self.clock)
def receive_message(self, sender_id, sender_timestamp):
self.clock = max(self.clock, sender_timestamp) + 1
print(f"Process {self.process_id} received a message from Process {sender_id} with updated
Timestamp {self.clock}")
process1 = LamportClock(1)
process2 = LamportClock(2)
process1.event()
process1.send_message(process2)
process2.event()
process2.send_message(process1)

vector clock
class VectorClock:
def init (self, process_id, num_processes):
self.process_id = process_id
self.num_processes = num_processes
self.vector = [0] * num_processes
def event(self):
self.vector[self.process_id] += 1
print(f"Process {self.process_id} - Internal event with Updated Vector {self.vector}")
def send_message(self, receiver):
self.vector[self.process_id] += 1
print(f"Process {self.process_id} sends a message to Process {receiver.process_id} with
Updated Vector {self.vector}")
receiver.receive_message(self.process_id, self.vector)
def receive_message(self, sender_id, sender_vector):
for i in range(self.num_processes):
self.vector[i] = max(self.vector[i], sender_vector[i]) + 1
self.vector[self.process_id] += 1
print(f"Process {self.process_id} received a message from Process {sender_id} with Updated
Vector {self.vector}")
# Create Processes
process1 = VectorClock(0, 3)
process2 = VectorClock(1, 3)
process3 = VectorClock(2, 3)
# Simulate Events
process1.event()
process1.send_message(process2)
process2.event()
process2.send_message(process3)
process3.send_message(process1)
