import csv

min=1000
max=-1000
sum=0
average=0
count=0
with open('s2data.csv', 'r', newline='') as csvfile:
	spamreader=csv.reader(csvfile,delimiter=',')
	for row in spamreader:
		value=float(row[-2])
		if value<min:
			min=value
		if value>max:
			max=value
		sum=sum+value
		count=count+1
	average=sum/count
	print('min',min)
	print('max',max)
	print('sum',sum)
	print('average',average)
	print('count',count)