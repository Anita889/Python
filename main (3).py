def sum_of_elements(numbers,exclude_negative):
    sum = 0
    if exclude_negative == True:
        for item in numbers:
            if item>0:
                sum+=item
            else:
                continue
    else:
         for item in numbers:
             sum+=item
    return sum

def main():
    userInput = input("enter a list of numbers separated by spaces: ")
    numbers = [int(x) for x in userInput.split()]
    check = input("Do you want to exclude negative ones?(Yes or No): ")
    exclude_negative = check.startswith('y')

    result_sum = sum_of_elements(numbers, exclude_negative)
    print("Sum:", result_sum)
if __name__ == "__main__":
    main()