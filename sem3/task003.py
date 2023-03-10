#[1, 2, 3, 4]

list= [1, 2, 4, 3, 5, 7]
count=0
for i in range(0, len(list)-1):
    if list[i+1]> list[i]:
        count+=1
print(count)