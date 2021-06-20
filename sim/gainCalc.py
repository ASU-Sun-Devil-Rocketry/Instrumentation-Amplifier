### gainCalc -- Python Module for calculating digital gain setting resistances 
###             in a parallel resistor network. 
###
### Author: Colton Acosta, cacost12@asu.edu
###
### Date: 6/17/2021

## Library imports
import sys

## Function: dofCorrect -- ask user to renter data 
##           until dataType is an integer greater 
##           than 2 
def dofCorrect(inputData):
   try:
      inputData = int(inputData)
      if (inputData < 3):
         inputData = input("Invalid entry. Try again: ")
         dofCorrect(inputData)
      return inputData
   except ValueError:
      inputData = input("Invalid entry. Try again: ")
      dofCorrect(inputData)

## Function: methodCorrect -- ask user to renter the amplification 
##           method until entry is a valid choice
def methodCorrect(inputData):
   # Choices: 1, 2, 3, 4, 5
   maxChoice = 5
   minChoice = 1
   
   # Recursive Loop
   try:
      inputData = int(inputData)
      if(inputData < minChoice or inputData > maxChoice):
         inputData = input("Invalid choice. Try again: ")
         methodCorrect(inputData)
      return inputData
   except ValueError: 
      inputData = input("Invalid choice. Try again: ")
      methodCorrect(inputData)
      

## Class: gainNetwork -- class to contain all data and functions for calculating
##        the optimum parallel resistor configuration for programming the 
##        amplifier gain
## 
## Input Attributes: Input Range  -- range of input voltages, self.minVin to self.maxVin
##                   Output Range -- range of amplified outputs, self.minVout to 
##                                   self.maxVout
##                   Amplification Method -- Type of amplifier chip/circuit used
##                                           self.ampMethod
##                   Error Range -- Expected variance in raw output, used to determine 
##                                  range of useful programmable gains, self.inError
##                   DOF -- Degrees of freedom, number of resistors used to set the gain
##                          self.dof
##      
class gainNetwork:

   # Instantiate gainNetwork class with gain range and amplifier chip
   def __init__(self, Vinputs = [0,0], Voutputs = [0,0], ampMethod = 1, inError = 0.1, dof = 4):
      self.minVin = Vinputs[0]
      self.maxVin = Vinputs[1]
      self.minVout = Voutputs[0]
      self.maxVout = Voutputs[1]
      self.ampMethod = ampMethod
      self.inError = inError
      self.dof = dof

   # Method: enterInputs -- Get the input parameters from the terminal
   def enterInputs(self):
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
      print("Enter the amplification method:")
      print("   1. AD623 Instrumnetation Amp IC ")
      print()
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
      print("________________________________________________________________")
      print()

   # Method: calcTargets -- Calculate Target gain and offsets
   # Inputs: printTargets -- prints the target gain and offset along with the 
   #                         input parameters used in the calculation, boolean
   #                         value, does not print by default
   def calcTargets(self, printTargets = False):
      # Offset
      self.offset = self.minVout - self.minVin

      # Target gain
      maxVinOffset = self.maxVin + self.offset
      self.targetGain = self.maxVout/maxVinOffset

      # Print Results
      if(printTargets):
         # Inputs
         print("Input Parameters: \n")
         print("Input Signal: ", self.minVin, "-", self.maxVin, " V")
         print("Output Signal: ", self.minVout, "-", self.maxVout, "V")
         if(self.ampMethod == 1):
             print("Amplification Method: AD623 Instrumentation Amp IC")
         else:
             print("Amplification Method: Choice ", self.ampMethod)
         print("Input Error: ", self.inError*100, "%")
         print("Number of Resistors: ", self.dof)
         print("________________________________________________________________")

         # Targets
         print("Target Parameters: \n")
         print("Offset: ", self.offset, " V")
         print("Target Gain: ", self.targetGain)

   # Function: calcResist -- Calculate the resistance corresponding to a given 
   #                         gain
   # Inputs: gain -- target gain of the configuration, G
   #         method -- amplification method being used, method
   # Outputs: req -- equivalent resistance needed to achieve the target gain
   def calcResist(G, method):
      if(method == 1):
         req = 100000/(G-1)
      else:
         print("An invalid amplification code was encountered while calculating the gain resistance. Quitting the program ... ")
         sys.exit()


   # Method: calcResist -- Calculate the values of the resistors in the array
   #def calcResist(self):
                     


      
   
         
