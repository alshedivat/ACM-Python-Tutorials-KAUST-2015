fig = plt.figure(figsize=(18,4))
ax = fig.add_subplot(1,1,1)
ax.plot(data['Year']+data['Month']/12.0+data['Day']/365, data['Temp'])
ax.axis('tight')
ax.set_title('tempeatures in Stockholm')
ax.set_xlabel('year')
ax.set_ylabel('temperature (C)');