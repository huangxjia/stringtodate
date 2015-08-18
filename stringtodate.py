__author__ = 'huangxuejia'

import pandas as pd
import datetime
import matplotlib.pyplot as plt

class string():
    def __init__(self, series):
        self.series = series

    def string_to_date(self):
        for i in self.series.index:
            self.series.ix[i] = datetime.datetime.strptime(self.series.ix[i], "%Y-%m-%d")
        return self.series

if __name__ == "__main__":

    bars = pd.read_csv("/Users/huangxuejia/Documents/data/1.csv")
    index = pd.Series(bars.ix[1:445, 0])
    mac = string(index).string_to_date()
    iron_ore = pd.DataFrame(bars.ix[1:445, 1].reshape(445,1), columns = ['prices'], index=mac)

    fig, ax = plt.subplots()
    ax.plot(iron_ore.index, iron_ore['prices'],'k',  label = "iron ore future prices")
    plt.title('Iron ore futures prices')
    plt.xlabel('Time')
    plt.ylabel('Prices')
    plt.grid(True)
    ax.set_xlim(['2013-9-20', '2014-12-30'])#good
    #ax.xaxis.set_major_locator(matplotlib.dates.WeekdayLocator(byweekday=matplotlib.dates.MO) )
    #ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%d\n%b\n%Y'))
    #ax.xaxis.set_major_formatter(matplotlib.scale.ScalarFormatter())
    #rec = ax.set_xlim(mac)

    plt.show()

