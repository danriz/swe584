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
    x_avg=x_sum/line_count
    y_avg=y_sum/line_count
    return x_avg,y_avg


#c_x1,c_y1=average_of_a_class ('sampledata')
#print(c_x1)
#print(c_y1)
