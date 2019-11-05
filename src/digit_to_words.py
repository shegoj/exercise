#!/usr/bin/python3
__author__    = "OluSegun Ojewale"
__version__   = "$Revision: beta $"
'''
program converts numbers into words:
Example 1:

Input: 123
Output: "One Hundred Twenty Three"

Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
'''

import sys

# using a class for translation implementation so as to make it easy to abstract details and easy future ehancements

class DigitsTranslation ():
    ''' numbers dictionary'''
    numbers_dictionary ={
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        15: 'Fifteen',
        18: 'Eighteen'
        20: 'Twenty ',
        40: 'Forty ',
        80: 'Eighty'
    }

    TEEN_SUFFIX = 'teen'
    tens_SUFFIX = 'ty '


    # break digit down into millions, thousands, hundreds, tens, units & comma delimited
    def digest_translate (self, digit):

        #check if there is a match in dictionary and return
        if digit in self.numbers_dictionary:
            return self.numbers_dictionary [digit]

        # break numbers down into groups...
        millionth  = digit // 1000000
        thousandth = ((digit % 1000000) // 1000)
        hundredth  = (((digit % 1000000) %  1000) // 100)
        tens       = ((((digit % 1000000) %  1000) % 100) //10)
        units      = (((((digit % 1000000) %  1000) % 100) % 10))
        tens_and_units = tens*10 + units
        digits_in_words      = "" # this to build up return string

        if millionth > 0 :
            digits_in_words = digits_in_words + self.digest_translate (millionth) + " Million "
        if thousandth > 0 :
            digits_in_words = digits_in_words + self.digest_translate (thousandth) + " Thousand "
        if hundredth > 0 :
            digits_in_words = digits_in_words  + self.digest_translate (hundredth ) + " Hundred "
        if (tens_and_units) in self.numbers_dictionary:
            digits_in_words = digits_in_words + self.numbers_dictionary [tens_and_units]
        elif tens == 1: # 16-19
            digits_in_words = digits_in_words + self.digest_translate (units) + self.TEEN_SUFFIX
        elif tens > 0  or units > 0 :  #21-99
            if (tens *10) in self.numbers_dictionary:
                digits_in_words = digits_in_words + self.numbers_dictionary [tens *10]
            else:
                digits_in_words = digits_in_words + self.digest_translate (10 + tens) + self.tens_SUFFIX
                digits_in_words = digits_in_words.replace ("teen","")
            if units != 0:
                digits_in_words = digits_in_words + self.numbers_dictionary [units]

        return digits_in_words



#main body here
if __name__=="__main__":
    console_param = sys.argv [1]
    MAX_NUMBER = 999999999
    try:
        # Let's  make sure we are dealing with only positive numerals
        given_number = int (console_param)
        if given_number < 0 or given_number > MAX_NUMBER:
            raise ValueError ()
        try:
            translator = DigitsTranslation()
            numbers_in_words = translator.digest_translate (given_number)
            print ("{} ".format(numbers_in_words))
        except (Error) as e:
            print ("error {}".format (e))
            exit (1)
    except ValueError:
        print (" {} is not valid ".format (console_param))
        sys.exit(1)
    except Error:
        print ("error {}".format (e))
