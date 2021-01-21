#include <iostream>
using namespace std;

int main(){

  int num1;
  int num2;

  cout << "Enter the speed limit: ";
  cin >> num1;
  cout << "Enter the recorded speed of the car: ";
  cin >> num2;
  
  if (num2 <= num1){

    cout << "Congratulations, you are within the speed limit!";
  }
  else if(num2 - num1 >= 1  && num2 - num1 <= 20){

    cout << "You are speeding and your fine is $100.";
  }
  else if(num2 - num1 >= 21  && num2 - num1 <= 30){

    cout << "You are speeding and your fine is $270.";
  }
  else if(num2 - num1 >= 31 ){

    cout << "You are speeding and your fine is $500.";
  }

  return 0;
}
