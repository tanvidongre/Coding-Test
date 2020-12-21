"""to flatten the array from the nested array"""

def flatten_array(input_array):
    result_array = []
    for item in input_array:
        # for levels (nested list) in array  
        if type(item) is list:
            result_array.extend(flatten_array(item))
        # appending the element from the list
        else:
            result_array.append(item)
    return result_array 

if __name__ == '__main__':
    input_array = input()
    print(flatten_array(input_array))
