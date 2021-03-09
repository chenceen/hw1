# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107061115.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Retrive all data points which station id are "C0A880", "C0F9A0", "C0G640", "C0R190", and "C0X260" as a list.
tmp = list(filter(lambda item: item['station_id'] == 'C0A880' or item['station_id'] == 'C0F9A0' or item['station_id'] == 'C0G640' or item['station_id'] == 'C0R190' or item['station_id'] == 'C0X260', data))
# Retrive the data points which HUMD are not -99.000 or -999.000
tmp = filter(lambda item: item['HUMD'] != '-99.000' and item['HUMD'] != '-999.000', tmp)
# Sort the station id in the lexicographical order
tmp = sorted(tmp, key = lambda item: item['station_id'])
# Build the array to store the output data
target_data = [['C0A880', 'None'], ['C0F9A0', 'None'], ['C0G640', 'None'], ['C0R190', 'None'], ['C0X260', 'None']]

j = 0                                                       # Declare the variable
for i in range(len(target_data)):                           # Store data in five station
   while (j < len(tmp)):                                    # Run every data
      if tmp[j]['station_id'] != target_data[i][0]:         # Determine if the data is for that station
         break                                              # If not, switch to another station
      else:                                                 # If the data is for that station
         if target_data[i][1] == 'None':                    # If there's no data in the station
            target_data[i][1] = float(tmp[j]['HUMD'])       # Assign the data in it
         else:                                              # If there's data inside
            target_data[i][1] += float(tmp[j]['HUMD'])      # Add up the data
      j+=1                                                  # Deal with next data

#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)

#========================================
