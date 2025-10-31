def linear_search(un_list, target):
    """ Linear Search """
    length = len(un_list)
    for i in range(0, length):
        if un_list[i] == target:
            return i
    return -1


# Use Case
result = linear_search(un_list=[2, 4, 0, 1, 9, 3, 7, 6], target=6)
if result == -1:
    print("Element not found")
else:
    print("Element found at index: ", result)


class LinearSearch:
    def __init__(self, un_list=None):
        """Initialize with an optional list to search."""
        self.un_list = un_list if un_list is not None else []

    def linear_search(self, target):
        """ Linear Search """
        length = len(self.un_list)
        for i in range(0, length):
            if self.un_list[i] == target:
                return i
        return -1
