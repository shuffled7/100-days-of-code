# selection sort algorithm to sort array in ascending order

def selection_sort(array, length):

    for i in range(length - 1):     # since last indexed value will eventually be the greatest, run loop till 1 less than
        minimum = i                 
        for j in range(i,length):
            if array[j] < array[minimum]:
                minimum = j
            
        array[i],array[minimum] = array[minimum],array[i]
        print(f"Step {i+1}: {array}")
        
def main():

    length = int(input("Enter the length of array: "))
    array = [int(input(f"{i+1} of {length}: ")) for i in range(length)]
    print("Initial array:",array)

    selection_sort(array, length)

    print("Final:",array)

main()