from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess
import shlex
import socket

def index(request):
    
    # process = subprocess.Popen(
    #     # shlex.split("nc -n -v localhost 10000 < 'test'"),
    #     shlex.split("ls"), 
    #     stdin=subprocess.PIPE, 
    #     stdout=subprocess.PIPE, 
    #     stderr=subprocess.PIPE, 
    #     text=True
    # )
    # process.wait()
    # output = process.stdout.read()

    # json = {
    #     "data": output.strip()
    # }


    TCP_IP = 'localhost'
    TCP_PORT = 10000
    BUFFER_SIZE = 1024
    MESSAGE = "Hello, World Test!".encode()
     
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_client.connect((TCP_IP, TCP_PORT))
    socket_client.send(MESSAGE)
    data = socket_client.recv(BUFFER_SIZE)

    socket_client.close()


    # socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # # Connect the socket to the port where the server is listening
    # server_address = ('localhost', 10000)
    # socket_client.connect(server_address)

    # try:
    #     # Send data
    #     message = 'Message: [DATA]'
    #     socket_client.sendall(message)

    #     # Look for the response
    #     amount_received = 0
    #     amount_expected = len(message)
        
    #     while amount_received < amount_expected:
    #         data = socket_client.recv(1000)
    #         amount_received += len(data)

    # finally:
    #     socket_client.close()


    json = {
        "data": data.decode("utf-8"),
    }
    
    return JsonResponse(json, safe=False)

def show(request, id):
    json = {
        "id": id,
        "name":"John Doe",
        "number": "0000 0000 0000 0000 0000 0000",
    }
    return JsonResponse(json, safe=False)

@csrf_exempt
def create(request):
    data = {
        "name": request.POST["name_2"],
        "number": request.POST["number"],
    }
    return JsonResponse(data, safe=False)
        
@csrf_exempt
def update(request, id):
    data = {
        "id": id,
        "name": request.POST["name"],
        "number": request.POST["number"],
    }
    return JsonResponse(data, safe=False)

@csrf_exempt
def delete(request, id):
    data = {
        "id": id,
        "name": request.POST["name"],
        "number": request.POST["number"],
    }
    return JsonResponse(data, safe=False)
