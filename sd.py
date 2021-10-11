import csv
import plotly.express as px
import pandas as pd
import math

with open('data.csv', newline='') as f:
    f_read = csv.reader(f)
    data = list(f_read)
marks = data[0]

def mean(data):
    sum = 0
    n = len(data)
    for i in marks:
        sum += int(i)
    mean = sum/n
    return mean

sq_l = []

for i in marks:
    a = int(i)- mean(marks)
    a = a**2
    sq_l.append(a)

sum_s = 0

for i in sq_l:
    sum_s += i

result = sum_s/(len(marks)-1)

sd = math.sqrt(result)

print(result, sd)
