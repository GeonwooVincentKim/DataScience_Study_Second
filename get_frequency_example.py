a = [1, 2, 3, 3, 5, 5, 5, 9, 10]
b = []
    
count = 0
many_frequency_number = 0
for i in a:
    if(i not in b):
        b.append(i)
        
    elif(i in b):
        print(a, count)
        count += 1
        many_frequency_number = i
        
print("Many Frequency Number : {0} - Count : {1}".format(many_frequency_number, count))
