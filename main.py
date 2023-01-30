import pygame as pg
import random
from matplotlib import pyplot as plt
from people_module import*
import csv

def main(n):
    #pygame 초기화
    pg.init()
    inf_p = 1
    #사람 수 카운트
    sus_count  = []
    exp_count = []
    inf_count = []
    rec_count = []
    rem_count = []
    sus_count_all = []
    exp_count_all = []
    inf_count_all = []
    rec_count_all = []
    rem_count_all = []

    for _ in range(number_of_people- first_infected_person):
        sus_person= susceptible()
        sus_people_list.add(sus_person)

    for _ in range(first_infected_person):
        inf_person = infectious(random.randint(10,width-10),random.randint(10,height-10),random.randint(3,7),random.randint(1,360))
        inf_people_list.add(inf_person)
    global done,l,already_social_distancing,already_wear_mask
    #루프
    while done:
        
        #fps 설정
        clock.tick(FPS)

        #이벤트 처리
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = 0
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    done = 0
        #스크린 배경 색상
        screen.fill(White)
    
        #사람들 업데이트
        rec_people_list.update()
        rem_people_list.update()
        sus_people_list.update()
        exp_people_list.update()
        inf_people_list.update()
        

        #메세지 출력
        msg_normal = myfont.render("susceptible : {}".format(len(sus_people_list.sprites())),True,Blue) 
        screen.blit(msg_normal,(10,10))
        #접촉군
        msg_exp = myfont.render("exposed :{}".format(len(exp_people_list.sprites())),True,Yellow)
        screen.blit(msg_exp,(10,40))
        #감염자 수
        msg_infected = myfont.render("infected : {}".format(len(inf_people_list.sprites())),True,Red)
        screen.blit(msg_infected,(10,70))
        #회복한 사람
        msg_number_of_recovered_person = myfont.render("recovered: {}".format(len(rec_people_list.sprites())),True,Green)
        screen.blit(msg_number_of_recovered_person,(10,100))
        #죽은 사람
        msg_number_of_dead = myfont.render("removed: {}".format(len(rem_people_list)),True,Gray)
        screen.blit(msg_number_of_dead,(10,130))

        #전체 사람 수
        msg_number_of_person = myfont.render("person : {}".format(number_of_people),True,Black)
        screen.blit(msg_number_of_person,(size[0]-150,10))
        #반복횟수 표시
        msg_repeat = myfont.render("repeat : {}/{}".format(repeat-n+1,repeat),True,Black)
        screen.blit(msg_repeat,(size[0]-150,70))
        #밀도
        msg_density = myfont.render("density : {}".format(density),True,Black)
        screen.blit(msg_density,(size[0]-150,100))
        #반복 및 자동 종료
        if len(inf_people_list) == 0:
            sus_count_all.append(sus_count)
            exp_count_all.append(exp_count)
            inf_count_all.append(inf_count)
            rec_count_all.append(rec_count)
            rem_count_all.append(rem_count)
            

            sus_people_list.empty()
            exp_people_list.empty()
            inf_people_list.empty()
            rec_people_list.empty()
            rem_people_list.empty()
            
            sus_count = []
            exp_count = []
            inf_count = []
            rec_count = []
            rem_count = []

            
            
            for _ in range(number_of_people - first_infected_person):
                sus_person= susceptible()
                sus_people_list.add(sus_person)
            for _ in range(first_infected_person):
                inf_person = infectious(random.randint(10,width-10),random.randint(10,height-10),random.randint(3,7),random.randint(1,360))
                inf_people_list.add(inf_person)
            
            n-=1
            if n ==0:
                done = 0
            
        pg.display.flip()
        sus_count.append(len(sus_people_list.sprites()))
        exp_count.append(len(exp_people_list.sprites()))
        inf_count.append(len(inf_people_list.sprites()))
        rec_count.append(len(rec_people_list.sprites()))
        rem_count.append(len(rem_people_list.sprites()))
        #이미지 저장
        #name = 'capture%05d'%l
        #pg.image.save(screen,"C:/Users/jihun/Desktop/python/epidemic-simulation/200image/{}.png".format(name))
        l+=1

    pg.quit()
    total = []
    for i in range(repeat):
        total.append(len(sus_count_all[i]))
    long = max(total)
    for a in range(repeat):
        sus_count_last = sus_count_all[a][-1]
        for _ in range((long -len(sus_count_all[a]))):
            sus_count_all[a].append(sus_count_last)
    for a in range(repeat):
        exp_count_last = exp_count_all[a][-1]
        for _ in range((long -len(exp_count_all[a]))):
            exp_count_all[a].append(exp_count_last)
    for a in range(repeat):
        inf_count_last = inf_count_all[a][-1]
        for _ in range((long -len(inf_count_all[a]))):
            inf_count_all[a].append(inf_count_last)
    for a in range(repeat):
        rec_count_last = rec_count_all[a][-1]
        for _ in range((long -len(rec_count_all[a]))):
            rec_count_all[a].append(rec_count_last)
    for a in range(repeat):
        rem_count_last = rem_count_all[a][-1]
        for _ in range((long -len(rem_count_all[a]))):
            rem_count_all[a].append(rem_count_last)
    total_sus_list = []
    total_exp_list = []
    total_inf_list = []
    total_rec_list = []
    total_rem_list = []
    x = 0
    for k in range(long):
        for m in range(repeat):
            x += int(sus_count_all[m][k]/repeat)
        total_sus_list.append(x)
        x= 0
    for k in range(long):
        for m in range(repeat):
            x += int(exp_count_all[m][k]/repeat)
        total_exp_list.append(x)
        x= 0
    for k in range(long):
        for m in range(repeat):
            x += int(inf_count_all[m][k]/repeat)
        total_inf_list.append(x)
        x= 0
    for k in range(long):
        for m in range(repeat):
            x += int(rec_count_all[m][k]/repeat)
        total_rec_list.append(x)
        x= 0
    for k in range(long):
        for m in range(repeat):
            x += int(rem_count_all[m][k]/repeat)
        total_rem_list.append(x)
        x= 0
    #csv 파일 쓰기
    f = open("{},{},{},({},{})data.csv".format(density,infected_chance,radius,r_time_1,r_time_2),"w",newline='')
    wr = csv.writer(f)
    wr.writerows(sus_count_all)
    wr.writerows(exp_count_all)
    wr.writerows(inf_count_all)
    wr.writerows(rec_count_all)
    wr.writerows(rem_count_all)
    f.close()

    #중첩 그래프 
    if 1:
        plt.figure(1)
        plt.plot(total_sus_list,color= 'b',ls= '-',label = 'suspect')
        plt.plot(total_exp_list,color = 'y',ls = '-',label = 'exposed')
        plt.plot(total_inf_list,color = 'r', ls = '-',label = 'infected')
        plt.plot(total_rec_list,color = 'g',ls = '-',label = 'recovered')
        plt.plot(total_rem_list,color = 'k',ls = '-',label = 'removed')
        plt.xlabel('time')
        plt.xticks(list(range(0,long,60)),labels=list(range(0,long//60+1)))

        plt.ylabel('number of person')
        plt.legend(shadow=True, fancybox=True, loc="upper right")
        
        plt.figure(2)
        plt.plot(total_sus_list,color= 'b',ls= '-',label = 'suspect')
        plt.xlabel('time')
        plt.xticks(list(range(0,long,60)),labels=list(range(0,long//60+1)))
        plt.ylabel('number of person')
        plt.ylim(0,number_of_people)
        plt.legend(shadow=True, fancybox=True, loc="upper right")
        
        plt.figure(3)
        plt.plot(total_exp_list,color = 'y',ls = '-',label = 'exposed')
        plt.xlabel('time')
        plt.xticks(list(range(0,long,60)),labels=list(range(0,long//60+1)))

        plt.ylabel('number of person')
        plt.ylim(0,number_of_people)
        plt.legend(shadow=True, fancybox=True, loc="upper right")
        
        plt.figure(4)
        plt.plot(total_inf_list,color = 'r', ls = '-',label = 'infected')
        plt.xlabel('time')
        plt.xticks(list(range(0,long,60)),labels=list(range(0,long//60+1)))

        plt.ylabel('number of person')
        plt.ylim(0,number_of_people)
        plt.legend(shadow=True, fancybox=True, loc="upper right")
        
        plt.figure(5)
        plt.plot(total_rec_list,color = 'g',ls = '-',label = 'recovered')
        plt.xlabel('time')
        plt.xticks(list(range(0,long,60)),labels=list(range(0,long//60+1)))

        plt.ylabel('number of person')
        plt.ylim(0,number_of_people)
        plt.legend(shadow=True, fancybox=True, loc="lower right")
        
        plt.figure(6)
        plt.plot(total_rem_list,color = 'k',ls = '-',label = 'removed')
        plt.xlabel('time')
        plt.xticks(list(range(0,long,60)),labels=list(range(0,long//60+1)))

        plt.ylabel('number of person')
        plt.ylim(0,number_of_people)
        plt.legend(shadow=True, fancybox=True, loc="upper right")
        
        plt.show()



    
    print('접촉자 최대값:{}'.format(max(total_exp_list)))
    print('감염자 최대값:{}'.format(max(total_inf_list)))
    print('접촉자 최대값 도달 시간 :{}'.format(total_exp_list.index(max(total_exp_list))+1))
    print('감염자 최대값 도달 시간 :{}'.format(total_inf_list.index(max(total_inf_list))+1))
    print("총시간:{}".format(len(total_exp_list)))
if __name__ == "__main__":
    main(repeat)

