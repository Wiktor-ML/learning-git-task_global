import random

def dice(number_of_throws):
    random_numbers_1 = []
    random_numbers_2 = []
    
    for _ in range(number_of_throws):
        random_numbers_1.append(random.randint(1, 6))
        random_numbers_2.append(random.randint(1, 6))
    
    return random_numbers_1, random_numbers_2        

random_numbers_1, random_numbers_2 = dice(5)

#print(random_numbers_1)
#print(random_numbers_2)

set_of_throws = set()

for i, number in enumerate(random_numbers_1):
    t = tuple([random_numbers_1[i],random_numbers_2[i]])
    #print(t)
    set_of_throws.add(t)
    

print(set_of_throws)

#for key, value in num_dict.items():
#    print(f"({key}, {value})")