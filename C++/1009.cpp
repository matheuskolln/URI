#include <iostream>
 
using namespace std;
 
int main() {
 
    string n;
    double f, v;
    cin >> n >> f >> v;
    cout << fixed;
    cout.precision(2);
    cout << "TOTAL = R$ " << f + (0.15 * v) << endl;
 
    return 0;
}