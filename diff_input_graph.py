import matplotlib.pyplot as plt


standard_time=[721.00,2433.53,4453.09,7358.05,9003.92]
data_size=[5000,15000,25000,35000,45211]

improved_time=[369.06,1538.02,2082.95,3204.39,4257.61]

plt.title("Data Size VS Time")
plt.xlabel('Data Size-->')
plt.ylabel('Time -->')

plt.scatter(data_size,standard_time)
plt.scatter(data_size,improved_time)
plt.plot(data_size, standard_time,color = 'r')
plt.plot(data_size, improved_time,color = 'b')
plt.show()