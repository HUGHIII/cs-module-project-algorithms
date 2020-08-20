'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    dupl = []
    new = []
    single = []

    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            dupl.append(arr[i + 1])
        else:
            new.append(arr[i])

    for i in range(len(dupl) - 1):
        if dupl[i] != new[i]:
            single.append(new[i])
        # if dupl[i] == new[i]:
        #     dupl.append(new[i])
        # else:
        #     single.append(new[i])

    return single       


l = [1,1,2,2,3,4,4]
print(single_number(l))

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")