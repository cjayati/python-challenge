import os
import csv


csvFile = os.path.join("resources", "budget_data.csv")

dates=[]
profits=[]
max_inc = 0
max_dec = 0
max_inc_date = 0
max_dec_date = 0

with open(csvFile) as file :
    csvreader = csv.DictReader(file, delimiter=",")
    for index, row in enumerate(csvreader):
        dates.append(row["Date"])
        profits.append(int(row["Profit/Losses"]))
        if(index>0):
            profit_change = profits[index]-profits[index-1]
            if(profit_change>max_inc):
                max_inc=profit_change
                max_inc_date=dates[index]
            elif(profit_change<max_dec):
                max_dec=profit_change
                max_dec_date=dates[index]

    
    total = len(dates)
    avg_profit = (profits[total-1]-profits[0])/(total-1)
    #print("Total Months: {}". format(str(total)))
    #print(str(sum(profits)))
   # print("%.2f" %avg_profit)
    #print(max_inc)
    #print(max_inc_date)
    #print(max_dec)
    #print(max_dec_date)

    output = """
    Financial Analysis
    ----------------------------
    Total Months: {}
    Total: ${}
    Average Change: ${}
    Greatest Increase in Profits: {} (${})
    Greatest Decrease in Profits: {} (${})
    """ .format(str(total), str(sum(profits)), "%.2f" %avg_profit, max_inc_date, str(max_inc), max_dec_date ,str(max_dec))

    ### printing the output in terminal
    print(output)

    ### writing the output in text file
    textFile = os.path.join("analysis", "output.txt")
    with open(textFile, "w") as f:
        f.write(output)