This file contains instructions of how to execute the programs located at this directory, as well as how they return data and a rough idea of their behavior.

## opposite_signs.py
#### Input
This code receives 4 inputs. A function, an initial x, an interval i and a maximum number m of iterations.

#### What does it do?
It supposes that the given function is continuous, then, for it will try m times to find an interval such that f\(x\) \* f\(x \+ i\) \< 0. This means that the function crosses the X axis and it has bracketed a root.

#### Ouput
Returns false if it could not bracket a function; this can happen if the given interval was too large. Returns the interval \(an array\) if it was found.

#### how to run?
Supposing you have python3 installed, run the following command:
```python opposite\_signs.py \<file\> \<x\> \<interval\> \<max\_iteractions\>```
* \<file\> is the file that contains the function to be evaluated by python's eval(). e.g. the file containing the function x² -2 would have the following content \(without quotes\): "math.pow(x, 2) - 2"
* \<x\> is the start x for which the function will be applied: f\(x\)
* \<interval\> the interval which is going to be tested during each iteraction; i.e. it will test if the interval [f\(x\), f\(x + interval\)] brackets a root
* \<max\_iterations\> the desired max number of iterations

## lagrange_and_opposite_sign.py
#### Input
It receives 2 inputs: a function and an interval delta.

#### What does it do?
It applies the lagrange method to bracket a root and then applies the opposite sign method in order to tighten the interval. **LaGrange method will only work if, and only if, for the given polynomial there exists a coefficient c such that c < 0 AND for the polynomial with degree n, the coefficient __An__ < 0 AND the coefficient __A0__ ≠ 0**

#### Ouput
Returns the interval that brackets a root of the function.

#### how to run?
```python lagrange\_and\_opposite\_sign.py \<file\> \<interval\_delta\>```
* \<file\> is the file that contains the function. e.g. the file containing the function x² -2 would have the following content \(without quotes\): "1 0 -2"
* \<interval\_delta\> is the precision of the interval. For instance, consider the function x \- 1 \(which has root 1\) and precision 0.001; then, a possible output would be [0.9995, 1.0005]

## bissection.py
#### Input
This code receives 4 inputs. The file containing the function, the interval start, the interval end and the max number of iterations.

#### What does it do?
It executes the bissection method to the required interval. It will stop if either the max numer of iterations was reached or if it have found a root.

#### Output
Returns the closest found value to the root

#### How to run?
```python bissection.py <filename> <interval_start> <interval_end> <iterations>```
* \<filename\> is the file that contains the function to be evaluated by python's eval(). e.g. the file containing the function x² -2 would have the following content \(without quotes\): "math.pow(x, 2) - 2"
* \<interval\_start\> A float number representing the begginning of the interval that is bracketing a root
* \<interval\_end\> A float number representing the end of the interval that is bracketing a root
* \<iteration\> An integer number representing the maximum number of iterations for which the method will be executed

## secant.py
#### Input
This code receives 4 inputs. The file containing the function, the interval start, the interval end and the max number of iterations.

#### What does it do?
It executes the secant method to the required interval. It will stop if either the max numer of iterations was reached or if it have found a root.

#### Output
Returns the closest found value to the root

#### How to run?
```python secant.py <filename> <interval_start> <interval_end> <iteractions>```
* \<filename\> is the file that contains the function to be evaluated by python's eval(). e.g. the file containing the function x² -2 would have the following content \(without quotes\): "math.pow(x, 2) - 2"
* \<interval\_start\> A float number representing the begginning of the interval that is bracketing a root
* \<interval\_end\> A float number representing the end of the interval that is bracketing a root
* \<iteraction\> An integer number representing the maximum number of iterations for which the method will be executed

## fixed_point_iteration.py
#### Input
This code receives 4 inputs. The file containing the function, the starting value of x, the desired precision epsolon and the max number of iterations.

#### What does it do?
It executes the fixed point iteration method to the required interval. It will stop if either the max numer of iterations was reached or if it have found a root.

#### Output
Returns the closest found value to the root

#### How to run?
```python fixed_point_iteration.py <filename> <x> <epsolon> <iteractions>```
* \<filename\> is the file that contains the function to be evaluated by python's eval(). e.g. the file containing the function x² -2 would have the following content \(without quotes\): "math.pow(x, 2) - 2"
* \<x\> A float number representing the initial guess for the root
* \<epsolon\> A float number representing the desired precision
* \<iteraction\> An integer number representing the maximum number of iterations for which the method will be executed

## bnewton.py
#### Input
This code receives 6 inputs. The file containing the function, the interval start for bissection, the interval end for bissection, the max number of iterations for bissection method, the file containing the derivative function and the max number of iterations for the newton method.

#### What does it do?
It executes an hybrid approach. It runs the bissection method accordingly with the given parameters \(see [bissection.py](#bissection.py) for more info\). Then, it executes the newton method starting at the X found with bissection. It does not verify if the derivative function is correct. Newton's method will finish whenever it has found the root **or** it has executed the maximum number of iterations **or** it has reached the machine precision 

#### Output
Returns the closest found value to the root

#### How to run?
```python bnewton.py <function_filename> <interval_start> <interval_end> <iterations> <derivative_filename> <iterations_newton>```
* \<function\_filename\> is the file that contains the function to be evaluated by python's eval(). e.g. the file containing the function x² -2 would have the following content \(without quotes\): "math.pow(x, 2) - 2"
* \<interval\_start\> A float number representing the begginning of the interval that is bracketing a root. It will only be used for **Bissection's** method.
* \<interval\_end\> A float number representing the end of the interval that is bracketing a root. It will only be used for **Bissection's** method.
* \<iterations\_bissection\> An integer number representing the maximum number of iterations for which the **bissection** method will be executed.
* \<derivative\_\filename\> is the file that contains the derivative function to be evaluated by python's eval(). e.g. the file containing the function x² -2 would have the following content \(without quotes\): "math.pow(x, 2) - 2". This function will only be used for **Newton's** method
* \<iterations\_\newton\> An integer number representing the maximum number of iterations for which the **Newton's** method will be executed.