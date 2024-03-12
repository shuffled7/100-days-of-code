# program to count characters of string using hashing
def main():

    string = input("Enter characters: ") #enter string

    # pre compute
    default_value = 0 
    hash = [default_value] * 256    # initialize hash array of required length to 0 | length is 256 as there are 256 ASCII values
    for i in range(len(string)):
        hash[ord(string[i])] += 1   # using ord() to obtain ASCII value of character | iterate over input array's values and increment its equivalent hash array indexes

    query_amount = int(input("Enter the amount of characters to check: ")) # enter amount of queries
    while (query_amount > 0):
        query_amount -= 1
        query_characters = input("Enter the characters to be checked:")  # enter value of query
        # fetch
        print(hash[ord(query_characters)])
main()