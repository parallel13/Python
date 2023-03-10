# напишите код который заменяет оценки но наоборот (1>5, 5<1)
array = [int(i) for i in input().split()]

def Change(array):
    min = array[0]
    max = array[0]
    for i in array:
        if i> max:
            max = i
        if i < min:
            min = i
    for i in range(len(array)):
        if array[i]== max:
            array[i]= min
    return array

print(Change(array))

