import pygame,sys,os,random
from pygame.locals import*
from pygame import mixer
from pygame.transform import rotozoom

pygame.init()
mixer.init()

vongLap = True
huong_dan = False
gioi_thieu = False
manhinh = pygame.display.set_mode((800,600))
icon = pygame.image.load('source/cat/nyan-cat-icegif-15-0_preview_rev_1.png').convert_alpha()
pygame.display.set_icon(icon)
pygame.display.set_caption("Cat_Rainbow")
game_run = True
gravity = 0.7
#text_info
font = pygame.font.Font('sound/Oswald-VariableFont_wght.ttf', 100)
font2 = pygame.font.Font('sound/Oswald-VariableFont_wght.ttf', 30)
menu_text = font.render("PLAY", True, (255,255,255))
menu_text_rect = menu_text.get_rect(center = (400,200)) 
huongDan = font2.render("Hướng dẫn",True,(255,255,255))
huongDan_rect = huongDan.get_rect(center = (400,420))
gioiThieu = font2.render("Giới thiệu", True, (255,255,255))
gioiThieu_rect = gioiThieu.get_rect(center = (400,320))
thoat = font2.render("Thoát Game", True, (255,255,255))
thoat_rect = gioiThieu.get_rect(center = (387,550))
thoat_rect2 = gioiThieu.get_rect(center = (387,470))
class HD():
    def __init__(self):
        self.font = pygame.font.Font('sound/Oswald-VariableFont_wght.ttf', 30)
        self.img = pygame.image.load('source/huongdan.png')
        self.rect = self.img.get_rect(center = (400,300))
        self.return_menu = self.font.render("Trở về trang chính",True,(255,255,255))
        self.return_menu_rect = self.return_menu.get_rect(center = (230,400))
    def draw(self):
        manhinh.blit(self.img,self.rect)
        manhinh.blit(self.return_menu,self.return_menu_rect)
hd = HD()        
        
    
class Intro():
    def __init__(self):
        self.font = pygame.font.Font('sound/Oswald-VariableFont_wght.ttf', 30)
        self.font2 = pygame.font.Font('sound/Oswald-VariableFont_wght.ttf', 20)
        self.text1 = self.font.render("Nhà phát triển: Game DEV Nhóm 2",True,(255,255,255))
        self.text2 = self.font.render("Võ Chí Trung",True,(255,255,255))
        self.text3 = self.font.render("Cao Thị Yến Vy",True,(255,255,255))
        self.text4 = self.font.render("Nguyễn Thị Lan Anh",True,(255,255,255))
        self.text5 = self.font2.render("Game được xây dựng dựa trên ý tưởng của game Flappy Bird  nhưng được thay đổi lối chơi sang chiều ngang",True,(255,255,255))
        self.text6 = self.font2.render("Game hoàn toàn được xây dựng bằng ngôn ngữ Python",True,(255,255,255))
        self.text_rect = self.text1.get_rect(center = (400,100))
        self.return_menu = self.font.render("Trở về trang chính",True,(255,255,255))
        self.return_menu_rect = self.return_menu.get_rect(center = (400,500))
    def draw(self):
        manhinh.blit(self.text1,self.text_rect)
        manhinh.blit(self.text2,(self.text_rect.centerx-400,self.text_rect.centery + 50))
        manhinh.blit(self.text3,(self.text_rect.centerx-400,self.text_rect.centery + 100))
        manhinh.blit(self.text4,(self.text_rect.centerx-400,self.text_rect.centery + 150))
        manhinh.blit(self.text5,(self.text_rect.centerx-400,self.text_rect.centery + 200))
        manhinh.blit(self.text6,(self.text_rect.centerx-400,self.text_rect.centery + 250))
        manhinh.blit(self.return_menu,self.return_menu_rect)
intro = Intro()
def draw_menu():
    manhinh.blit(gioiThieu,gioiThieu_rect)
    manhinh.blit(menu_text,menu_text_rect)
    manhinh.blit(huongDan,huongDan_rect)
    manhinh.blit(thoat,thoat_rect)
# Nhạc nền
mixer.music.load('sound/y2mate.com - Giornos Theme  il vento doro 8Bit VRC6  JoJos Bizarre Adventure Golden Wind.mp3')
va_cham = mixer.Sound('sound/y2mate (mp3cut.net).mp3')
nhay = mixer.Sound('sound/mixkit-player-jumping-in-a-video-game-2043 (1).wav')
mixer.music.play(-1)
def end():
    mixer.music.stop()
    mixer.Sound.play(va_cham)
def jump_sound():
    mixer.Sound.play(nhay)
class Cat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.transform.scale(pygame.image.load('source/cat/nyan-cat-icegif-15-0_preview_rev_1.png'),(131,74))
        self.rect = self.img.get_rect(center = (100,300))
        self.animation_lst = []
        self.frame_index = 0
        self.time = pygame.time.get_ticks()
        self.motion =0
        self.jump = False
        for i in range(len(os.listdir('source/cat'))):
            self.animation_lst.append(pygame.transform.scale(pygame.image.load(f'source/cat/nyan-cat-icegif-15-{i}_preview_rev_1.png'),(131,74)))
    def draw(self):
       # pygame.transform.rotozoom(self.img, self.motion , 1)
        manhinh.blit(pygame.transform.rotozoom(self.img, -self.motion , 1),self.rect)
    def move(self):
        dy = 0
        self.motion += gravity
        if self.jump == True:
            self.motion = -15
            self.jump = False
        dy += self.motion
        self.rect.centery += dy
    def update_animation(self):
        if pygame.time.get_ticks() - self.time >= 50:
            self.frame_index  += 1
            self.time = pygame.time.get_ticks()
            self.img = self.animation_lst[self.frame_index]
            if self.frame_index >= len(self.animation_lst)-1:
                self.frame_index = 0
cat = Cat()      
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.transform.scale(pygame.image.load('source/bg/5m5V-0.png').convert_alpha(),(800,600))
        self.animation_lst = []
        self.time = pygame.time.get_ticks()
        self.frame_index = 0
        self.time_play = 1
        self.x = 0
        for i in range(3):
            self.animation_lst.append(pygame.transform.scale(pygame.image.load(f'source/bg/5m5V-{i}.png').convert_alpha(),(800,600)))
    def run(self):
        self.time_play += 0.0003
        self.x -= self.time_play
        if self.x <= -800:
            self.x = 0
    def draw(self):
        manhinh.blit(self.img,(self.x,0))
        manhinh.blit(self.img,(self.x + 800,0))
    def update_animation(self):
        if pygame.time.get_ticks() - self.time >= 100:
            self.frame_index += 1 
            self.time = pygame.time.get_ticks()
            self.img = self.animation_lst[self.frame_index]
            if self.frame_index == 2:
                self.frame_index = 0
bg = Background()       

class Rainbow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.transform.scale(pygame.image.load('source/rainbow/Pin-on-Geek-culture-0_preview_rev_1.png').convert_alpha(),(100,80))
        self.time = pygame.time.get_ticks()
        self.frame_index = 0
        self.animation_lst = []
        for i in range(len(os.listdir('source/rainbow'))):
            self.animation_lst.append(pygame.transform.scale(pygame.image.load(f'source/rainbow/Pin-on-Geek-culture-{i}_preview_rev_1.png').convert_alpha(),(100,80)))
    def draw(self):
        self.rect = self.img.get_rect(midright =(cat.rect.centerx-20,cat.rect.centery))
        manhinh.blit(pygame.transform.rotozoom(self.img, -cat.motion, 1),self.rect)
    def update_animation(self):
        if pygame.time.get_ticks()- self.time >= 200:
            self.frame_index += 1
            self.time = pygame.time.get_ticks()
            self.img = self.animation_lst[self.frame_index]
            if self.frame_index == len(self.animation_lst)-1:
                self.frame_index = 0
rainbow = Rainbow()   

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.y_lst = [50,100,150,200,250,300,350,400,450,500,550]
        self.y = 300
        self.thien_thach_lst = []
        self.animation_lst = []
        self.frame_index = 0
        self.time_play = 4
        # khúc này hơi rối
        self.timer = 2500  # thời gian spaw và là biến giảm khi chơi càng lâu
        self.time = pygame.time.get_ticks() # thời gian để update animation cho thiên thạch
        self.time_add_meteor = pygame.time.get_ticks() # thời gian để thêm một vị trí cũng như hình vuông mới cho viên thiên thạch
        self.time_update_speed = pygame.time.get_ticks() # thời gian để thời gian spaw bị rút ngắn lại 
        for i in range(len(os.listdir('source/meteor'))):
            self.animation_lst.append(pygame.transform.scale((pygame.transform.rotate(pygame.image.load(f'source/meteor/Meteor{i}.png').convert_alpha()  , -90) ),(128,128)))
    def remove(self):
        for i in self.thien_thach_lst:
            if i.x <=-100:
                self.thien_thach_lst.remove(i)
    def draw(self):
        self.y = random.choice(self.y_lst)
        for i in self.thien_thach_lst:
            manhinh.blit(self.img,i) 
            i.centerx -= self.time_play
        self.time_play += 0.001
    def update_animation(self):
        if pygame.time.get_ticks() - self.time >= 100:
            self.frame_index += 1
            self.time = pygame.time.get_ticks()
            self.img = self.animation_lst[self.frame_index]
            if self.frame_index == len(self.animation_lst) -1:
                self.frame_index = 0
    def level(self):
        if pygame.time.get_ticks() - self.time_update_speed >= 1000:
            self.time_update_speed = pygame.time.get_ticks()
            self.timer -= 20
            if self.timer == 0:
                self.timer += 20
    def update_timer(self):
        if pygame.time.get_ticks() - self.time_add_meteor >= self.timer:
            self.time_add_meteor = pygame.time.get_ticks()
            self.thien_thach_lst.append(self.img.get_rect(center =(1100,self.y)))    
thienthach = Meteor()  
 
class Text():
    def __init__(self):
        self.vongLap = True
        self.text_lst = ["","NHẤN CÁCH ĐỂ CHƠI LẠI"]
        self.text_num = 0
        self.font = pygame.font.Font('sound/Oswald-VariableFont_wght.ttf', 22)
        self.text = self.font.render(self.text_lst[self.text_num], True, (255,255,255))
        self.text_rect = self.text.get_rect( center = (400,560))
    def draw(self):
        manhinh.blit(self.text,self.text_rect)
    def update_text(self):
        if game_run == False:
            self.text_num =1
            manhinh.blit(thoat,thoat_rect2)
            if thoat_rect2.collidepoint(pos):
                if game_run == False:
                    if pygame.mouse.get_pressed()[0] == 1:
                        self.vongLap = False;
                
        else:
            self.text_num = 0
        self.text = self.font.render(self.text_lst[self.text_num], True, (255,255,255))
        self.text_rect = self.text.get_rect( center = (400,560))
text = Text()

class Score():
    def __init__(self):
        self.time = pygame.time.get_ticks()
        self.score = 0
        self.size = 22
        self.font = pygame.font.Font('sound/Oswald-VariableFont_wght.ttf', self.size)
        self.output = self.font.render(str(self.score), True, (255,255,255))
    def draw(self):
        if game_run == False:
            self.size = 200
            self.font = pygame.font.Font('sound/Oswald-VariableFont_wght.ttf', self.size)
            self.rect = self.output.get_rect(center = (400,300))
            self.output = self.font.render(str(self.score), True, (255,255,255))
        else:
            self.size = 22
            self.font = pygame.font.Font('sound/Oswald-VariableFont_wght.ttf', self.size)
            self.rect = self.output.get_rect(center = (200,560))
            self.output = self.font.render("điểm" + str(self.score), True, (255,255,255))
        manhinh.blit(self.output,self.rect)  
    def update_score(self):
        if pygame.time.get_ticks() - self.time >= 1000:
            self.time = pygame.time.get_ticks()
            self.score += 1 
            if game_run == False: 
                self.score -= 1
score = Score()
menu = False
while vongLap:
    if text.vongLap == False:
        vongLap = False 
    pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and menu == True:
                cat.jump = True                
                jump_sound()
            if event.key == K_SPACE and game_run == False:
                cat.rect = cat.img.get_rect(center = (100,300))
                thienthach.thien_thach_lst.clear()
                thienthach.timer = 2500
                thienthach.time_play = 4
                bg.time_play = 1
                mixer.music.play(-1)
                score.score = 0
                game_run = True
    #bg
    bg.draw()  
    bg.update_animation()
    if gioi_thieu == True:
        intro.draw()
    elif huong_dan :
        hd.draw()
    else :
        draw_menu()
        if thoat_rect.collidepoint(pos):
            if (menu == False) :
                if pygame.mouse.get_pressed()[0] == 1:
                    vongLap = False
            
    
    if menu_text_rect.collidepoint(pos) and gioi_thieu == False and huong_dan == False:
        if pygame.mouse.get_pressed()[0] == 1 :
            menu = True
    if huongDan_rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1 :
            huong_dan = True;
    if gioiThieu_rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            gioi_thieu = True   
    if intro.return_menu_rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            gioi_thieu = False    
    if hd.return_menu_rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            huong_dan = False   
    if menu:  
        bg.draw()
        bg.run()
        bg.update_animation()              
        if game_run: 
            #rainbow
            rainbow.draw()
            rainbow.update_animation()
            #cat
            cat.draw()  
            cat.update_animation() 
            cat.move()
            #meteor
            thienthach.draw()
            thienthach.update_animation()
            thienthach.level()
            thienthach.update_timer()
            thienthach.remove()
            #system 
            for i in thienthach.thien_thach_lst:
                if cat.rect.collidepoint(i.center):
                    game_run = False
                    end()     
            if cat.rect.top <= -200 or cat.rect.bottom >= 800:
                game_run = False
                end()         
        #score
        score.draw()
        score.update_score()
    #text
    text.draw()
    text.update_text()
    pygame.time.Clock().tick(120)
    pygame.display.update()