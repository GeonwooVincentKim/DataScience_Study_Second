a = [1, 2, 3, 3, 5, 5, 5, 9, 10]
b = []
    
count = 0
many_frequency_number = 0
for i in a:
    if(i not in b):
        b.append(i)
        
    elif(i in b):
        # print(a, count)
        many_frequency_number = i
        count += 1
        # print("Many Frequency Number : {0} - Count : {1}".format(many_frequency_number, count))
        # many_frequency_number = i
        # print("Many Frequency Number : {0} - Count : {1}".format(many_frequency_number, count))
        

# get_previous_frequency_number = 0
# get_next_frequency_number = 0
# temp_value = 0
# for i in a:
#     for j in a:
#         get_previous_frequency_number = i
#         get_next_frequency_number = j
#         print(get_next_frequency_number)
        
#         if(get_previous_frequency_number < get_next_frequency_number):
#         #     # print("Bigger")
#             temp_value = get_previous_frequency_number
#             get_previous_frequency_number = get_next_frequency_number
#             get_previous_frequency_number = temp_value
#             print("temp Value : {0}".format(temp_value))
        
#         elif(get_previous_frequency_number > get_next_frequency_number and many_frequency_number == count):
#             temp = get_next_frequency_number
#             get_next_frequency_number = get_previous_frequency_number
#             get_next_frequency_number = temp_value
#             print("temp Value 23 : {0}".format(temp_value))
#         #     many_frequency_number = get_previous_frequency_number
        
#         # elif(get_previous_frequency_number < get_next_frequency_number):
#         #     many_frequency_number = get_next_frequency_number
    
    
print("Many Frequency Number : {0} - Count : {1}".format(many_frequency_number, count))
# print("{0}".format())
    

# for i in b:
#     # get_previous_frequency_number = many_frequency_number
#     print("Many Frequency Number : {0} - Count : {1}".format(i, count))
    

