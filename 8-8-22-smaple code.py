def calculatefare():
    global var1
    Path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]
    BusStops = ['TH', 'GA', 'IC', 'HA', 'TE', 'LU', 'NI', 'CA']
    prompt1 = str(input("Enter Pickup = "))
    prompt2 = str(input("Enter Destination = "))
    total = 0
    if prompt1 not in BusStops or prompt2 not in BusStops:
        print("Check your Input and enter bus stop from valid path")
    elif prompt1 not in BusStops and prompt2 not in BusStops:
        print("Check your Input and enter bus stop from valid path")
    else:
        for i in range(0, len(BusStops)):
            if BusStops[i] == prompt1:
                var = i
        for j in range(0, len(BusStops)):
            if BusStops[j] == prompt2:
                var1 = j
        if var == var1:
            print("INVALID")
        elif (var < var1):
            while (var <= var1):
                total = total + Path[var]
                var += 1
        elif (var > var1):
            while (var >= var1):
                total = total + Path[var]
                var -= 1
        return total


amount = calculatefare() * 0.005
print(f'RS {amount} is your travel fare')
