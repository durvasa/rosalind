#!/usr/bin/python3

fibo = []
timepoint = 29
multiplier = 5

fibo.append(1)
fibo.append(1)
for month in range(2,timepoint):
	fibo.append(fibo[month-1] + multiplier*fibo[month-2])
print("%d" %fibo[timepoint-1])
