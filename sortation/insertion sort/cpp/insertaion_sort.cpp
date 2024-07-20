#include <iostream>

using namespace std;

int set_arr_length()
{
    int len;
    cout << "please enter array length: ";
    cin >> len;
    return len;
}

int *create_array(size_t len)
{
    int *arr = new int[len];
    for (size_t i = 0; i < len; i++)
    {
        int number;
        cout << "please enter value in " << i << " : ";
        cin >> number;
        arr[i] = number;
    }
    return arr;
}

int *insertion_sort(int arr[], int len)
{
    for (int i = 1; i < len; i++)
    {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
         arr[j + 1] = key;
    }
    return arr;
}

int main()
{
    int len = set_arr_length();

    int* arr = create_array(len);

    arr = insertion_sort(arr, len);

    for (size_t i = 0; i < len; i++)
    {

        cout << arr[i] << endl;
    }

    delete[] arr;

    return 0;
}