def my_func(num_list):
    output = []
    
    for index in range(0, len(num_list)):
        current_num = num_list[index]
        
        if len(output) < 3:
            output.insert(0, current_num)
        elif current_num > output[0]:
            output[0] = current_num
        print(output)
        if len(output) > 1:
            for k in range(1, len(output)):
                if output[k] < output[k-1]:
                    temp_val = output[k]
                    output[k] = output[k-1]
                    output[k-1] = temp_val
        print(output)
    return output
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [24, 54, 14, 7, 5, 4, 6, 98, 65, 45]
list3 = [4, 5, 4, 3, 6, 7, 5, 16, 15, 14, 99, 66, 77]

                    
# print(my_func(list1))
print(my_func(list2))
# print(my_func(list3)