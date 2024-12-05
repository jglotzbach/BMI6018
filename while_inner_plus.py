#Jason Glotzbach module 5 assignment inner list using while loop

def innerloop_plus1(lst):
    while any(isinstance(element, list) for element in lst):
        for element in lst:
            if isinstance(element, list):
                lst = element
                break
    output_list = [x + 1 for x in lst]
    print(output_list)

# example solution:
innerloop_plus1([1,[2,3,[4,[7,9,2],5],6,7,8],9])