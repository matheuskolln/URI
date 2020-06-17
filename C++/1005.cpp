#include <iostream>
 
using namespace std;
 
int main() {
 
    double a, b;
    cout << fixed;
    cout.precision(5);
    cin >> a >> b;
    cout << "MEDIA = " << (a * 3.5 + b * 7.5) / 11 << endl;
    
    return 0;
}