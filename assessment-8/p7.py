def merge_lists(list1, list2):
    return list1 + list2

list1 = list(map(int, input("Enter first list elements separated by space: ").split()))
list2 = list(map(int, input("Enter second list elements separated by space: ").split()))

print("Merged List =", merge_lists(list1, list2))