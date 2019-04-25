import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime

def main():
    f = open('graph.csv', 'r')

    data, dates, severities = [], [], []
    count = 0

    for lines in f:
        if count != 0:
            x = lines.split(',')
            dates.append(str(x[0]).strip())
            data.append(str(x[1]).strip() + ", " + str(x[2]).strip())
            severities.append(str(x[3]).strip())
        count += 1

    dates = [datetime.strptime(ii, "%a %b %d %H:%M:%S %Y") for ii in dates]
    levels = np.array([-5, 5, -3, 3, -1, 1])
    fig, ax = plt.subplots(figsize=(13, 5))

    start = min(dates)
    stop = max(dates)
    ax.plot((start, stop), (0, 0), 'k', alpha=.5)

    low = 'g'
    medium = 'y'
    high = 'r'
    for ii, (iname, idate, iseverity) in enumerate(zip(data, dates, severities)):
        level = levels[ii % 6]
        vert = 'top' if level < 0 else 'bottom'
        rotation = 80 if level < 0 else 110
        severity = 'w'
        if iseverity == 'MEDIUM':
            severity = medium
        elif iseverity == 'HIGH':
            severity = high
        elif iseverity == 'LOW':
            severity = low
        ax.scatter(idate, 0, s=100, facecolor=severity, edgecolor='k', zorder=9999)
        ax.plot((idate, idate), (0, level), c='b', alpha=.7)
        ax.text(idate, level, iname,
                horizontalalignment='left', verticalalignment=vert, fontsize=10,
                backgroundcolor=(1., 1., 1., .3))

    ax.set(title="Event Viewer")

    ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=1))
    ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %d %Y"))
    fig.autofmt_xdate()

    plt.setp((ax.get_yticklabels() + ax.get_yticklines() +
              list(ax.spines.values())), visible=False)
    plt.show()