import pickle
import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9987
serversocket.bind((host, port))
serversocket.listen()
print(f"Serve listening on port {port}")
while True:
    clientsocket, addr = serversocket.accept()
    print(f"Go to conect from {addr}")
    receblista = clientsocket.recv(1024)
    lista = pickle.loads(receblista)
    peso = lista[0]
    altura = lista[1]
    imc = int(peso)/pow(float(altura), 2)
    envia = pickle.dumps(imc)
    clientsocket.send(envia)
    lista.clear()
    clientsocket.close()
