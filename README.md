# Homework 1 Python Data Analysis
Find out the summation of the HUMD value from C0A880, C0F9A0, C0G640, C0R190, C0X260.

## How to setup and run the program
### 1. Import module
Download 107061115.csv, and import into the program
```
import csv
```

### 2. Read cwb weather data
```
cwb_filename = '107061115.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
  mycsv = csv.DictReader(csvfile)
  header = mycsv.fieldnames
  for row in mycsv:
    data.append(row)
```

### 3. Analyze data
Using filter function to get all data points of 5 stations, and use another filter to get the data which are not '-99.000' and '-999.000'. Then, use the sorted function to sort the data with its station id. Create an array target_data to store the summation of 'HUMD' value of 5 stations. Use double loop to classify the data into 5 stations. Outer loop for switching to different station, inner loop to run every data. An if function to determine whether the data is for the true station, and another if/else function to determine whether to assign the data or to sum up (target_data had been initialize as 'None').

### 4. Print result
```
print(target_data)
```

### 5. Run the program
```
python3 hw1.py
```

## Result
```
[['C0A880', 22.34], ['C0F9A0', 18.88], ['C0G640', 20.770000000000003], ['C0R190', 18.339999999999996], ['C0X260', 18.549999999999997]]
```
