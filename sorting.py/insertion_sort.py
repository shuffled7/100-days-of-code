# insertion sort algorithm to sort array in ascending order
# insertion sort: takes an element and swaps till its placed in its correct order

def insertion_sort(array,length):       # consider length 5

    for i in range(1,length):           # i loop: 1 to 4
        j = i

        while(j > 0 and array[j-1] > array[j]): # j > 0, since j>=0 will make arr[j-1] an error | compare to the left
            array[j-1],array[j] = array[j],array[j-1]   # swap
            j -= 1
        print(f"Step{i}: {array}")

def main():

    length = int(input("Enter the length of array: "))
    array = [int(input(f"{i+1} of {length}: ")) for i in range(length)]
    print("Initial array:",array)

    insertion_sort(array, length)

    print("Final:",array)

main()