# PalindromeCheck-
Program to determine if the content of a text file is a Palindrome

DESCRIPTION
===========

A palindrome is a word or sentence that is spelled the same backwards and forwards. A simple of example of this is Swedish pop sensation ABBA, which, when written backwards, is also ABBA. Their hit song (and winner of the 1974 Eurovision Song Contest!) "Waterloo" is not a palindrome, because "Waterloo" backwards is "Oolretaw".
Palindromes can be longer than one word as well. "Solo gigolos" (the saddest of all gigolos) is a palindrome, because if you write it backwards it becomes "Sologig olos", and if you move the space three places back (which you are allowed to do), that becomes "Solo gigolos".
This program that detects whether or not a particular input is a valid palindrome.

INPUTS

On the first line of the input, there should be a number specifying how many lines of input to read. After that, the input consists of some number of lines of text that the program will read and determine whether or not it is a palindrome or not.
The only important factor in validating palindromes is whether or not a sequence of letters is the same backwards and forwards. All other types of characters (spaces, punctuation, newlines, etc.) are ignored, and whether a character is lower-case or upper-case is irrelevant.

OUTPUTS

The program outputs "Palindrome" if the input is a palindrome, "Not a palindrome" if it's not.

SAMPLE INPUTS 

Input 1

3
Was it a car
or a cat
I saw?
Output 1

Palindrome

Input 2

4
A man, a plan, 
a canal, a hedgehog, 
a podiatrist, 
Panama!
Output 2

Not a palindrome
