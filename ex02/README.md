The goal with this exercice is to write a function that takes an
integer and return its equivalent in gray code.

More info about gray code : https://en.wikipedia.org/wiki/Gray_code

To convert an integer in it's equivalent in gray code, one method is taking result
from the exclusif OR between the base integer right shifted once and the base integer\n
So for 7 we would have :\n 
  0111 -> base int\n
^ 0011 -> shifted base int\n
-------\n
  0100 -> binary result that will just be converted by the Python interpreter when
          printing the result
