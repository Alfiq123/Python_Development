# Bubble Sort Algorithm in Python

def bubble_sort(numbers):
    """
    Sorts a list of numbers in ascending order using the Bubble Sort algorithm.

    Parameters:
    numbers (list): The list of integers or floats to sort.
    """

    # Outer loop for each pass through the list
    for pass_index in range(len(numbers)):

        # Inner loop for comparing adjacent elements
        for current_index in range(0, len(numbers) - pass_index - 1):

            # Get the current and next element
            current_number = numbers[current_index]
            next_number = numbers[current_index + 1]

            # If the current number is greater than the next one, swap them
            if current_number > next_number:
                # Swap the elements
                numbers[current_index] = next_number
                numbers[current_index + 1] = current_number

    return numbers


# Example usage:
unsorted_numbers = [-2, 45, 0, 11, -9]

# bubble_sort(unsorted_numbers)

# print('Sorted list in ascending order:')
print(bubble_sort(unsorted_numbers))


def bubble_sort_o(arr):
    """
    Sorts an array in ascending order using the optimized bubble sort algorithm.

    Args:
        arr (list): The list to be sorted (modified in place)
    """
    # Outer loop: tracks how many elements have been sorted
    for pass_num in range(len(arr)):

        # Flag to check if any swaps occurred this pass
        swapped = False

        # Inner loop: compares adjacent elements
        # We subtract pass_num because the last pass_num elements are already sorted
        for current_index in range(0, len(arr) - pass_num - 1):

            # Compare adjacent elements
            if arr[current_index] > arr[current_index + 1]:
                # Swap if they're in the wrong order
                current_value = arr[current_index]
                arr[current_index] = arr[current_index + 1]
                arr[current_index + 1] = current_value

                swapped = True

        # If no swaps occurred, the array is already sorted
        if not swapped:
            break


# Test the function
numbers_to_sort = [-2, 45, 0, 11, -9]
bubble_sort_o(numbers_to_sort)

print('Sorted Array in Ascending Order:')
print(numbers_to_sort)
