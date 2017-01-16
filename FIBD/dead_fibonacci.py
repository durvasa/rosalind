#!/usr/bin/python3

dead_fibo = {}
timepoint = 98
lifespan = 16

# initialise dead_fibo
dead_fibo[(1,1)] = 1
for month in range(2,lifespan+1):
	dead_fibo[(1,month)] = 0

for time in range(2,timepoint+1):
	for month in range(1,lifespan+1):
		if month == 1:
			tempsum = 0
			for k in range(2,lifespan+1):
				tempsum += dead_fibo[(time-1,k)]
			dead_fibo[(time,month)] = tempsum
		else:
			dead_fibo[(time,month)] = dead_fibo[(time-1,month-1)]

population = 0
for month in range(1, lifespan+1):
	population += dead_fibo[(timepoint,month)]
print("%d" %population)
