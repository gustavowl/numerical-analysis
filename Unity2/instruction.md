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
* \<file\> is the file that contains the function. e.g. the file containing the function x² -2 would have the following content \(without quotes\): "1 0 -2"
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