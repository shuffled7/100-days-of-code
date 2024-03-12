# program to count elements of array using hashing
def main():

    num = int(input("Enter at max the amount of numbers valid: ")) # enter size of array
    array = [int(input(f"{i + 1} of {num}: "))for i in range(num)] # enter values into array

    default_value = 0 
    hash = [default_value] * 50     # initialize hash array of required length to 0
    for i in range(num):
        hash[array[i]] += 1         # iterate over input array's values and increment its equivalent hash array indexes


    query_amount = int(input("Enter the amount of numbers to check: ")) # enter amount of queries
    while (query_amount > 0):
        query_amount -= 1
        query_numbers = int(input("Enter the numbers to be checked:"))  # enter value of query
        print(hash[query_numbers])
main()