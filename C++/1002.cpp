#include <iostream>
 
using namespace std;
 
int main() {
 
    double a;
    cin >> a;
    cout << fixed;
    cout.precision(4);
    cout << "A=" << 3.14159 * (a * a) << endl;
 
    return 0;
}