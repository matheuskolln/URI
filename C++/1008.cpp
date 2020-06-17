#include <iostream>
 
using namespace std;
 
int main() {
 
    int n, h;
    float v;
    cin >> n >> h >> v;
    cout << fixed;
    cout.precision(2);
    cout << "NUMBER = " << n << endl;
    cout << "SALARY = U$ " << h * v << endl;
 
    return 0;
}