day = 5
indices = np.where(data['Day'] == day) # find indices of 5th day for every month (over all data)
temp = data['Temp'][indices] # find corresponding temperatures
print temp.size
print temp
