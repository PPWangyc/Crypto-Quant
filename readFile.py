from asyncio.windows_events import NULL
import pandas as pd


data_path = 'data.csv'
Timestamp = NULL
Open = NULL
High = NULL
Low = NULL
Close = NULL
Volume = NULL
Quantity = NULL
csv_data = NULL
date_time = NULL

def readFile():
    global csv_data
    global Timestamp
    global Open
    global High
    global Low
    global Close
    global Volume
    global Quantity
    csv_data = pd.read_csv(data_path)
    csv_data.columns=csv_data.columns.str.strip()
    csv_data = csv_data.sort_values(by = 'Timestamp')
    Timestamp = csv_data.iloc[:,0].values.reshape(-1,1)
    Open = csv_data.iloc[:,1].values.reshape(-1,1)
    High = csv_data.iloc[:,2].values.reshape(-1,1)
    Low = csv_data.iloc[:,3].values.reshape(-1,1)
    Close = csv_data.iloc[:,4].values.reshape(-1,1)
    Volume = csv_data.iloc[:,5].values.reshape(-1,1)
    Quantity = csv_data.iloc[:,6].values.reshape(-1,1)
    toDateTime()

def toDateTime():
    global Timestamp
    global date_time
    temp = []
    for x in Timestamp:
        temp.append(pd.to_datetime(x,unit='ms'))

    temp = pd.DataFrame(data = temp)
    temp = temp.sort_values(by = 0)
    date_time = temp.iloc[:,0].values
    return date_time

def test():
    readFile()
    print(csv_data)
    print(Timestamp)
    print(Open)
    print(date_time)

