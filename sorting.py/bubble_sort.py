# bubble sort algorithm to sort array in ascending order
# bubble sort: pushes maximum to the last by adjacent swaps

def bubble_sort(array,length):      # consider length 5
    step = 0

    for i in range(length,0,-1):    # decrementing i loop: 5 to 1
        did_swap = 0                # is a check for sorted input array
        
        for j in range(i-1):        # j loop: 0 to 3,2,1
            if array[j] > array[j+1]:   # checking adjacent values
                array[j],array[j+1] = array[j+1],array[j] # swap
                did_swap = 1

            step += 1
            print(f"Step{step}: {array}")
        if did_swap == 0:
            break

def main():

    length = int(input("Enter the length of array: "))
    array = [int(input(f"{i+1} of {length}: ")) for i in range(length)]
    print("Initial array:",array)

    bubble_sort(array, length)

    print("Final:",array)

main()