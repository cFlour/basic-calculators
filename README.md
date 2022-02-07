# Basic Calculators

Basic calculators made by me.

## How to use?

Select the file for which you want the calculator. The files are named according to the figures for which the calculators are. Copy the contents of the file into Visual Studio code (if you are on a computer) or Jupyter notebook. If you are on mobile, copy it to pyroid.
Then run the file, enter the neccesary inputs and lo! the calculator works. The things for which use instructions aren't provided are pretty straightforward.

Few things to be noted:
* Everything is case sensitive. So, `Plus` is not the same as `plus`.
* In most of the places, you need to enter the numerical value of the input asked, not the name in words.
* Ignore the .github/workflows folder.

# File-by-file usage

## [Numeral Calculator](https://github.com/cFlour/basic-calculators/blob/main/numeric-calc.py)

This one is used for addition, subtraction, multiplication, division, exponents, roots and percentage. For the `First Number` input, put the first number you want in your operation (eg. for 34+16, first number input should be 34). For the `Operation` input, put the mathematical symbol of the operation to perform (+,-,*,/,^,√,% respectively). For the `Second Number` input, put the second number of the operation (in the above given example, this value would be 16).

#### Use in root, percentage and exponents

When you want to find the root of a number (lets say sqrt of 32), the usage here is:
First number - 32
Operation - √
Second number - 2        (the 2 means square root. if its put as 3, it finds the cube root of the first number)

For percentage, it will find how much percent the first number is of the second number.

For exponents, the first number is the original number and the second number is the x'th power of the first number (Eg if first number is 4 and second is 3, it finds the value of the 3rd power of 4).

Example:
![calcvid](https://i.imgur.com/kuugXKi.webm)

## [Calendar](https://github.com/cFlour/basic-calculators/blob/main/calendar.py)

The calendar just tells you which day of the week did a certain date fell on or will fall on. Here, in the year input, enter 4 digit year number and in the month input, enter two digit month number.

Example:
![image](https://user-images.githubusercontent.com/79126652/152731140-2c2b9dbb-75ed-4c42-8f8d-b26c10330711.png)
