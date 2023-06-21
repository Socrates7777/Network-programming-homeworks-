
import socket
import threading

quiz_questions = [
    "What is the capital of France?",
    "Who painted the Mona Lisa?",
    "What is the smallest country in the world?",
    "Who won the champions league 2015?",
    "What is the largest planet in our solar system?",
    "What is the deepest lake in the world?"
]

quiz_answers = [
    "Paris",
    "Leonardo da Vinci",
    "Vatican City",
    "Barcelona",
    "Jupiter",
    "Baikal"
]

client_scores = {}

def handle_client(conn, addr):
    
   
    for i in range(len(quiz_questions)):
        conn.sendall(quiz_questions[i].encode())
        answer = conn.recv(1024).decode()
        
       
        if answer == quiz_answers[i]:
            if addr in client_scores:
                client_scores[addr] += 1
            else:
                client_scores[addr] = 1
    
    final_score = f"Your final score is {client_scores[addr]} out of {len(quiz_questions)}"
    conn.sendall(final_score.encode())
    
    
    conn.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen(5)
print("Server got started on http//localhost:5000 and waiting..")

while True:
    
    conn, addr = server_socket.accept()
    
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
