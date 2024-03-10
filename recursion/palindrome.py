
# program to check if string is Palindrome or not
def is_palindrome(array,length,index):

    # base case 
    if (index >= length//2): # checks till halfway point of list
        return True
    
    if (array[index] != array[length - index - 1]): # checks if char does not match the symmetric char
        return False
    
    return is_palindrome(array,index+1) # increment index to check next pair of characters

def main():
    string =  input("Enter a string to check if it is Palindrome or not:")
    array = list(string) # convert string  to a  list
    length = len(array)  # store the length  i.e. num of characters
    result = is_palindrome(array,length,0)
    print(result)

main()
'''
# A more Pythonic way
def is_palindrome(string):
    string = string.lower()  # Convert the string to lowercase
    reversed_string = string[::-1]  # Reverse the string using slicing

    return string == reversed_string  # Check if the original string is equal to the reversed string

def main():
    string = input("Enter a string to check if it is Palindrome or not: ")
    result = is_palindrome(string)
    print(result)

main()
'''