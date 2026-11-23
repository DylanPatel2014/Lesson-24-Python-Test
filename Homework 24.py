scores={"dylan":100,"timmy":32,"sadeya":99,"aria":54,"connor":91}
total=0
for i in scores:
    total+=scores[i]
average=total/len(scores)
print("The average of the results of the test is",average)
maximum=max(scores.values())
print("The highest score on the test is",maximum)
maximum_scorer=max(scores,key=scores.get)
print("The higest scorer was scored by",maximum_scorer)
minimum=min(scores.values())
print("The lowest score on the test is",minimum)
minimum_scorer=min(scores,key=scores.get)
print("The lowest scorer was scored by",minimum_scorer)


name=input("Please enter a name to see if they attended the test: ")
student=scores.get(name)
if name=="dylan":
    print("He attended the test and scored",student)
elif name=="timmy":
    print("He attended the test and scored",student)
elif name=="sadeya":
    print("He attended the test and scored",student)
elif name=="aria":
    print("He attended the test and scored",student)
elif name=="connor":
    print("He attended the test and scored",student)
else:
    print(name,"did not enter the test")
