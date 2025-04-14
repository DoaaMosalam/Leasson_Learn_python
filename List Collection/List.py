jobs = [1,"Android",2,"It","Web",3,"Service","Front","Back","Android",True,False]
print(jobs)

print(jobs[0:3])
print(jobs.index("Service"))

#concatenation between two list
jobs2 =["account","teacher"]
print(jobs2 + jobs)

#extend add two list in one list
jobs.extend(jobs2)
print("Extend two list . \t" ,jobs)

jobs.append("flutter")
print(jobs)
#sort
print("Sort List is: ")
jobs2.sort()
print(jobs2)

print(jobs.count("Android"))

# insert item in index
jobs.insert(1,"Android")
print(jobs)

jobs.pop()
print(jobs)
# reverse  list
jobs.reverse()
print("reverse list . \t" ,jobs)

jobs.remove("Android")
print(jobs)

jobs.clear()
print(jobs)

