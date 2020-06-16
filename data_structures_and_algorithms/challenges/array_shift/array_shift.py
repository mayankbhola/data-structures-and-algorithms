import sys, math

"""
Input ::    input_list - list of elements
            element -  element to be inserted at middle index in list

Output ::   new_list - new list with element inserted at middle index of input list

Complexity ::
    Time - Linear O(N)
    Space - Linear O(N)

"""
def insertion(input_list, element) :
    
    new_list = []
    index = int((math.ceil((len(input_list))/2.0)))
    
    for i in range(index) :
        new_list.append(input_list[i])

    new_list.append(element)

    for i in range(index, len(input_list)) :
        new_list.append(input_list[i])

    return new_list


"""
Input ::    input_array - stringified version of list and element in list format
        
Output ::   input_list - python list
            element - element to be inserted in list at middle index

Complexity ::
    Time - Linear O(N)
    Space - Linear O(N)

"""
def validation(input_array) :

    if len(input_array) != 2 :
        raise Exception("Invalid input")

    input_list = input_array[0]
    element = input_array[1]

    if (not element) or str.isspace(element) :
        raise Exception("element is None")

    if (not input_list) or str.isspace(input_list) :
        raise Exception("Input list is None")

    input_list = eval(input_list)
    element = eval(element)

    print("Input list : {}, Element : {}".format(input_list, element))
    return input_list, element
    

if __name__ == "__main__":
    
    try :
        input_array = raw_input("Input the list and element to insert :: ").rsplit(",", 1)

        input_list, element = validation(input_array)
        new_list = insertion(input_list, element)
        
        print("Output list : {} ".format(new_list))
    
    except Exception as exception :
        print("Exception :: {}".format(exception))



