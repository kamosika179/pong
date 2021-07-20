# -*- coding: utf-8 -*-

import pygame
import sys
from pygame.locals import *
from model import Model

WIN_SIZE = (700,800)
WIN_TITLE = "break_block"
class View:
    def __init__(self,screen):
        #この辺はサンプルコードまるパクリです
        self.screen = screen
        #どの画面を表示するか決める。
        self.now_screen = "title"
        self.sprites = {}
        self.sprites["bar"] = pygame.image.load("sprites/bar.png")
        self.sprites["ball"] = pygame.image.load("sprites/ball.png")
        #self.sprites["block"] = pygame.image.load("block.png")
        #self.sprites["special_block"] = pygame.image.load("special_block.png")
        #self.sprites["speed_item"] = pygame.image.load("speed_item.png")
        #self.sprites["clone_item"] = pygame.image.load("clone_item.png")
        #self.sprites["bigger_item"] = pygame.image.load("bigger_item.png")
        #play画面では使わなそうなもの
        self.sprites["title"] = pygame.image.load("sprites/title.png")
        #self.sprites["stageclear"] = pygame.image.load("stageclear.png")
        #self.sprites["gameover"] = pygame.image.load("gameover.png")
        self.sprites["start"] = pygame.image.load("sprites/start.png")
        self.sprites["score"] = pygame.image.load("sprites/score.png")
        #self.sprites["retry_button"] = pygame.image.load("retry_button.png")
        #self.sprites["exit_button"] = pygame.image.load("exit_button.png")


    def draw(self,visible_obj):
        img = self.sprites[visible_obj.name]
        img_trasform = pygame.transform.scale(img,visible_obj.size)
        self.screen.blit(img_trasform,(visible_obj.x_pos,visible_obj.y_pos))

    
class Controller:
    def __init__(self,model):
        self.model = model

    def left_key_down(self):
        self.model.move("left")
    
    def right_key_down(self):
        self.model.move("right")

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WIN_SIZE)
        pygame.display.set_caption(WIN_TITLE)

        self.view = View(self.screen)
        self.model = Model(self.view)
        self.controller = Controller(self.model)

        #keyの押しっぱなしを適応する
        #ここの第二引数を調整することでバーの速さを調整できる気もする！
        pygame.key.set_repeat(5,15)

    '''
   イベントに関する処理をまとめたもの
   以前の方法だと、現在のscreenを表示するためにwhile分使っているために、その外側の
   eventに関する処理を行うことができなかったために、ここで関数としてまとめて、
   screenを表示するためのwhile文の中でその関数を呼び出す形にしたいが。。。
   ちょっとゴリ押しな気もするのでいい案があれば・・・よろしく
   '''
    def event_controll(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()        
            
            #キー入力に関するもの
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    self.controller.left_key_down()
                elif event.key == K_RIGHT:
                    self.controller.right_key_down()
            
            if event.type == pygame.MOUSEBUTTONDOWN and self.view.now_screen == "title":
                for e in self.model.visibles:
                    if e.name == "start" and e.is_inner(event.pos):
                        self.view.now_screen = e.push_and_get_next_screen()
                        #画面に表示されている要素を全て削除する
                        for s in self.model.visibles:
                            s.delete()
                        #プレイ画面を作る。
                        self.model.make_game_play()

    #仮
    i = 0
    def event_loop(self):
        clock = pygame.time.Clock()
        while True:

                #どの画面を表示するか、now_screenを見て決める。画面遷移をさせたい時はnow_screenの値を変えるようにする．
                while self.view.now_screen == "title":
                    self.event_controll()
                    #画面を黒で塗りつぶす。これがないと千手観音みたいになる
                    self.screen.fill((0,0,0))
                    #仮実装
                    #一度だけmake_titleを呼び出すためにこうしている。
                    if self.i == 0:
                        self.model.make_title()
                        self.i =1 
                    self.model.update()
                    pygame.display.update()

                while self.view.now_screen == "game_play":
                    self.event_controll()
                    self.screen.fill((0,0,0))
                    self.model.update()
                    pygame.display.update()

                while self.view.now_screen == "ranking":
                    return
                while self.view.now_screen == "how_to_play":
                    return

                


if __name__ == "__main__":
    app = App()
    app.event_loop()