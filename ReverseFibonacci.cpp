#include "ReverseFibonacci.h"
#include <iostream>

using namespace std;

ReverseFibonacci::ReverseFibonacci(int n)
{
    this->n = n;
    fib = new int[n];
    fib[0] = 1;
    fib[1] = 1;
    for (int i = 2; i < n; i++)
    {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
}

ReverseFibonacci::~ReverseFibonacci()
{
    cout << "Object destroyed" << endl;
    delete[] fib;
}

void ReverseFibonacci::print()
{
    for (int i = n - 1; i >= 0; i--)
    {
        cout << fib[i] << " ";
    }
    cout << endl;
}
