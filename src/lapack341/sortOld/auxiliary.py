import urllib, shutil, csv
from time import time
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir) 
import summary.summary


print "----------------- Sort the auxiliary routines in the old version -----------------"


###------------ find auxiliary routines in the old version 
wr_single = csv.writer(open('./routines/auxiliary_old_single.txt', 'w'), delimiter=';')
wr_double = csv.writer(open('./routines/auxiliary_old_double.txt', 'w'), delimiter=';')
wr_complex = csv.writer(open('./routines/auxiliary_old_complex.txt', 'w'), delimiter=';')
wr_complex16 = csv.writer(open('./routines/auxiliary_old_complex16.txt', 'w'), delimiter=';')
wr_aux = csv.writer(open('./routines/auxiliary_old_aux.txt', 'w'), delimiter=';')

auxiliary_single = []
auxiliary_double = []
auxiliary_complex = []
auxiliary_complex16 = []
auxiliary_aux = []
i=0
j=0
k=0
l=0
m=0
start = time()
f = open("./routines/routines_old_list.txt", 'r')
for line in f:
    routineName = line.split(' ')[1]
    category = line.split(' ')[2]
    #print category
    if "auxiliary" in category:
        print routineName, "------->", category
        if category[0:3] == "aux":
            m += 1
            auxiliary_aux.append(routineName)
            wr_aux.writerow([m, routineName[0], routineName[1:-2], "http://www.netlib.org/lapack/lapack_routine/"+routineName])
            #print category
        elif category[0:4] == "real":
                i += 1
                auxiliary_single.append(routineName)
                wr_single.writerow([i, routineName[0], routineName[1:-2], "http://www.netlib.org/lapack/lapack_routine/"+routineName])
        elif category[0:6] == "double":
            j += 1
            auxiliary_double.append(routineName)
            wr_double.writerow([j, routineName[0], routineName[1:-2], "http://www.netlib.org/lapack/lapack_routine/"+routineName])
        elif category[0:9] == "complex16":
            l += 1
            auxiliary_complex16.append(routineName)
            wr_complex16.writerow([l, routineName[0], routineName[1:-2], "http://www.netlib.org/lapack/lapack_routine/"+routineName])
        else:
            k += 1
            auxiliary_complex.append(routineName)
            wr_complex.writerow([k, routineName[0], routineName[1:-2], "http://www.netlib.org/lapack/lapack_routine/"+routineName])  

f.close()


print "Auxiliary single: ", len(auxiliary_single)
print "Auxiliary double: ", len(auxiliary_double)
print "Auxiliary complex: ", len(auxiliary_complex)
print "Auxiliary complex16: ", len(auxiliary_complex16)
print "Auxiliary auxiliary: ", len(auxiliary_aux)
print "total time: ", time()-start
