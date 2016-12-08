# Programmers:  Holly and Deb
# Course:  CS201.01, Dr. Olsen
# Date: November 30, 2016
# Programming Assignment:  PA6
# Problem Statement: To solve problems chosen by the user having to do with files on storms over years.
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
# Parameters: filename
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

def storm_graph_dict(storms_list1):
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
# Purpose:determine what storms happen in some years than others (add storm types to dictionary)
# Parameters:storm_list1
# Return:storm_dictionary


def storm_years(storm_list1):
    storm_dict = {}
    for line in storm_list1:
        if line[7] not in storm_dict:
            storm_dict[line[7]] = 1
        else:
            storm_dict[line[7]] += 1
    return storm_dict

# Function Name:storm_years_secondfile()
# Purpose:determine what storms happen in the second file based on user input
# Parameters:none
# Return:none


def storm_years_secondfile():
    file2 = input("Please enter another file you would like to input and compare to the original file")
    new_file = read_file(file2)
    storm_years(new_file)



# Function Name:comparison_of_years
# Purpose:compare two dictionaries and output how many more  storms of a certain type happen in a certaiyear
# Parameters:filename,dict_1,dict_2,outfile_name
# Return:none

def comparison_of_years(filename,dict_1,dict_2,outfile_name):
    inputfile=open(filename,"r")
    outputfile=open (outfile_name,"w")
    for key in dict_1:
        if key == dict_2:
            print(dict_1[key]-dict_2[key],file=outputfile)
    inputfile.close()
    outputfile.close()




# Function Name:common_storm
# Purpose:What is the most common storm for a particular state?
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


# Function Name:injuries_in_a_state
# Purpose:How many injuries in a specific state
# Parameters:storm_list, given_state2
# Return:how many injuries
def injuries_in_a_state(given_state2, storm_list1):
    total_injuries = 0
    for i in storm_list1:
        if given_state2 == storm_list1[6]:
            total_injuries += storm_list1[i][8]
    return total_injuries

# Function Name:menu
# Purpose:To give the choices to the users
# Parameters:none
# Return:choice
def menu():
    print("The choices you have to choose from to learn more about storms are: (A) A graph showing the number of storms in a certain month in a particular state,(B) most common storms that happened in a certain year,"+
          "(C) how many injuries from storms in a specific state, (D) most common storms that happened in a particular state ")
    choice = input("What would you like to know about storms?")
    return choice


# Function Name:main
# Purpose:run the overall program
# Parameters:none
# Return:none


def main():
    filename = inputFile()
    new_file = read_file(filename)
    choice = menu()
    if choice == "A":
        graph_dict =storm_graph_dict(new_file)
        storm_graph(graph_dict)
    if choice == "B":
        stormdict_1= storm_years(new_file)
        given_storm = input("Please enter a storm type in which you would like to find the year it occurred.")
        stormdict_2 = storm_years_secondfile(given_storm)
        outfile_name = input("Please enter the name of an output file.")
        comparison_of_years(filename,stormdict_1,stormdict_2,outfile_name)


    if choice == "C":
        given_state2 = input("Please input a state.")
        injuries =injuries_in_a_state(given_state2, new_file)
        print("The total injuries in this state are",injuries)
    if choice == "D":
        given_state = input("Please input a state.")
        common_storm(new_file, given_state)
        common_storm_max(new_file)
        print("The storm with the highest number of occurrences, occurred",common_storm_max(new_file),"times.")



main()