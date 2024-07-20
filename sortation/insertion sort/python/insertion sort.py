def set_arr_length():
    while True:
        try:
            len = int(input("please enter array length: "))
            if len <= 0:
                raise ValueError("Array length must be positive")
            return len
        except ValueError as e:
            print(f"Invalid input: {e}")

def create_array(len):
    arr = [None] * len
    for i in range(len):
        try:
            number = int(input(f"please enter value in {i} : "))
            arr[i] = number
        except ValueError as e:
            print(f"Invalid input for element {i}: {e}")
            return None

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def main():
    try:
        len = set_arr_length()
        arr = create_array(len)
        if arr is None:
            print("Error creating array")
            return
        arr = insertion_sort(arr)
        for num in arr:
            print(num)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

