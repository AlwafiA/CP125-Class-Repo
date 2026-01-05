"""def find_station(stations, name):
    for item in range(len(stations)):
        if stations[item] == name:
            return item 
    return -1


def count_stops(stations, start, stop):
    count = 0
    start_check = find_station(stations, start)
    stop_check = find_station(stations, stop)
    if start_check == -1 or stop_check == -1:
        return -1
    else :
        for start in range(len(stations)):
            if stations[start] != stop:
                count +=1
    print(count)
    return count


train = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
count_stops(train, "Marina", "Sentosa")"""

def find_station(stations, name):
    for i in range(len(stations)):
        if stations[i] == name:
            return i
    return -1

def count_stops(stations, start, stop):
    start_idx = find_station(stations, start)
    stop_idx = find_station(stations, stop)
    
    if start_idx == -1 or stop_idx == -1:
        return -1
        
    return abs(start_idx - stop_idx)

train = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
count_stops(train, "Marina", "Sentosa")