# Programmers:  Holly and Deb
# Course:  CS201.01, Dr. Olsen
# Date: November 30, 2016
# Programming Assignment:  PA6
# Problem Statement:
# Data In: input file name, output file name,
# Data Out:  specified storm information based on user input
# Other files needed: Stormdata_2000_shortened.csv,Stormdata_2001_shortened.csv,Stormdata_2002_shortened.csv,Stormdata_2003_shortened.csv
#Stormdata_2004_shortened.csv,Stormdata_2009_shortened.csv,Stormdata_2011_shortened.csv,Stormdata_2012_shortened.csv,Stormdata_2013_shortened.csv
# Credits: None

# Purpose: Ask the user for a filename
# Parameters: none
# Return: filename
def inputFile():
    import os
    filename = input("Please input a file to read from.")
    # create a loop to error check
    while not os.path.exists(filename):
        filename = input("Error. That is not a valid file name. Please try again.")
    return filename  # return the given file name


#Purpose: read from the file
#Paramaters:none
#Return:list
 def process_file(filename):
     try:
         storm_list1={}
         file=open(filename,"r")
         for line in file:
            storm_list1.append(line.split(","))
     file.close()
    except FileNotFoundError:
    print("Sorry File Not Found")
    return storm_list1







Function Name:process_file
Purpose:To read from the file
Parameters:filename
Return:storm list
Algorithm:
1.)try
2.)create an empty list
3.)open the file that the user inputs
4.)for every line in the file
    a.split line at the comma
    b.append line to the empty list
5.)close the input file
6.)except an error
    a.)output "Sorry File Not Found"
    b.)end the program
7.)return the list