def classify_numbers(numbers):
    even_numbers = []
    odd_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    return even_numbers, odd_numbers

def main():
    userInput = input("Enter a list of numbers separated by spaces: ")

    numbers = [int(x) for x in userInput.split()]

    even_numbers, odd_numbers = classify_numbers(numbers)
    print("List of even numbers:", even_numbers)
    print("List of odd numbers:", odd_numbers)

if __name__ == "__main__":
    main()