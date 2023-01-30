import pygame as pg
import random
from math import radians,sin,cos
#pygame 초기화
pg.init()
#색상 변수
White = (255,255,255)
Red = (255,0,0)
Yellow = (255,255,0)
Green = (0,255,0)
Blue = (80,188,223)
Gray = (128,128,128)
Black = (0,0,0)

#시스템 설정
width = 1080
height = 720 
size = [width,height] 
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
FPS = 1000
done = 1
myfont = pg.font.SysFont(None,30)
pg.display.set_caption("epidemic simulation")
repeat = 1#반복 횟수
number_of_people = 1500#사람수
density = int(width *height/number_of_people)
l=1#변경 금지

#확률
infected_chance =0.4#  감염 확률
die_percent = 0.1#감염된 사람이 죽을 확률

first_infected_person = 1#초기 감염자 수 
#크기
person_size = [8,8]
radius =13#감염 확산 범위

#죽거나 회복 할때까지 걸리는 시간
r_time_1 = 300#최소 시간
r_time_2 = 600#최대 시간
r_time_3 = 300
r_time_4 = 600
#감염자 증가시 마스크 착용 또는 거리두기 실행
infect_people =10#마스크,거리두기,감염자 격리 시작 감염자 수

wear_mask = 0#마스크 착용 
mask_infect_chance = 0.01#마스크 착용시 감염 확률
already_wear_mask = 0

social_distancing = 0#사회적 거리두기 실행
social_distancing_radius = 6#거리두기 실행시 감염 확산 범위
already_social_distancing = 0
#아직 미완성, 만지지 마라
infected_person_isolation = 0#감염자 격리
maximum_isolation = 200#감염자 격리 최대 수용인원
isolation_time_1 = 15#0.25초
isolation_time_2 = 30#0.5초
isolation_fatality_rate = 0.03#격리시 치사율
isolaton_person = 0#변경 금지,격리자 수
#감염대상군
class susceptible(pg.sprite.Sprite):
    def __init__(self):
        global already_wear_mask
        pg.sprite.Sprite.__init__(self)
        self.speed = random.randint(3,7)
        self.x = random.randint(10,width-10)
        self.y = random.randint(10,height-10)
        self.moving_degree = random.randint(-10,10)
        self.delta_degree = random.randint(1,5)
        self.degree = random.randint(1,360)
        self.color = Blue
        self.rect = pg.Rect((self.x,self.y),person_size)
        self.infect_bool = False
        self.already_check = False
        already_wear_mask = 0
    def sus_move(self):
        self.rect = pg.Rect((self.x,self.y),person_size)
        self.center = (self.x,self.y)
        if self.moving_degree > 0:
            self.degree += self.delta_degree
            self.moving_degree -= 1
        elif self.moving_degree < 0:
            self.degree -= self.delta_degree
            self.moving_degree += 1
        else:
            self.moving_degree = random.randint(-20,20)
            self.delta_degree = random.randint(1,5)
        if self.x <= 0:
            self.degree = 180 - self.degree
            self.x = 0
        elif self.x >= width:
            self.degree = 180-self.degree
            self.x = width
        elif self.y <= 0:
            self.degree = 360 - self.degree
            self.y = 0
        elif self.y >= height:
            self.degree = 360 - self.degree
            self.y = height
        self.x += self.speed * cos(radians(self.degree))
        self.y += self.speed * sin(radians(self.degree))
        self.sus_person = pg.draw.ellipse(screen,self.color,self.rect)
    def infection(self):
        global infected_chance,already_wear_mask
        if self.infect_bool:
            if already_wear_mask:
                if random.random()<=mask_infect_chance:
                    sus_people_list.remove(self)
                    expose = Exposed(self.x,self.y,self.speed,self.degree)
                    exp_people_list.add(expose)
                    self.infect_bool = False
                else:
                    self.infect_bool = False
                    self.already_check = True
            else:
                if random.random()<=infected_chance:
                    sus_people_list.remove(self)
                    expose = Exposed(self.x,self.y,self.speed,self.degree)
                    exp_people_list.add(expose)
                    self.infect_bool = False
                else:
                    self.infect_bool = False
                    self.already_check = True
        if not pg.sprite.spritecollide(self,inf_people_list,False):
            self.already_check = False
        #마스크 착용
        if wear_mask:
            if len(inf_people_list)> infect_people:
                already_wear_mask = 1

        
    def update(self):
        self.sus_move()
        self.infection()
#접촉군
class Exposed(pg.sprite.Sprite):
    def __init__(self,x,y,speed,degree):
        pg.sprite.Sprite.__init__(self)
        self.speed = speed
        self.x = x
        self.y = y
        self.moving_degree = random.randint(-10,10)
        self.delta_degree = random.randint(1,5)
        self.degree = degree
        self.rect = pg.Rect((self.x,self.y),person_size)
        self.rect.center = (self.x,self.y)
        self.color = Yellow
        self.inf_tick = random.randint(60,180)#접촉된 사람이 감염된 사람이 될 때까지 걸린 시간 /기본:1~3초 사이 실수 
        
    def exp_move(self):
        self.rect = pg.Rect((self.x,self.y),person_size)
        self.rect.center = (self.x,self.y)
        if self.moving_degree > 0:
            self.degree += self.delta_degree
            self.moving_degree -= 1
        elif self.moving_degree < 0:
            self.degree -= self.delta_degree
            self.moving_degree += 1
        else:
            self.moving_degree = random.randint(-20,20)
            self.delta_degree = random.randint(1,5)
        if self.x <= 0:
            self.degree = 180 - self.degree
            self.x = 0
        elif self.x >= width:
            self.degree = 180-self.degree
            self.x = width
        elif self.y <= 0:
            self.degree = 360 - self.degree
            self.y = 0
        elif self.y >= height:
            self.degree = 360 - self.degree
            self.y = height
        self.x += self.speed * cos(radians(self.degree))
        self.y += self.speed * sin(radians(self.degree))
        self.inf_person = pg.draw.ellipse(screen,self.color,self.rect)

    def exp_to_inf(self):
        if self.inf_tick ==0:
            exp_people_list.remove(self)
            inf_person = infectious(self.x,self.y,self.speed,self.degree)
            inf_people_list.add(inf_person)
        self.inf_tick -= 1

    def update(self):
        self.exp_move()
        self.exp_to_inf()

#감염군
class infectious(pg.sprite.Sprite):
    def __init__(self,x,y,speed,degree):
        global die_percent
        pg.sprite.Sprite.__init__(self)
        self.speed = speed
        self.x = x
        self.y = y
        self.moving_degree = random.randint(-10,10)
        self.delta_degree = random.randint(1,5)
        self.degree = degree
        self.man = pg.Rect((self.x,self.y),person_size)
        self.color = Red
        if len(inf_people_list)<infect_people:
            die_percent = isolation_fatality_rate
        if random.random()<=die_percent:
            self.you_already_die_LOL = 1
            self.dead_tick = random.randint(r_time_1,r_time_2)#죽을때 까지 걸린 시간/기본:5~10초 사이 실수 
        else:
            self.you_already_die_LOL = 0
            self.recovered_tick = random.randint(r_time_3,r_time_4)#회복까지 걸리는 시간/기본 :5~10초 사이 실수
        self.isolation_time = random.randint(isolation_time_1,isolation_time_2)#격리까지 걸리는 시간,미완성
        self.k = 1#변경 금지
        self.radius = radius
        self.sd_radius = social_distancing_radius
        self.rad = pg.Surface((self.radius*2,self.radius*2),pg.SRCALPHA)
        self.sd_rad = pg.Surface((self.sd_radius*2,self.sd_radius*2),pg.SRCALPHA)
        self.rect = self.rad.get_rect(center=(self.x,self.y))
        already_social_distancing = 0
    def inf_move(self):
        global social_distancing,already_social_distancing
        self.x += self.speed * cos(radians(self.degree))
        self.y += self.speed * sin(radians(self.degree))
        self.man = pg.Rect((self.x,self.y),person_size)
        self.man.center = (self.x,self.y)
        if self.moving_degree > 0:
            self.degree += self.delta_degree
            self.moving_degree -= 1
        elif self.moving_degree < 0:
            self.degree -= self.delta_degree
            self.moving_degree += 1
        else:
            self.moving_degree = random.randint(-20,20)
            self.delta_degree = random.randint(1,5)
        if self.x <= 0:
            self.degree = 180 - self.degree
            self.x = 0
        elif self.x >= width:
            self.degree = 180-self.degree
            self.x = width
        elif self.y <= 0:
            self.degree = 360 - self.degree
            self.y = 0
        elif self.y >= height:
            self.degree = 360 - self.degree
            self.y = height
        
        pg.draw.ellipse(screen,self.color,self.man)
        if social_distancing:
            if len(inf_people_list)> infect_people:
                already_social_distancing = 1
        if already_social_distancing:
            if len(inf_people_list)>infect_people:
                if self.k:
                    self.rect = self.sd_rad.get_rect(center = (self.x,self.y))
                    screen.blit(self.sd_rad,self.rect)
                    pg.draw.circle(self.sd_rad,(255,0,0,30),(self.sd_radius,self.sd_radius),self.sd_radius)
            else:
                if self.k:
                    self.rect = self.rad.get_rect(center = (self.x,self.y))
                    screen.blit(self.rad,self.rect)
                    pg.draw.circle(self.rad,(255,0,0,30),(self.radius,self.radius),self.radius)
        
        else:
            if self.k:
                self.rect = self.rad.get_rect(center = (self.x,self.y))
                screen.blit(self.rad,self.rect)
                pg.draw.circle(self.rad,(255,0,0,30),(self.radius,self.radius),self.radius)
        
    def inf_to_rem_or_rec(self):
        if infected_person_isolation:
            if len(inf_people_list.sprites()) < maximum_isolation:
                if self.isolation_time ==0:
                    self.color = 255,127,0
                    self.k = 0
                else:
                    self.isolation_time -= 1
        if self.you_already_die_LOL: 
            if self.dead_tick ==0:
                inf_people_list.remove(self)
                rem_person = removed(self.x,self.y)
                rem_people_list.add(rem_person)
            self.dead_tick -=1
        elif not self.you_already_die_LOL:
            if self.recovered_tick ==0:
                inf_people_list.remove(self)
                rec_person = recovered(self.x,self.y)
                rec_people_list.add(rec_person)
            self.recovered_tick -= 1
    def infection(self):
        if pg.sprite.spritecollide(self,sus_people_list,False):
            for colliding in pg.sprite.spritecollide(self,sus_people_list,False):
                if not colliding.already_check:
                    colliding.infect_bool = True
                
    def update(self):
        self.inf_move()
        self.inf_to_rem_or_rec()
        if self.k:
            self.infection()

#회복군
class recovered(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.color=Green
        self.x = x
        self.y = y
        self.rect = pg.Rect((self.x,self.y),person_size)
    def recovered_draw(self):
        self.recovered_person = pg.draw.ellipse(screen,Green,self.rect)
    
    def update(self):
        self.recovered_draw()

#사망군
class removed(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.color = Gray
        self.x = x
        self.y = y
        self.rect = pg.Rect((self.x,self.y),person_size)

    def removed_draw(self):
        self.removed_person = pg.draw.ellipse(screen,self.color,self.rect)
    
    def update(self):
        self.removed_draw()
#그룹화
sus_people_list = pg.sprite.Group()
exp_people_list = pg.sprite.Group()
inf_people_list = pg.sprite.Group()
rec_people_list = pg.sprite.Group()
rem_people_list = pg.sprite.Group()
