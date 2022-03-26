import datetime
import random
import math
import shutil


#assign random values to cluster centers
c1_x=1+random.random()*25
c1_y=1+random.random()*25
c2_x=1 + random.random() * 25
c2_y=1 + random.random() * 25
c3_x=1 + random.random() * 25
c3_y=1 + random.random() * 25


def fill_the_clusters():
    global c1_x,c1_y,c2_x,c2_y,c3_x,c3_y,sensitivity,iteration_count
    print('we reach fill the clusters')
    file1 = open('sampledata.txt', 'r')
    f3x = open('c1.txt', 'w')
    f3x.close()
    f3x = open('c2.txt', 'w')
    f3x.close()
    f3x = open('c3.txt', 'w')
    f3x.close()
    # Using for loop
    # print("Using for loop")
    for line in file1:
        #line_count += 1
        x1,y1=line.split(';')
        x1_f=float(x1)
        y1_f=float(y1)
        dif1=(c1_x-x1_f)**2
        dif2=(c1_y-y1_f)**2
        abs_dif1=math.sqrt(dif1+dif2)
        dif3 = (c2_x - x1_f) ** 2
        dif4 = (c2_y - y1_f) ** 2
        abs_dif2 = math.sqrt(dif3 + dif4)
        dif5 = (c3_x - x1_f) ** 2
        dif6 = (c3_y - y1_f) ** 2
        abs_dif3 = math.sqrt(dif5 + dif6)
        if abs_dif1==min(abs_dif1,abs_dif2,abs_dif3):
            f3 = open('c1.txt', 'a')
            f3.write(str(x1_f))
            f3.write(';')
            f3.write(str(y1_f) + '\n')  # python will convert \n to os.linesep
            f3.close()
        elif abs_dif2==min(abs_dif1, abs_dif2, abs_dif3):
            f4 = open('c2.txt', 'a')
            f4.write(str(x1_f))
            f4.write(';')
            f4.write(str(y1_f) + '\n')  # python will convert \n to os.linesep
            f4.close()
        elif abs_dif3==min(abs_dif1, abs_dif2, abs_dif3):
            f4 = open('c3.txt', 'a')
            f4.write(str(x1_f))
            f4.write(';')
            f4.write(str(y1_f) + '\n')  # python will convert \n to os.linesep
            f4.close()

    # Closing files
    file1.close()
    if iteration_count==0:
        shutil.copyfile('c1.txt', 'c1_first.txt')
        shutil.copyfile('c2.txt', 'c2_first.txt')
        shutil.copyfile('c3.txt', 'c3_first.txt')
    adjust_clusters()

def average_of_a_class(classfilename):
# Opening file
    file1 = open(classfilename+'.txt', 'r')
    line_count = 0
    x_sum=0.0
    y_sum=0.0

    # Using for loop
    print("Using for loop")
    for line in file1:
        line_count += 1
        x1,y1=line.split(';')

        x_sum+=float(x1)
        y_sum+=float(y1)
    # Closing files
    file1.close()
    if line_count==0:
        x_avg=0
        y_avg=0
    else:
        x_avg=x_sum/line_count
        y_avg=y_sum/line_count
    return x_avg,y_avg

def adjust_clusters():
    global c1_x,c1_y,c2_x,c2_y,c3_x,c3_y,sensitivity,iteration_count
    iteration_count+=1
    if iteration_count == 1:
        fc6 = open('firstscenters.txt', 'w')
        fc6.write(str(c1_x))
        fc6.write(';')
        fc6.write(str(c1_y))
        fc6.write('\n')
        fc6.write(str(c2_x))
        fc6.write(';')
        fc6.write(str(c2_y))
        fc6.write('\n')
        fc6.write(str(c3_x))
        fc6.write(';')
        fc6.write(str(c3_y))
        fc6.write('\n')
        fc6.close()
    print('we reach fill adjust clusters')
    x_center_of_a_class,y_center_of_a_class=average_of_a_class ('c1')
    x_center_of_class1_f=float(x_center_of_a_class)
    y_center_of_class1_f=float(y_center_of_a_class)
    print('c1 class')
    print(x_center_of_class1_f)
    print(y_center_of_class1_f)

    x_center_of_class2,y_center_of_class2=average_of_a_class ('c2')
    x_center_of_class2_f=float(x_center_of_class2)
    y_center_of_class2_f=float(y_center_of_class2)
    print('c2 class')
    print(x_center_of_class2_f)
    print(y_center_of_class2_f)

    x_center_of_a_class,y_center_of_a_class=average_of_a_class ('c3')
    x_center_of_class3_f=float(x_center_of_a_class)
    y_center_of_class3_f=float(y_center_of_a_class)
    print('c3 class')
    print(x_center_of_class3_f)
    print(y_center_of_class3_f)
    sum_of_center_dif = (abs(y_center_of_class3_f - c3_y) + abs(x_center_of_class3_f - c3_x) + abs(
        y_center_of_class2_f - c2_y) + abs(x_center_of_class2_f - c2_x) + abs(x_center_of_class1_f - c1_x) + abs(
        y_center_of_class1_f - c1_y))
    fc2 = open('objective.txt', 'a')
    fc2.write(str(iteration_count))
    fc2.write(';')
    fc2.write(str(sum_of_center_dif))
    fc2.write('\n')
    fc2.close()
    if (abs(x_center_of_class1_f-c1_x)>sensitivity) or (abs(y_center_of_class1_f-c1_y)>sensitivity) or (abs(x_center_of_class2_f-c2_x)>sensitivity) or (abs(y_center_of_class2_f-c2_y)>sensitivity) or (abs(x_center_of_class3_f-c3_x)>sensitivity) or (abs(y_center_of_class3_f-c3_y)>sensitivity):
        print('we reach iteration if')
        fc1 = open('iteration.txt', 'a')
        fc1.write('cluster1 x difference ')
        fc1.write(str(abs(x_center_of_class1_f-c1_x)))
        fc1.write(' cluster 1 y difference ')
        fc1.write(str(abs(y_center_of_class1_f - c1_y)))
        fc1.write(' cluster 2 x difference ')
        fc1.write(str(abs(x_center_of_class2_f-c2_x)))
        fc1.write(' cluster 2 y difference ')
        fc1.write(str(abs(y_center_of_class2_f-c2_y)))
        fc1.write(' cluster 3 x difference ')
        fc1.write(str(abs(x_center_of_class3_f-c3_x)))
        fc1.write(' cluster 3 y difference ')
        fc1.write(str(abs(y_center_of_class3_f-c3_y)))
        fc1.write('\n')
        fc1.close()

        c1_x=x_center_of_class1_f
        c1_y=y_center_of_class1_f
        c2_x=x_center_of_class2_f
        c2_y=y_center_of_class2_f
        c3_x=x_center_of_class3_f
        c3_y=y_center_of_class3_f
        print('iteration call for clusters')
        fill_the_clusters()
    else:
        print('adjustment complete')
        fc1 = open('iteration.txt', 'a')
        fc1.write('Final values cluster1 x difference ')
        fc1.write(str(abs(x_center_of_class1_f - c1_x)))
        fc1.write(' cluster 1 y difference ')
        fc1.write(str(abs(y_center_of_class1_f - c1_y)))
        fc1.write(' cluster 2 x difference ')
        fc1.write(str(abs(x_center_of_class2_f - c2_x)))
        fc1.write(' cluster 2 y difference ')
        fc1.write(str(abs(y_center_of_class2_f - c2_y)))
        fc1.write(' cluster 3 x difference ')
        fc1.write(str(abs(x_center_of_class3_f - c3_x)))
        fc1.write(' cluster 3 y difference ')
        fc1.write(str(abs(y_center_of_class3_f - c3_y)))
        fc1.write('\n')
        fc1.close()
        fc5 = open('finalcenters.txt', 'w')
        fc5.write(str(c1_x))
        fc5.write(';')
        fc5.write(str(c1_y))
        fc5.write('\n')
        fc5.write(str(c2_x))
        fc5.write(';')
        fc5.write(str(c2_y))
        fc5.write('\n')
        fc5.write(str(c3_x))
        fc5.write(';')
        fc5.write(str(c3_y))
        fc5.write('\n')
        fc5.close()
        quit()

#cleaning data in the text files
f = open('sampledata.txt', 'w')
f.close()

f = open('c1.txt', 'w')
f.close()

f = open('c2.txt', 'w')
f.close()

f = open('c3.txt', 'w')
f.close()

f = open('iteration.txt', 'w')
f.close()

f = open('objective.txt', 'w')
f.close()
#cleaning complete

sensitivity=0.001 #the value is trashhold limit for determining class

generator_counter=0 #counter for generating x and y coordinates.

#creating data set with 30000 elements. it consists of 3 parts
while generator_counter<30000:
    if generator_counter<10000:
        x_coordinate = random.random()*-3+5+random.random()*3
        y_coordinate = random.random()*-3+4+random.random()*3
#first part is complete
    elif  generator_counter>9999 and generator_counter<20000:
        x_coordinate = random.random()*-3+10+random.random()*3
        y_coordinate = random.random()*-3+9+random.random()*3
#second part is complete
    elif  generator_counter>19999 and generator_counter<30000:
        x_coordinate = random.random()*-3+15+random.random()*3
        y_coordinate = random.random()*-3+14+random.random()*3
#thrid part is complete
    f = open('sampledata.txt', 'a')
    f.write(str(x_coordinate))
    f.write(';')
    f.write(str(y_coordinate)+'\n')  # python will convert \n to os.linesep
    f.close()
    generator_counter += 1
print('random data generation complete')




iteration_count = 0

fill_the_clusters()
