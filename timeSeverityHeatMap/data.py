import csv, json


def TimeGenerator():
    with open('US_Accidents_May19.csv') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            yield(row["Start_Time"], row["Severity"])

def findHr(dateStr):
    return dateStr[0].split(" ")[1].split(":")[0]

# def findMin(dateStr):
#     return dateStr.split(" ")[1].split(":")[1]

def findSev(infoTuple):
    return infoTuple[1]

def main():
    hr_min_value_list = []
    for hrs in range(24):
        temp_hr_list = []
        for mins in range(4):
            temp_hr_list.append(0)
        hr_min_value_list.append(temp_hr_list)


    for time in TimeGenerator():
        hr_min_value_list[int(findHr(time))][int(findSev(time))-1] += 1
        #print("tiem:", time)
    
    # i=0
    # for hr in hr_min_value_list:
    #     print(i, "  ", hr)
    #     i += 1
        
    with open("timeFreq.csv", "w") as outfile:
        outfile.write("Hour,Min,Count_Corrected\n")
        for hrs in range(24):
            for mins in range(4):
                count = hr_min_value_list[hrs][mins]
                outfile.write(str(hrs)+','+str(mins+1)+','+str(count//25)+'\n')
            
main()