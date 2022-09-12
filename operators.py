1.KEY WORDS AVAILABLE IN PYTHON
   
  Keywor          Description
=============   ==================
  and	--->   A logical operator
  as	--->  To create an alias
 assert	--->  For debugging
 break	--->  To break out of a loop
 class	--->  To define a class
 continue ---> To continue to the next iteration of a loop
  def	 ---> To define a function
  del	---> To delete an object
 elif	---> Used in conditional statements, same as else if
 else	---> Used in conditional statements
 except	---> Used with exceptions, what to do when an exception occurs
False	---> Boolean value, result of comparison operations
finally	---> Used with exceptions, a block of code that will be executed no matter
             if there is an exception or not
for    --->  To create a for loop
from   --->  To import specific parts of a module
global --->  To declare a global variable
if	---> To make a conditional statement
import	---> To import a module
in      ---> To check if a value is present in a list, tuple, etc.
is	---> To test if two variables are equal
lambda	---> To create an anonymous function
None	---> Represents a null value
nonlocal---> To declare a non-local variable
not	---> A logical operator
or	---> A logical operator
pass	---> A null statement, a statement that will do nothing
raise	---> To raise an exception
return	---> To exit a function and return a value
True    ---> Boolean value, result of comparison operations
try	---> To make a try...except statement
while	---> To create a while loop
with	---> Used to simplify exception handling
yield   ---> To end a function, returns a generator

------------------------------------------------------------------------------------------------------------------
2.== VS IS OPERATORS

  --> ==  : is for value equality. It's used to know if two objects have the same value.
  -->  is : is for reference equality. It's used to know if two references refer (or point) to the same object, i.e if they're identical.

------------------------------------------------------------------------------------------------------------------------------
3./ // % DIFFERENCES

    '/'  Division  --> Divides left hand operand by right hand operand

    '//' Floor Division	--> The division of operands where the result is the quotient in which the digits after the decimal point are removed.
                            But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity) −

     '%' Modulus   -->	Divides left hand operand by right hand operand and returns remainder	

----------------------------------------------------------------------------------------------------------------------------------
         4.DECISION MAKING, LOOPS
===============================================



1.WHEN TO USE IF ELIF ELSE AND NESTEDIF
 
 A) if   --> python,if statement is used for decision making operations

    elif --> use the elif condition is used include multipleconditional expressions after the if condition or       
             b/w if and else conditions

    else -->  An if else Python statement evaluates whether an expression is true or false.
               If a condition is true, the “if” statement executes. Otherwise, the “else” statement executes

   nestedif --> There may be a situation when you want to check for another condition after a condition resolves to true

-------------------------------------------------------------------------------------------------------------------------------
2.WHILE VS FOR

       While loop – This loop statement checks for a condition at the beginning and till the condition is fulfilled, 
                    it will execute the body of the loop.

       For loop – For loops are used to sequentially iterate over a python sequence.
                  When the sequence has been iterated completely, the for loop ends and thus executes the next piece of code.
