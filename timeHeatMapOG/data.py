import csv, json


def TimeGenerator():
    with open('US_Accidents_May19.csv') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            yield(row["Start_Time"])

def findHr(dateStr):
    return dateStr.split(" ")[1].split(":")[0]

def findMin(dateStr):
    return dateStr.split(" ")[1].split(":")[1]

def main():
    hr_min_value_list = []
    for hrs in range(24):
        temp_hr_list = []
        for mins in range(60):
            temp_hr_list.append(0)
        hr_min_value_list.append(temp_hr_list)


    for time in TimeGenerator():
        hr_min_value_list[int(findHr(time))][int(findMin(time))] += 1

    with open("timeFreq.csv", "w") as outfile:
        outfile.write("Hour,Min,Count_Corrected\n")
        for hrs in range(24):
            for mins in range(60):
                count = hr_min_value_list[hrs][mins]
                outfile.write(str(hrs)+','+str(mins)+','+str(count//25)+'\n')
            
main()