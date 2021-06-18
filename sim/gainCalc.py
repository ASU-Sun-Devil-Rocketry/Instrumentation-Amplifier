### gainCalc -- Python Module for calculating digital gain setting resistances 
###             in a parallel resistor network. 
###
### Author: Colton Acosta, cacost12@asu.edu
###
### Date: 6/17/2021

class gainNetwork:

   # Instantiate gainNetwork class with gain range and amplifier chip
   def __init__(self):
      # User data queries
      print("Digitally Programmable Amplifier Input Parameters")
      print("________________________________________________________________")
      print()
 
      # Ask for Input signal range
      print("Enter the range of the input signal: \n")
      self.minVin = input("Minimum input voltage (V): ")
      self.maxVin = input("Maximum input voltage (V): ")
      print()

      # Ask for target signal range 
      print("Enter the desired signal range: ")
      self.minVout = input("Minimum output voltage (V): ")
      self.maxVout = input("Maximum output voltage (V): ")
      print()

      # Ask for amplifier option 
      print("Enter the amplification method: \n")
      print("1. AD623 Instrumnetation Amp IC ")
      self.ampMethod = input("Enter your choice: ")
      print()

      # Ask for input error
      self.inError =  input("Enter the error of the input signal (%): ")
      self.inError = float(self.inError)
      self.inError /= 100
      print()

   # Calculate Target gain
         
