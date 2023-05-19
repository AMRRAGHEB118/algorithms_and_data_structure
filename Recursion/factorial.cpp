#include <iostream>
using namespace std;

int factorial(int num)
{
    if (num == 0 || num == 1) // Base Case
        return 1;
    else
        return num * factorial(num - 1);
}

int main()
{
    unsigned int num;
    cout << "Enter a non-negative number: ";
    cin >> num;
    if (num < 0)
    {
        cout << "Error: input number must be non-negative." << endl;
        return 1;
    }
    int result = factorial(num);
    cout << "The factorial of " << num << " is: " << result << endl;
    return 0;
}
