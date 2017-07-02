list1 = [43, 54, 67, 34, 54, 65, 97, 75, 32]
list2 = [12,54,65,78,43,65,87,34,23,32]
list3 = [76,43,76,24,78,43,26,37,38,39,73]

def sort(li):
    return sorted(li)

li1 = sort(list1)
li2 = sort(list2)
li3 = sort(list3)

len1 = len(list1)
len2 = len(list2)
len3 = len(list3)
minavg = (li1[0]+li1[1]+li2[0]+li2[1]+li3[0]+li3[1])/6
maxavg = (li1[len1-1]+li1[len1-2]+li2[len2-1]+li2[len2-2]+li3[len3-1]+li3[len3-2])/6

print(minavg)
print(maxavg)
