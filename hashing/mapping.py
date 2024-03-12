# mapping values in dictionary to count number of elements in an array
def main():

    num = int(input("Enter at max the amount of numbers valid: ")) # enter size of array
    array = [int(input(f"{i + 1} of {num}: "))for i in range(num)] # enter values into array

    # pre-compute
    map = {}
    for i in range(num):
        map[array[i]] = map.get(array[i], 0) + 1
        # when you try to access a key that doesn't exist, it raises a KeyError by default. If the specified key is not found in the dictionary, the get() method returns a default value (0) instead of raising an error. If the key already exists in the dictionary, its corresponding value is updated i.e. + 1

    query_amount = int(input("Enter the amount of numbers to check: ")) # enter amount of queries
    while (query_amount > 0):
        query_amount -= 1
        query_number = int(input("Enter the numbers to be checked:"))  # enter value of query
        # fetch
        print(map.get(query_number, 0)) 

main()