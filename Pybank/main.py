import os 

import csv

file_input = os.path.join(".","Resources","budget_data.csv")
file_output = os.path.join(".","analysis","budget_analysis.txt")

# variables
total_months=0
total_net=0
net_change = 0
dates = []
profits = []
#start with loop to read file
with open(file_input) as csv_data:
    reader=csv.reader(csv_data)

    header = next(reader) 

    #first 
    first_row=next(reader)
    total_months+=1
    total_net+=int(first_row[1])
    previous_net=int(first_row[1])
    

    for row in reader:
        #Keeping track of dates
        dates.append(row[0])
        


        #Calculate net change and save it 
        
        net_change = int(row[1])-int(previous_net)
        profits.append(net_change)
        previous_net=int(row[1])

        #Update Variables
        total_months= total_months+1
        total_net+=int(row[1])
        
    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    avg_change = sum(profits)/len(profits)

    #print findings
    print("Financial Analysis")
    print("-----------------------")
    print("Total Months:" + str(total_months))
    print("Total: $" + str(total_net))
    print("Average Change: $" + str(round(avg_change, 2)))
    print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
    print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

#Export to .txt file
output = open(file_output, "w")

line1 = "Financial Analysis"
line2 = "-----------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_net)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))