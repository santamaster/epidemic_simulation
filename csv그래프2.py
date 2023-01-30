import csv
from matplotlib import pyplot as plt

inf_count_all = []
inf_count_all2 = []
inf_count_all3 = []
inf_count_all4 = []
inf_count_all5 = []
total_inf_list = []
total_inf_list2 = []
total_inf_list3 = []
total_inf_list4 = []
total_inf_list5 = []
repeat = 3

f = open('102,0.4,13,(300,600)data.csv','r')
f2 = open('230,0.4,13,(300,600)data.csv','r')
f3 = open('307,0.4,13,(300,600)data.csv','r')
f4 = open('921,0.4,13,(300,600)data.csv','r')
f5 = open('1470,0.4,13,(300,600)data.csv','r')
rdr = csv.reader(f)
rdr2 = csv.reader(f2)
rdr3 = csv.reader(f3)
rdr4 = csv.reader(f4)
rdr5 = csv.reader(f5)
a = 3
for i in rdr:
    alist = []
    if a//3 ==3:
        for k in i:
            alist.append(int(k))
        inf_count_all.append(alist)
    a +=1
x = 0
for k in range(len(inf_count_all[0])):
    for m in range(repeat):
        x += int(inf_count_all[m][k]/repeat)
    total_inf_list.append(x)
    x= 0

a = 3
for i2 in rdr2:
    alist = []
    if a//3 ==3:
        for k2 in i2:
            alist.append(int(k2))
        inf_count_all2.append(alist)

    a +=1
x = 0
for k in range(len(inf_count_all2[0])):
    for m in range(repeat):
        x += int(inf_count_all2[m][k]/repeat)
    total_inf_list2.append(x)
    x= 0
a = 3
for i3 in rdr3:
    alist = []
    if a//3 ==3:
        for k3 in i3:
            alist.append(int(k3))
        inf_count_all3.append(alist)

    a +=1
x = 0
for k in range(len(inf_count_all3[0])):
    for m in range(repeat):
        x += int(inf_count_all3[m][k]/repeat)
    total_inf_list3.append(x)
    x= 0
a = 3
for i4 in rdr4:
    alist = []
    if a//3 ==3:
        for k4 in i4:
            alist.append(int(k4))
        inf_count_all4.append(alist)

    a +=1
x = 0
for k in range(len(inf_count_all4[0])):
    for m in range(repeat):
        x += int(inf_count_all4[m][k]/repeat)
    total_inf_list4.append(x)
    x= 0
a = 3
for i5 in rdr5:
    alist = []
    if a//3 ==3:
        for k5 in i5:
            alist.append(int(k5))
        inf_count_all5.append(alist)

    a +=1
x = 0
for k in range(len(inf_count_all5[0])):
    for m in range(repeat):
        x += int(inf_count_all5[m][k]/repeat)
    total_inf_list5.append(x)
    x= 0
f.close()
repeat = 3

list_length = []
list_length.append(len(total_inf_list))
list_length.append(len(total_inf_list2))
list_length.append(len(total_inf_list3))
list_length.append(len(total_inf_list4))
list_length.append(len(total_inf_list5))
long = max(list_length)
plt.plot(total_inf_list,color= 'r',ls= '-',label = 'suspect')
plt.plot(total_inf_list2,color = 'r',ls = '-',label = 'exposed')
plt.plot(total_inf_list3,color = 'r', ls = '-',label = 'infected')
plt.plot(total_inf_list4,color = 'r',ls = '-',label = 'recovered')
plt.plot(total_inf_list5,color = 'r',ls = '-',label = 'removed')
plt.xlabel('time')
plt.xticks(list(range(0,long,60)),labels=list(range(0,long//60+1)))
plt.ylabel('number of person')
plt.legend(shadow=True, fancybox=True, loc="upper right")
        
plt.show()

