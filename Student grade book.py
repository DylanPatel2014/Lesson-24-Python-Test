report={"bob":91,"dylan":99,"greg":68,"lisa":72,"sadeya":100}
sum=0
for i in report:
    sum+=report[i]
avg=sum/len(report)
print("The average of the results of the test is",avg)
maximum=max(report.values())
print("The highest score on the test is",maximum)
max_scorer=max(report,key=report.get)
print("The higest scorer was scored by",max_scorer)

minimum=min(report.values())
print("The lowest score on the test is",minimum)
min_scorer=min(report,key=report.get)
print("The lowest scorer was scored by",min_scorer)

name=input("Please enter a name to see if they attended the test: ")
student=report.get(name)
if student is not None:
    print(f"{name} mark is {student}")
else:
    print("Student not found")