Created on Fri Sep  4 18:38:12 2020

@author: Hadi Rouhani
"""
## Import Libraries >>>>>
#from textwrap import wrap
import math


# Main Function Call >>>>>
# n: An integer considered as an input whose square root is to be calculated
def oldsqrt(n):
   n = int(n*int(1e20))
   two_digit_string = digit_sep(n)
   residue_digits = str(object='')
#    while True:
   for next_digit in two_digit_string:
       residue_digits = residue_digits + next_digit
       for num in range(1,11):
           if two_digit_string.index(next_digit) == 0:
               res_subtract = int(residue_digits) - num**2
               if res_subtract >= 0:
                   continue
               else:
                   res_num = str(num - 1)
                   divisor_num = str(int(res_num)*2)
                   next_num = str(int(residue_digits)-(num-1)**2)
                   break
           else:
               res_subtract = int(residue_digits) - (int(divisor_num )*10+num)*num
               if res_subtract >= 0:
                   continue
               else:
                   res_num = res_num + str(num - 1)
                   if num - 1 == 0:
                       next_num = str(int(residue_digits))
                   else:
                       next_num = str(int(residue_digits) - (int(divisor_num )*10+(num-1))*(num-1))
                   divisor_num = str(int(divisor_num)*10 + (num-1)*2)
                   break
               
               
       residue_digits = next_num      
   res_num = str(int(res_num)/1e10)
   return res_num
       
def digit_sep(n):
   digit_n = str(n)
   two_digit_string = []
   if len(digit_n)%2==0:
#       two_digit_string = wrap(digit_n,2)
      two_digit_string = [digit_n[i:i+2] for i in range(0,len(digit_n),2)]
   else:
#       two_digit_string = wrap(digit_n[1:],2)
      two_digit_string = [digit_n[i:i+2] for i in range(1,len(digit_n),2)]
      two_digit_string.insert(0,digit_n[0])
   return two_digit_string
   
   
############## Example:
if __name__ == "__main__":
    n = 325161232141232
    string_n = digit_sep(n) 
    print(string_n)
    e = oldsqrt(n)       
    print('The Square root of ',str(n),' is ',str(e),'Actual result is:',str(math.sqrt(n)))
