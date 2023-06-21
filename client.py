import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))


for i in range(6):
    question = client_socket.recv(1024).decode()
    print(question)
    answer = input("Answer: ")
    client_socket.sendall(answer.encode())


final_score = client_socket.recv(1024).decode()
print(final_score)


client_socket.close()
