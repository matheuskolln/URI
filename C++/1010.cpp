#include <iostream>
 
using namespace std;
 
int main() {
    float total;

    for (int i = 0; i <= 1; i ++){
        int c, n;
        float v;
        cin >> c >> n >> v;
        total = total + (n * v);
    }
    cout << fixed;
    cout.precision(2);
    cout << "VALOR A PAGAR: R$ " << total << endl;
    
    return 0;
}