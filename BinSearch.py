def binSearch(list, item):
    low = 0
    high = len(list)-1
    mid = (low + high) // 2
    # If item is in the second half of the list
    while list[mid] < item:
        low = mid
        mid = (low + high) // 2
        print(f"New mid value is: {list[mid]}")
        while list[mid] > item:
            high = mid
            mid = (low + high) // 2
            print(f"New mid value is: {list[mid]}")
    # If item is in the first half of the list
    while list[mid] > item:
        high = mid
        mid = (low + high) // 2
        print(f"New mid value is: {list[mid]}")
        while list[mid] < item:
            low = mid
            mid = (low + high) // 2
            print(f"New mid value is: {list[mid]}")
    if list[mid] == item:
        print(f"Binary search completed item found: {list[mid]}")
        return(list[mid])
