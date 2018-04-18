import random
import math
import csv
from scipy.stats import truncnorm

def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

r=[]
a=get_truncated_normal(mean=1.663366, sd=0.93437546, low=0, upp=3)#alcohol
b=get_truncated_normal(mean=3.1584158415842, sd=0.96012561196001, low=1, upp=4)#chest pain
c=get_truncated_normal(mean=2, sd=1, low=1, upp=3)#smoking
dm=get_truncated_normal(mean=131.6, sd=17.599747729588, low=100, upp=320)#restingBP systolic male
df=get_truncated_normal(mean=127, sd=13.599747729588, low=100, upp=320)#restingBP systolic female
#e=get_truncated_normal(mean=180, sd=30, low=160, upp=220)#max heart rate dependent upon age
f=get_truncated_normal(mean=2, sd=1, low=0, upp=3)# bmi
g=get_truncated_normal(mean=1, sd=1, low=0, upp=2)#exercise level
hm=get_truncated_normal(mean=246, sd=52, low=105, upp=380)#cholestrol male
hf=get_truncated_normal(mean=240, sd=50, low=105, upp=380)#cholestrol female
j=get_truncated_normal(mean=0.148, sd=0.35, low=0, upp=1)#diabetes

with open('data4.csv', 'wb') as csvfile:
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
		out=(age/70)+sex+(chestPain/4)+(restingBP/320)+(cholestrol/380)+(1-diabetes)+(smoking/3)+(maxHeartRate/220)-(exerciseLevel)+(bmi/3)+(alcohol/3)
		r.append(math.floor(out/2))
		spamwriter.writerow(r)
		del r[:]