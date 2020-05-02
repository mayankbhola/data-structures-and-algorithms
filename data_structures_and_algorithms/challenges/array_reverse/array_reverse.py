"""
Func :: Reverse the array in-place

Input :: arr - Array to be reversed

Output :: arr - Reversed Array

Time Complexity :: Linear - O(n)

Space Complexity :: Constant - O(1) 
"""
def reverse(arr) :
    low = 0
    high = len(arr)-1
    while low <= high :
        arr[low], arr[high] = arr[high], arr[low]
        low+=1
        high-=1


def validate(input_list) :

    """ if enter is pressed without giving any input then raw_input returns empty str"""
    if (not input_list) or (str.isspace(input_list)) :
        raise Exception("Input is None")

    """ converts string input to list """
    input_list = eval(input_list)

    if len(input_list) == 0 :
        raise Exception("Input list is empty")

    """ validate if all elements of list are integer """
    if not all(isinstance(elem, int)for elem in input_list) :
        raise Exception("Invalid input. Elements can only be integer")

    return input_list


if __name__ == "__main__" :

    """ ** Taking input array as list ** """
    input_list = raw_input("Enter input as list of elements : ")

    try :
        """ validate the list elements"""
        input_list = validate(input_list)
        
        """ *** reverse the list """
        reverse(input_list)
        
        print("Reversed list :: {}".format(input_list))
        
    except Exception as exception :
        print("Exception :: {}".format(exception))


