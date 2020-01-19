array = ''
with open(r'C:\Users\fnlse\Desktop\Fox\text_task1.txt') as file:
    array = file.read()

new_array = array.split('\n')
new_array = [int(item) for item in new_array]
print(new_array)

#90 процентиль
i = 0.9*(len(new_array) - 1) + 1
print(i)
i = int(i)
print(i)
        
