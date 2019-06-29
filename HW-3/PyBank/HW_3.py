import os
import csv

csvpath = os.path.join('..', 'PyBank','budget_data.csv')

#variables
monthCount = 0
totalPL = 0
pretotal = 0
Diff = 0
maxDiff = 0
minDiff = 0
totalDiff = 0
Diffs = []

with open(csvpath,newline="") as csvfile:
   csvreader = csv.reader(csvfile,delimiter=",")
   csv_header = next(csvreader)
   print(f'Financial Analysis')
   print(f'-------------------')
   list = []

   for i in csvreader:
       month = i[0]
       total = i[1]
       Diff = int(total) - int(pretotal)
       list.append(i[1])

       if maxDiff < Diff:
           maxDiff = Diff
           maxDiffMonth = month
       if minDiff > Diff:
           minDiff = Diff
           minDiffMonth = month

       monthCount = monthCount + 1
       totalPL += int(total)


   for j in range(int(monthCount - 1)):
       Diff = int(list[j+1]) - int(list[j])
       totalDiff += Diff

       pretotal = month

avgDiff = totalDiff / (monthCount - 1)
averageDiff = round(avgDiff)


print(f'Total months: {monthCount}')
print(f'Total Profit: ${totalPL}')
print(f'Average Change: ${averageDiff}')
print(f'Greatest Increase in Profits: {maxDiffMonth} (${maxDiff})')
print(f'Greatest Decrease in Profits: {minDiffMonth} (${minDiff})')


output_file = os.path.join('..', 'PyBank', 'data_results.csv')

with open(output_file, "w") as file:
  file.write(f"Financial Analysis")
  file.write("\n")
  file.write(f"----------------------------")
  file.write("\n")
  file.write(f"Total months: {monthCount}")
  file.write("\n")
  file.write(f"Total Profit: ${totalPL}")
  file.write("\n")
  file.write(f"Average Change: ${averageDiff}")
  file.write("\n")
  file.write(f"Greatest Increase in Profits: {maxDiffMonth} (${maxDiff})")
  file.write("\n")
  file.write(f"Greatest Decrease in Profits: {minDiffMonth} (${minDiff})")