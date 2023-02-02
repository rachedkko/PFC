from _thread import*
import socket
import pickle
from game import Game

server="localhost"
port=10
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    print(e)


s.listen()
print("J'attend une connexion, Dresseur de Pokémon")


connected=set()
games={}
idCount=0
def threaded_client(conn,p,gameId):
    global idCount
    conn.send(str.encode(str(p)))


    reply= ""
    while True:

        try:

            data= conn.recv(2048*10).decode()

            if gameId in games:
                game=games[gameId]

                if not data:
                    break
                else:
                    if data=="reset":
                        game.resetMove()
                    elif data != "get":
                        game.play(p,data)
                    reply=game
                    conn.sendall(pickle.dumps(reply))
            else:
                break

        except:
            break

    print("lost connexion")

    try:
        del games[gameId]
        print("closing game n " + gameId)
    except:
        pass
    idCount-=1
    conn.close()

while True:
    conn,addr=s.accept()
    print("Connected to ",addr)
    idCount+=1
    p=0
    gameId=(idCount-1)//2
    if idCount%2==1:
        games[gameId]=Game(gameId)
        print("Nouveau Jeu crée")
    else:
        games[gameId].ready=True
        p=1
    start_new_thread(threaded_client,(conn,p,gameId))
