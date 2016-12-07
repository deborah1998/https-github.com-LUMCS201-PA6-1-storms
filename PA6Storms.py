# Programmers:  Holly and Deb
# Course:  CS201.01, Dr. Olsen
# Date: November 30, 2016
# Programming Assignment:  PA6
# Problem Statement:
# Data In: input file name, output file name,
# Data Out:  specified storm information based on user input
# Other files needed: Stormdata_2000_shortened.csv,Stormdata_2001_shortened.csv,Stormdata_2002_shortened.csv,Stormdata_2003_shortened.csv
# Stormdata_2004_shortened.csv,Stormdata_2009_shortened.csv,Stormdata_2011_shortened.csv,Stormdata_2012_shortened.csv,Stormdata_2013_shortened.csv
# Credits: None

# Purpose: Ask the user for a filename
# Parameters: none
# Return: filename

import os


def inputFile():
    filename = input("Please input a file to read from.")
    # create a loop to error check
    while not os.path.exists(filename):
        filename = input("Error. That is not a valid file name. Please try again.")
    return filename  # return the given file name


# Purpose: read from the file
# Paramaters:filename
# Return:list

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


# Function Name:storm_graph
# Purpose:To generate a graph for the storms per month
# Parameters:storm list
# Return:graph

def storm_graph_dict(storms_list1): # Shoud be dictionary******
    import pylab
    graph_dict = {}
    for graph_dict in storms_list1:
        if storms_list1[0][4:5] not in graph_dict:
            graph_dict = 1
        else:
            graph_dict += 1
    return graph_dict


# Function Name:storm_graph
# Purpose:To generate a graph for the storms per month
# Parameters:storm list
# Return:graph
def storm_graph(graph_dict):
    keys_list = graph_dict.keys()
    values_list = graph_dict.values()

    pylab.ploy(keys_list,values_list)
    pylab.ylabel("Number of Storms")
    pylab.xlabel("Month")
    pylab.title("Number of Storms per month")


# Function Name:storm_years
# Purpose:Do more storms happen in some years than others
# Parameters:storm list
# Return:none


def storm_years(storm_list1):
    storm_dict={}
    for line in storm_list1:
        if line[7] not in storm_dict:
            storm_dict[line[7]] = 1
        else:
            storm_dict[line[7]] += 1
    return storm_dict



def storm_years_secondfile(given_storm):
    file2=input("Please enter another file you would like to input and compare to the original file")
    new_file=read_file(file2)
    storm_years(new_file)


# Function Name:comparison_of_years
# Purpose:
# Parameters:
# Return:

def comparison_of_years(outfile_name,dict_1,dict_2):
    outputfile=open (outfile_name,"w")
    for key in dict_1.keys():
        if key in dict_2.keys():
            print(dict_1[key]-dict_2[key],file=outputfile)
    outputfile.close()




# Function Name:common_storm
# Purpose:What is the most common storm for a particular state?  **Line is not the variable - find out what you're looking for
# Parameters:storm_list, given_state **** If everything else works, make print(line) and see what comes out
# Return:storm_dict
def common_storm(storm_list1,given_state):
    storm_dict = {}
    for line in storm_list1:
        if line[5] == given_state:
            if line[7] not in storm_dict:
                storm_dict[line[7]] = 1
            else:
                storm_dict[line[7]] += 1
    return storm_dict

# Function Name:common_storm_max
# Purpose:Find the max value in a dictionary
# Parameters:storm_dict
# Return:max_value
def common_storm_max(storm_dict):
    biggest_value = 0
    for key in storm_dict:
        if int(key[1]) > biggest_value:
            biggest_value = int(key[1])
    return biggest_value


# Function Name:injuries_state
# Purpose:How many injuries in a specific state
# Parameters:storm_list, given_state2
# Return:how many injuries
def injuries_in_a_state(given_state2, storm_list1):
    total_injuries = 0
    if given_state2 == storm_list1[6]:
        for i in storm_list1:
            total_injuries += storm_list1[i][8]
    return total_injuries


def menu():
    print("The choices you have to choose from to learn more about storms are most  common storms that happened in a certain year,"+
          " how many injuries from storms in a specific state,most common storms that happened in a particular state ")
    choice = input("What would you like to know about storms?")
    return choice

def main():
    filename = inputFile()
    new_file = read_file(filename)
    print(common_storm_max(new_file))
    user_state=("Ple")
main()