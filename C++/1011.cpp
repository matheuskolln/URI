#include <iostream>
 
using namespace std;
 
int main() {
 
    double r;
    cin >> r;
    cout << fixed;
    cout.precision(3);
    cout << "VOLUME = " << (4.0 / 3.0) * 3.14159 * (r * r * r) << endl;

 
    return 0;
}