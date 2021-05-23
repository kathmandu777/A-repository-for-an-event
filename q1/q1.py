import csv
import math

file = open("./q1.csv","r", encoding="utf_8", errors="", newline="" )

reader = csv.reader(file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

header = next(reader)
print(header)
# for row in reader:
#     print(row)

def get_distance(row):
    base_lati = 35.6697
    base_long = 139.76714

    base_lati = int(base_lati* 10 **7)
    base_long = int(base_long* 10 **7)

    answer = row[0]
    latitude = int(float(row[1]) * 10**7)
    longtitude = int(float(row[2]) * 10**7)

    distance = math.sqrt( (latitude - base_lati)**2 + (longtitude - base_long)**2 )
    return distance, answer 
    
min = 99999999
answer = "ex"

for row in reader:
    dis, ans = get_distance(row)
    if(min > dis):
        min = dis
        answer = ans
    
print(answer,min)