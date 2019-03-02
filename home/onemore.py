import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import bytespdate2num

time, impressions = np.loadtxt("/home/pi/finalLog.csv", #%Y-%m-%d %H:%M:%S
unpack=True, delimiter=',', converters={0: bytespdate2num('%Y:%m:%d:%H:%M:%S')})

plt.plot_date(x=time, y=impressions, linestyle ="-")
#plot.bar(x=time, y=impressions)
plt.title("Page impressions on example.com")
plt.ylabel("Page impressions")
plt.grid(True)
plt.show()



plt.show()