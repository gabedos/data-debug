from src.datadebug import logger, List

def bubble_sort(arr: List):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                arr.customize_node(j, color="green")
                arr.customize_node(j+1, color="red")
                logger.visualize()

# Example list
my_list = List([64, 34, 25, 12, 22, 11, 90], display_edges=False, display_index=False, label="BubbleSort")

# Sorting the list in place using bubble sort
bubble_sort(my_list)

# Printing the sorted list
print("Sorted list:", my_list)
