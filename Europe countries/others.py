import pandas

#modified original downloaded csv file
data = pandas.read_csv('data.csv')
data['name'].to_csv('modified_data.csv')

data = pandas.read_csv('additional_data.txt', sep=' ', header=None)
file = pandas.read_csv('modified_data.csv', index_col=0)

file['x'] = data[0]
file['y'] = data[1]

file.to_csv('final.csv')