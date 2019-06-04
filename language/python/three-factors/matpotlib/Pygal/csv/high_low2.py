import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index,cloume_header in enumerate(header_row):
        print(index,cloume_header)

    dates,highs,lows = [],[],[]
    for row in reader:
        
        try:
            current_date = datetime.strptime(row[0],'%Y-%m-%d') 
            high = int(row[1]) 
            low = int(row[3])
        except ValueError as e:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs, c='red')
plt.plot(dates,lows, c='blue')
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)# 给图表区域着色
plt.title("Daily high and low temperatures, - 2014", fontsize=24)

plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # 绘制斜的日期标签
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
