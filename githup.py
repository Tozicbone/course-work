import math
root=math.sqrt(9)
print("root is =",root)
counter=1
print("PLEASE INPUT YOUR DATE OF BIRTH IN NUMBERS SO THAT I CAN TELL YOU HOW MUCH YOU HAVE IN YOUR BANK ACCOUT")
myNum1=int(input("DAY:")) 
myNum2=int(input("MONTH:"))
myNum3=int(input("YEAR:"))
mySum=myNum1+myNum2*myNum3
print(mySum)
print("RICH ASS MOTHERFUCKER don't spend all on stupid shit your mum will say")
def sub_sort(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low

def quick_sort(array,low,high):
    if low < high:
        key_index = sub_sort(array,low,high)
        quick_sort(array,low,key_index)
        quick_sort(array,key_index+1,high)


array = [8,10,9,6,4,16,5,13,26,18,2,45,34,23,1,7,3]
print (array)
quick_sort(array,0,len(array)-1)
print (array)
