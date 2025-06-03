def bubble(un_list):
    """ Bubble Sort Algorithm """
    indexing_length = len(un_list) - 1  # `len()` is start with 1.
    is_sorted = False  # Check condition

    while not is_sorted:
        is_sorted = True
        for i in range(0, indexing_length):
            # If item in the left greater than item in the right,
            if un_list[i] > un_list[i + 1]:
                is_sorted = False
                # Flip two items.
                un_list[i], un_list[i + 1] = un_list[i + 1], un_list[i]
    return un_list

print(bubble(un_list = [1, 4, 6, 2, 8, 5, 1, 0, 7, 9, 4, 3]))


class BubbleSorter:
    """
    A class to encapsulate the bubble sort algorithm.
    Sorts a list in-place.
    """

    @staticmethod
    def bubble_sort(arr: list) -> None:
        """
        Sorts a list using the bubble sort algorithm in ascending order.
        Modifies the list in-place.

        Args:
            arr (list): The list of comparable elements to be sorted.
        """
        n = len(arr)
        # Traverse through all array elements
        for i in range(n - 1):
            # Last i elements are already in place, so no need to check them
            swapped = False  # Optimization: if no two elements were swapped
            # by inner loop, then the list is sorted.
            for j in range(n - 1 - i):
                # Traverse the array from 0 to n-i-1
                # Swap if the element found is greater than the next element
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

            # If no two elements were swapped by inner loop, break
            if not swapped:
                break


# --- How to use it ---

if __name__ == "__main__":
    # Create an instance of the sorter
    sorter = BubbleSorter()

    # Example 1: Sorting a list
    my_list_1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original list 1: {my_list_1}")
    sorter.bubble_sort(my_list_1)
    print(f"Sorted list 1  : {my_list_1}")  # The list is modified in-place

    print("═" * 50)

    # Example 2: Sorting another list using the same sorter instance
    my_list_2 = [5, 1, 4, 2, 8]
    print(f"Original list 2: {my_list_2}")
    sorter.bubble_sort(my_list_2)
    print(f"Sorted list 2  : {my_list_2}")

    print("═" * 50)

    # Example 3: Edge case - already sorted
    my_list_3 = [1, 2, 3, 4, 5]
    print(f"Original list 3: {my_list_3}")
    sorter.bubble_sort(my_list_3)
    print(f"Sorted list 3  : {my_list_3}")

    print("═" * 50)

    # Example 4: Edge case - empty list
    my_list_4 = []
    print(f"Original list 4: {my_list_4}")
    sorter.bubble_sort(my_list_4)
    print(f"Sorted list 4  : {my_list_4}")