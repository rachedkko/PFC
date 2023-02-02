import pygame
from network import Network
import pickle
import sys
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.5)
bul=pygame.mixer.Sound("bulbizarre.ogg")
car=pygame.mixer.Sound("carapuce.ogg")
sal=pygame.mixer.Sound("salameche.ogg")
clock=pygame.time.Clock()
w=500
h=500

screen=pygame.display.set_mode((w,h))
pygame.display.set_caption("PFC Pokémon")


class Bouton():
    def __init__(self,s,x,y,text):
        self.image=s
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.text=text
    def click(self,pos):
        pass

Pierre=Bouton(pygame.transform.scale(pygame.image.load("carapuce.png").convert_alpha(),(153,189)),173.5,300,"R")
Papier=Bouton(pygame.transform.scale(pygame.image.load("bulbizarre.png").convert_alpha(),(153,189)),20.5,300,"P")
Ciseau=Bouton(pygame.transform.scale(pygame.image.load("salameche.png").convert_alpha(),(153,189)),326.5,300,"S")
boutons=[]

boutons.append(Pierre)
boutons.append(Papier)
boutons.append(Ciseau)
play=True
n=Network()
player=int(n.getP())

run=True
start = False
clicked=True
myscore=0
yourscore=0
while run:


    clock.tick(60)




    try:
        game=n.send("get")
    except:

        run=False
        break

    if not game.connected():
        start=False
        font=pygame.font.Font("Pokemon Classic.ttf",20)
        text = font.render("On attend l'autre joueur ptn !", 1, (255, 0, 0))
        text1 = font.render(("T'es le joueur "+str(player+1)), 1, (255, 0, 0))
        screen.blit(text,((w-text.get_width())/2,(h-text.get_height())/2))
        screen.blit(text1, ((w - text1.get_width()) / 2, (h - text1.get_height()) / 2-25))
        pygame.display.update()
    else:
        if play:
            pygame.mixer.music.play(1)
            play=False
        start=True

    if start:

        screen.blit(pygame.transform.scale(pygame.image.load("fond.jpg").convert(), (500, 500)), (0, 0))
        for e in boutons:

            screen.blit(e.image,e.rect)

        screen.blit(pygame.transform.scale(pygame.image.load("ball.png").convert_alpha(),(210,210)),(145,50))
        font1=pygame.font.Font("Pokemon Classic.ttf",40)
        text = font1.render(str(myscore), 1, (0,0,0))
        text2 = font1.render(str(yourscore), 1, (0,0,0))
        screen.blit(text,(0+5,0))
        screen.blit(text2,(495-text2.get_width(),0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONUP:
            if event.button==1:
                for e in boutons:
                    if pygame.Rect.collidepoint(e.rect,pygame.mouse.get_pos()) and game.connected() and clicked:
                        if e.text=="R":
                            e.image=pygame.transform.scale(pygame.image.load("c.png").convert_alpha(),(153,189))
                            car.play()
                        elif e.text=="P":
                            e.image = pygame.transform.scale(pygame.image.load("b.png").convert_alpha(), (153, 189))
                            bul.play()
                        elif e.text == "S":
                            e.image = pygame.transform.scale(pygame.image.load("s.png").convert_alpha(), (153, 189))
                            sal.play()
                        if player==0:
                            if not game.p1move:
                                n.send(e.text)
                        else:
                            if not game.p2move:
                                n.send(e.text)
                        clicked=False






    if game.bothMove():
        pygame.time.delay(300)
        win=game.winner()

        font=pygame.font.Font("Pokemon Classic.ttf",27)
        start=False
        if (win==1 and player==1) or  (win==0 and player==0) :
            text=font.render("T'as gagné gg !",1,(0,0,0))
            myscore+=1
        elif win==-1:
            text = font.render("Egalité !", 1, (0,0,0))
        else:
            text = font.render("T'as perdu mskn !", 1, (0,0,0))
            yourscore+=1
        screen.blit(text,((w - text.get_width()) / 2,0))
        pygame.display.update()
        pygame.time.delay(1500)
        try:
            n.send("reset")
            boutons=[]
            Pierre = Bouton(pygame.transform.scale(pygame.image.load("carapuce.png").convert_alpha(), (153, 189)),
                            173.5, 300, "R")
            Papier = Bouton(pygame.transform.scale(pygame.image.load("bulbizarre.png").convert_alpha(), (153, 189)),
                            20.5, 300, "P")
            Ciseau = Bouton(pygame.transform.scale(pygame.image.load("salameche.png").convert_alpha(), (153, 189)),
                            326.5, 300, "S")
            boutons.append(Pierre)
            boutons.append(Papier)
            boutons.append(Ciseau)
            truebut = boutons.copy()
            clicked=True
        except:
            run=False
          
            break
    pygame.display.update()