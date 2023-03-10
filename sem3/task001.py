#задача 19. смещение вправо на К

#s= [1, 2, 3, 4, 5, 6, 7]
#k= int()
#temp = None
#for i in range(0,k):
#    for j in range(len(s)-1, 0, -1):
#        temp = s[j]
#        s[j]= s[j-1]
#        s[j-1]= temp
#print(s)
        
list1= [1, 2, 3, 4, 5, 6, 7]
k= int(input('введите число K:'))
list1= list1[-k:] + list1[:-k]
print(list1)