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

python opposite_signs.py \<file\> \<x\> \<interval\> \<max\_iteractions\>

\<file\> is the file that contains the function. e.g. the file containing the function x² -2 would have the following content \(without quotes\): "1 0 -2"

\<x\> is the start x for which the function will be applied: f\(x\)

\<interval\> the interval which is going to be tested during each iteraction; i.e. it will test if the interval [f\(x\), f\(x + interval\)] brackets a root

\<max\_iteractions\> the desired max number of iterations