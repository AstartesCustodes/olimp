import matplotlib.pyplot as plt
from time import sleep, strftime, time
import csv

x = []
y = []

with open("/home/pi/templog.csv", "r") as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append((row[0]))
        y.append((row[1]))

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()