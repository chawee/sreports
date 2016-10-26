import glob
import csv
import matplotlib.pyplot as pl
import re

files=glob.glob('survey*.csv')
initials=[]
gender=[]
age=[]
major=[]
answer1=[]
answer2=[]
uniquemajors=[]
output=open('consolidated.csv','w')
for f in files:
    openfile=open(f,'r')
    data=csv.reader(openfile)
    for line in data:
        if line[0] is not '' :
            if (len(line[1].replace('.','')) < 4 and line[1] and line[5] and line[6] and 'None' not in line[6]):
                initials.append(line[1].replace('.',''))
                gender.append(line[2])
                age.append(line[4])
                major.append(line[3])
                if line[3] not in uniquemajors:
                    uniquemajors.append(line[3])
                '''print line[1],re.findall('\d+',line[6])

                break'''
                answer1.append(int(re.findall('\d+',line[5])[0]))

                answer2.append(int(re.findall('\d+',line[6])[0]))

out=csv.writer(output, delimiter=',')
for i in range(len(initials)):
    out.writerow([initials[i], gender[i], age[i], major[i], answer1[i], answer2[i]])

print len(uniquemajors)

