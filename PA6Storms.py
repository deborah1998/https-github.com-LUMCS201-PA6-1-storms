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
#Paramaters:filename
#Return:list

def read_file(filename):
    storms_list1 = []
    try:
        inputfile=open(filename,"r")
        for line in inputfile:
            storms_list1.append(line.split(","))
        inputfile.close()
    except FileNotFoundError:
        print("Sorry this file is not Found")
        SystemExit(1)
    return storms_list1


#Function Name:storm_graph
#Purpose:To generate a graph for the storms per month
#Parameters:storm list
#Return:graph

def storm_graph(storms_list1):
import pylab
x,y = [],[]
jan_count = 0
feb_count = 0
mar_count = 0
apr_count = 0
may_count = 0
jun_count = 0
jul_count = 0
aug_count = 0
sep_count = 0
oct_count = 0
nov_count = 0
dec_count = 0
for line in storms_list1:
    if storms_list1[0][4:5] == "01":
        jan_count += 1
    if storms_list1[0][4:5] == "02":
            feb_count += 1
    if storms_list1[0][4:5] == "03":
        mar_count += 1
    if storms_list1[0][4:5] == "04":
        apr_count += 1
    if storms_list1[0][4:5] == "05":
        may_count += 1
    if storms_list1[0][4:5] == "06":
        jun_count += 1
    if storms_list1[0][4:5] == "07":
        jul_count += 1
    if storms_list1[0][4:5] == "08":
        aug_count += 1
    if storms_list1[0][4:5] == "09":
        sep_count += 1
    if storms_list1[0][4:5] == "10":
        oct_count += 1
    if storms_list1[0][4:5] == "11":
        nov_count += 1
    if storms_list1[0][4:5] == "12":
        dec_count += 1
        storms_list1[0][4.5].append
        storms_list1.append y
    pylab.ploy (x,y)
    pylab.ylabel("")



#1.)Ask the user for a new file to input
#2.)call the process_file function for the user's new file(read from the new file)
#3.)open the output file
#4.)for line in file 1
#5.)for line in new file
#6.)for i in range of the length of storms list
#a.)if storm _list1[0][0:4] equals storms list2[0][0:4] ([0][0:4]the first four letters in the index to get the year)
    #b.)print storms list[0][0:4] to the file(the storm in the specific year from both files)
#7.)close the output file







#Function Name:storm_years
#Purpose:Do more storms happen in some years than others
#Parameters:storm list
#Return:none

def storm_years():
    try:
        new_file2=input("Please enter the name of the new file yould like to input ")
        storm_list2 =read_file(new_file2)
        for line in storm_list2



# Function Name:common_storm
# Purpose:What is the most common storm for a particular state?
# Parameters:storm_list, given_state
# Return:max_value
def common_storm(storm_list1,given_state):
    storm_dict = {}
    for each line in list
        if storm_list1[5] == given_state:
            if storm_list1[7] not in storm_dict:
                storm_dict [storm_list1[7]] = 1
            otherwise
            storm_dict[storm_list1[7]] += 1
b.find max value in dictionary
d.
return max_value

# Function Name:injuries_state
# Purpose:How many injuries in a specific state
# Parameters:storm_list, given_state
# Return:how many injuries
def injuries_in_a_state(given_state, storm_list1):
    total_injuries = 0
    if given_state == storm_list1[6]:
        for i in storm_list1:
            total_injuries += storm_list1[i][8]
    return total_injuries

def main():
    filename =inputFile()
    new_file =read_file(filename)
    print(new_file)
main()