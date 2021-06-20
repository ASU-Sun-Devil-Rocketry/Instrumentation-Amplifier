### gainCalc -- Python Module for calculating digital gain setting resistances 
###             in a parallel resistor network. 
###
### Author: Colton Acosta, cacost12@asu.edu
###
### Date: 6/17/2021

## Function: dofCorrect -- ask user to renter data 
##           until dataType is an integer greater 
##           than 2 
def dofCorrect(inputData):
   inputData = input("Invalid entry. Try again: ")
   try:
      inputData = int(inputData)
      if (inputData < 3):
         dofCorrect(inputData)
      return inputData
   except ValueError:
      dofCorrect(inputData)

## Function: methodCorrect -- ask user to renter the amplification 
##           method until entry is a valid choice
def methodCorrect(inputData):
   # Choices: 1, 2, 3, 4, 5
   maxChoice = 5
   minChoice = 1
   
   # Recursive Loop
   inputData = input("Invalid choice. Try again: ")
   try:
      inputData = int(inputData)
      if(inputData < minChoice or inputData > maxChoice):
         methodCorrect(inputData)
      return inputData
   except ValueError: 
      methodCorrect(inputData)
      

## Class: gainNetwork -- class to contain all data and functions for calculating
##        the optimum parallel resistor configuration for programming the 
##        amplifier gain
## 
## Methods: __init__ -- get all input parameters from the user
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
      self.minVin = float(self.minVin)
      self.maxVin = float(self.maxVin)
      print()

      # Ask for target signal range 
      print("Enter the desired signal range: ")
      self.minVout = input("Minimum output voltage (V): ")
      self.maxVout = input("Maximum output voltage (V): ")
      self.minVout = float(self.minVout)
      self.maxVout = float(self.maxVout)
      print()

      # Ask for amplifier option 
      print("Enter the amplification method: \n")
      print("1. AD623 Instrumnetation Amp IC ")
      self.ampMethod = input("Enter your choice: ")
 
      # Check if amplfier option is valid
      self.ampMethod = methodCorrect(self.ampMethod)
      print()

      # Ask for input error
      self.inError =  input("Enter the error of the input signal (%): ")
      self.inError = float(self.inError)
      self.inError /= 100
      print()

      # Ask for degrees of freedom (number of resistors)
      self.dof = input("Enter the number of resistors: ")

      # Check if dof entry is valid 
      self.dof = dofCorrect(self.dof)   
      print()

   # Calculate Target gain
         
