import sys

def main():
    # Verify that two numbers were provided as arguments
    if len(sys.argv) != 3:
        print("Error: Please provide exactly two numbers.")
        print("Usage: docker run <image_name> <num1> <num2>")
        sys.exit(1)

    try:
        # Convert arguments to floats to handle both integers and decimals
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])

        result = num1 + num2

        # Print the clean result (strip trailing .0 if it's a whole number)
        if result.is_integer():
            print(f"Result: {int(result)}")
        else:
            print(f"Result: {result}")

    except ValueError:
        print("Error: Both arguments must be valid numbers.")
        sys.exit(1)

if __name__ == "__main__":
    main()
