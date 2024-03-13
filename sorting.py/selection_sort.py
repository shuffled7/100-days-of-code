# selection sort algorithm to sort array in ascending order
# selection sort: pulls minimum to the start / select minimums & swap

def selection_sort(array, length): # consider length = 5

    for i in range(length - 1):     # since last indexed value will eventually be the greatest, run loop till 1 less than
        minimum = i                 # i loop: 0 to 3

        for j in range(i,length):   # j loop: i to 4
            if array[j] < array[minimum]:   # if arr[i to 4] < arr[0] 
                minimum = j
            
        array[i],array[minimum] = array[minimum],array[i] # swap
        print(f"Step {i+1}: {array}")
        
def main():

    length = int(input("Enter the length of array: "))
    array = [int(input(f"{i+1} of {length}: ")) for i in range(length)]
    print("Initial array:",array)

    selection_sort(array, length)

    print("Final:",array)

main()