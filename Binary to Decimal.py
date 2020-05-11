def binary_array_to_number(arr):
    print(arr)
    inh= ''.join(map(str, arr))
    print(inh)
    intj=int(inh)
    decnum=0
    power=0
    while intj>0:
        decnum+=2**power*(intj%10)
        intj//=10
        power+=1
    return decnum

lst=[1,1,1,1,1,2]
arr=lst
print(str(binary_array_to_number(arr)))