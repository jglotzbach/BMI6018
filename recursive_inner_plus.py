#Jason Glotzbach inner list problem using recursion

def innerloop_plus1(lst):
    for element in lst:
            if isinstance(element, list):
                return innerloop_plus1(element)
    output_list = [x + 1 for x in lst]
    print(output_list)

# example solution:
innerloop_plus1([1,[2,3,[4,[7,9,[22,99],8,2],5],6,7,8],9])