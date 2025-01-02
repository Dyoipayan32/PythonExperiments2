def is_prime(num):
    """
    Checks if a number is prime.
    :param num: The number to check.
    :return: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Check for factors up to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # If a factor is found, the number is not prime

    return True  # If no factors are found, the number is prime


print(is_prime(53))
# # Example usage:
# user_input = int(input("Enter a number (0 to 10000): "))
# if is_prime(user_input):
#     print(f"{user_input} is a prime number.")
# else:
#     print(f"{user_input} is not a prime number.")
