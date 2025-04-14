from os import remove

numbers =[100,300,200,600,400,500]
print(numbers)

unique_set = set(numbers)
print(unique_set)

jobs = ("Android","Web","IT","Doaa","Ahmed","Mohamed")
print(jobs)

unique_jobs = set(jobs)
print(unique_jobs)

print(len(unique_jobs))

# Remove Item from set using discard
print("Remove item from list set: ")
unique_jobs.discard("Android")
print(unique_jobs)