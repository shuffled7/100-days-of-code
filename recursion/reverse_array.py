def reverse_array(input_array,length,start_index):

    #Base case
    if (start_index >= length//2):
        return input_array
    
    #swap the values
    input_array[start_index],input_array[length-start_index-1] = input_array[length-start_index-1],input_array[start_index]

    return reverse_array(input_array,length,start_index+1) 
    
def main():
    length = int(input("Enter the length of array: "))
    print("Enter values into array:")
    input_array = [int(input(f"{i+1} of {length}: ")) for i in range(length)]
    print("Reversed Array:",reverse_array(input_array,length,0))

main()
'''
#Using parameterised recursion
#passing parameters l=left most index & r=right most index
#passing length as parameter is not necessary, helpful for efficiency and flexibility

def reverse_array(input_array,length,l,r): 

    #Base case
    if (l >= r):
        return input_array
    
    #swap the values
    input_array[l],input_array[r] = input_array[r],input_array[l]

    return reverse_array(input_array,length,l+1,r-1) 
    
def main():
    length = int(input("Enter the length of array: "))
    print("Enter values into array:")
    input_array = [int(input(f"{i+1} of {length}: ")) for i in range(length)]
    print("Reversed Array:",reverse_array(input_array,length,0,length-1))
    
main()
'''