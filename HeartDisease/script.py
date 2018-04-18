import random
import math
import csv
from scipy.stats import truncnorm

def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)
# #writing to csv file row wise
# h=['Spam','Baked','Beans','are','Lovely']
# with open('eggs.csv', 'w', newline='') as csvfile:
# 	spamwriter = csv.writer(csvfile)#, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 	spamwriter.writerow(h)
# 	spamwriter.writerow(h*2)

# experimenting with random no.
# random.seed(5)
# st=random.getstate()
# print(random.random())
# random.setstate(st)
# print(random.random(),'\n')
# random.setstate(st)
# print(random.gauss(5,3))
# print(random.gauss(5,3))
# print(random.gauss(5,3))
# print(random.gauss(5,3))
# print(random.gauss(5,3),'\n')
# random.setstate(st)
# print(random.normalvariate(5,3))
# print(random.normalvariate(5,3))
# print(random.normalvariate(5,3))
# print(random.normalvariate(5,3))
# print(random.normalvariate(5,3),'\n')
# for genrating within a range
# X = get_truncated_normal(mean=8, sd=3, low=1, upp=10)
# print(X.rvs(100))


# for age we use random.randint(28,70) which produces random integers
# for sex we use random.randrange(0,2,1) 0=male 1=female
# for chest pain scale (0-3) we use random.randrange(0,3,1)
# for level of smoking (0-->no,1-->low,2-->moderate,3-->high) we use random.randrange(0,2,1)
# for resting bp (in bpm) we use random.randrange()
# for thalach (max heart rate achieved) we use random.randrange()
# for level of alcohol consumption(0-->no,1-->light,2-->moderate,3-->heavy) random.randrange(0,3,1)
# bmi (0-->underweight,1-->normal,2-->overweight,3-->obese) random.randrange(0,3,1)
# exercise level for half an hour random.randrange(0,2,1)
# cholestrol (mg/dl)
# diabetes (0->no,1->yes)
# stress (0,40)
##r=[age,sex,chestPain,smokingLevel,restingBP,maxHeartRate,alcoholConsumption,BMI,exerciseLevel,cholestrol,diabetes,stress]
##writing to csv file row wise
# r=[]
# with open('eggs.csv', 'w', newline='') as csvfile:
# 	spamwriter = csv.writer(csvfile)#, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 	for i in range(1,100001):
# 		r.append(random.randint(28,70))#a
# 		r.append(random.randrange(0,1,1))
# 		r.append(random.randrange(0,3,1))#b
# 		r.append(random.randrange(0,2,1))#c
# 		r.append(random.randrange(50,100,1))#d
# 		r.append(random.randrange(160,220,1))#e
# 		r.append(random.randrange(0,3,1))#f
# 		r.append(random.randrange(0,3,1))#g
# 		r.append(random.randrange(0,2,1))#h
# 		r.append(random.randrange(100,350,1))#i
# 		spamwriter.writerow(r)
# 		del r[:]

r=[]
a=get_truncated_normal(mean=1.663366, sd=0.93437546, low=0, upp=3)#alcohol
b=get_truncated_normal(mean=2, sd=0.75, low=1, upp=4)#chest pain
c=get_truncated_normal(mean=2, sd=1, low=1, upp=3)#smoking
dm=get_truncated_normal(mean=127, sd=20, low=81, upp=320)#restingBP systolic male
df=get_truncated_normal(mean=122, sd=15, low=81, upp=320)#restingBP systolic female
#e=get_truncated_normal(mean=180, sd=30, low=160, upp=220)#max heart rate dependent upon age
f=get_truncated_normal(mean=2, sd=1, low=0, upp=3)# bmi
g=get_truncated_normal(mean=1, sd=1, low=0, upp=2)#exercise level
hm=get_truncated_normal(mean=192, sd=50, low=105, upp=380)#cholestrol male
hf=get_truncated_normal(mean=182, sd=50, low=105, upp=380)#cholestrol female
j=get_truncated_normal(mean=0.35, sd=0.5, low=0, upp=1)#diabetes
sm=get_truncated_normal(mean=12.1,sd=5.9,low=0,upp=40)
sf=get_truncated_normal(mean=13.7,sd=6.6,low=0,upp=40)
s1=get_truncated_normal(mean=14.2,sd=6.2,low=0,upp=40)
s2=get_truncated_normal(mean=13.0,sd=6.2,low=0,upp=40)
s3=get_truncated_normal(mean=12.6,sd=6.1,low=0,upp=40)
s4=get_truncated_normal(mean=11.9,sd=6.9,low=0,upp=40)
s5=get_truncated_normal(mean=12.0,sd=6.3,low=0,upp=40)

with open('s2data3.csv', 'w', newline='') as csvfile:
	spamwriter = csv.writer(csvfile)#, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for i in range(1,11112):
		age=random.randrange(28,71)
		r.append(age)
		sex=random.randrange(0,2,1)
		r.append(sex)
		chestPain=round(b.rvs())
		r.append(chestPain)#chest pain
		restingBP=0
		if sex==0: #for male resting bp
			restingBP=round(dm.rvs())
			r.append(restingBP)
		else:
			restingBP=round(df.rvs())
			r.append(restingBP)
		cholestrol=0
		if sex==0: #for male cholestrol
			cholestrol=round(hm.rvs())
			r.append(cholestrol)
		else:
			cholestrol=round(hf.rvs())
			r.append(cholestrol)
		diabetes=round(j.rvs())
		r.append(diabetes)#diabetes
		smoking=round(c.rvs())
		r.append(smoking)#smoking
		e=get_truncated_normal(mean=220-age, sd=10, low=90, upp=220)#max heart rate
		maxHeartRate=round(e.rvs())
		r.append(maxHeartRate)
		exerciseLevel=round(g.rvs())
		r.append(exerciseLevel)#exercise level
		bmi=round(f.rvs())
		r.append(bmi)#bmi
		alcohol=round(a.rvs())
		r.append(alcohol)#alcohol
		if age<30:
			stress=round(s1.rvs())
		elif age>=30 and age<=44:
			stress=round(s2.rvs())
		elif age>=45 and age<=54:
			stress=round(s3.rvs())
		elif age>=55 and age<=64:
			stress=round(s4.rvs())
		else:
			stress=round(s5.rvs())
		if sex==0:
			stress=(stress+sm.rvs())/2
			#stress=min(stress,sm.rvs())
		else:
			stress=(stress+sf.rvs())/2
			#stress=min(stress,sf.rvs())
		r.append(int(round(stress)))
		out=(age/70)+sex+(chestPain/4)+(restingBP/280)+(cholestrol/380)+(1-diabetes)+(smoking/2)+(maxHeartRate/220)-(exerciseLevel/2)*2+(bmi/3)*0.5+(alcohol/3)+(stress/40)
		r.append(math.floor(out/2))
		spamwriter.writerow(r)
		del r[:]