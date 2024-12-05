#Jason Glotzbach filter input at defined threshold

def filter(lst,f):
    output = lst[:f]
    print(output) 

# example solution:
filter([1,2,3,4,5,6,7,8,9],6)