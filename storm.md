#Storm Data PA6

##Problem
There are many different storms that happen throughout the USA on a given day, month, or year. 
Your goal is to analyze data about storms across all US cities to find trends.

##Details
You must create a progrma that can read in all data from the file, store it in a list, and then answer questions about that data.

###File Info
The file has the following values comma-delimited:
* The year and month in the format YYYYMM in which the storm started 
* The day of the month in which the storm started
* The time at which the storm started
* The year and month in the format YYYYMM in which the storm ended
* The day of the month in which the storm ended
* The time at which the storm ended
* The name of the state where storm occurred
* The type of storm
* The number of injuries directly caused by the storm
* The number of injuries indirectly caused by the storm
* The number of deaths directly caused by the storm
* The number of deaths indirectly caused by the storm
* The amount of damage to property
* The amount of damage to crops

You have multiple files of the same format. Each file has data for an entire year of storms in the USA. The user chooses which one to use as input.

###Program Abilities
Your program must answer the following questions:
* Do some months have more storms than others? Create a graph that displays the number of storms overall per month throughout the year (i.e. the number of total storms in January, then February, etc). 
* Do more storms happen in some years than others? Ask the user for a second file as input. Then compare how many more storms of each type happened in this year versus the first input file (note that your answer may be negative if fewer occurred). Output this information to a file so that on each line you have a storm type followed by the difference between years.
* What is the most common storm for a particular state? The user provides the state.
* A question of your choosing!

The user should be given a menu to choose options from, and can continue to choose options until they choose to quit.

If you are a group of 3, you will need to answer the following questions as well:
* What is the most common storm for a particular month in a particular state? The user provides the month and the state.
* One more question of your choosing!

###Error Checking
You must have all standard file error checking. You do not need to do any further value error checking, other than that if you can't find an answer (for instance, the user gives an invalid state), you must tell the user that no data was found. 
Be sure to implement good comparisons for string input so that case and whitespace don't cause it to not work correctly.

Be careful with your file, as many of the damage amounts are empty. Check for "" (empty string) before typecasting if you use those values in your own question.
