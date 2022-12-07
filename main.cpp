/*
Create a class ReverseFibonacci that can be constructed with an arbitrary number N. The class has one method `print` that it can call to print the first N numbers of the Fibonacci sequence in reverse order.

For example, if N is 5, the output should be 5 3 2 1 1.

The class should also have a destructor that prints a message when the object is destroyed. The class should be implemented in a file called `ReverseFibonacci.cpp` and the main program should be in a file called `assignment2.cpp`. The main program should create an object of the class and call the `print` method.
*/

#include "ReverseFibonacci.h"
#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        cout << "Usage: " << argv[0] << " N" << endl;
        return 1;
    }
    ReverseFibonacci rf(atoi(argv[1]));
    rf.print();
    return 0;
}
