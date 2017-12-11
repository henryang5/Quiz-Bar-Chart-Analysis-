"""
Henry Ang
CSC 4800 Advanced Python
1/11/17
Lab 1 - Quiz Data Bar Chart Analysis

This program takes in a file with quiz dataset and outputs the file, smallest score, largest score and creates
frequency bar chart and a score bar chart.
"""

def start():
    """
    Asks user to input file and prints out the input file. If file is not found user will be prompted to enter another
    file name. Smallest score, largest score, and largest frequency is printed out. Frequency bar chart and Score bar
    chart created from data set file.
    """
    fileName = input('Enter input data filename: ')             # ask user to input fileName.
                                                         # files: quizdataset1.txt, quizdataset2.txt
    print('Reading file \'' ,fileName,'\''' input:' , sep="")   # prints user input, escape sequence \' for single quote

    score = []                  # list for all scores
    frequency = []              # list of all frequencies
    scoreFrequency = [0] * 51   # 0-50, list of scores and frequencies

    try:                                     # try-except for IO error
        with open(fileName, "r") as file:    # reads file and prints dataset, saves dataset into 3 lists

            for line in file:                                   # reads file by line
                token = line.split()                            # splits white spaces between score and frequency
                score.append(token[0])                          # adds score to score list
                frequency.append(token[1])                      # adds frequency to frequency list
                scoreFrequency[int(token[0])] += int(token[1])   # score = index in list, freq = index value

                print(line, end='')                             # prints entire file
        print()

    except IOError:                # exception error-handling if file not found
        print()
        print('The file \'',fileName,'\''' could not be found. Please enter another file name.', sep="")
        start()                    # calls for user to re-enter filename
        print()

    # calculate max score, min score, max Frequency, min Frequency
    minScore = caluculateSmallest(score)
    maxScore = caluculateHighest(score)
    maxFrequency = caluculateHighest(frequency)
    minFrequency = caluculateSmallest(frequency)

    # prints out smallest score, largest score, and largest frequency
    print()
    print('The smallest score value is', minScore,'')
    print('The largest score value is', maxScore, '')
    print('The largest frequency count is', maxFrequency,'')
    print()

    frequencyBarChart(minScore, maxScore, scoreFrequency)                         # calls frequency bar chart function
    scoreBarChart(minFrequency, maxFrequency, scoreFrequency, minScore, maxScore) # calls score bar chart function

def caluculateSmallest(list):
    """
    Calculates the smallest value in a list
    :parameter list
    :return    x
    """
    x = 9999999999999999          # choose a really high number
    index = 0
    for i in list:                # loops through entire list
        if int(list[index]) < x:  # compares with x for smaller number
            x = int(list[index])  # if smaller, x = smaller num
        index += 1                # increments to go to next index
    return x                      # returns smallest value

def caluculateHighest(list):
    """
    Calculates the largest value in a list
    :parameter list
    :return    x
    """
    x = -1                       # choose a really low number
    index = 0
    for i in list:               # loops through entire list
        if int(list[index]) > x: # compares with x for larger number
            x = int(list[index]) # if larger, x = larger num
        index += 1               # increments to go to next index
    return x                     # returns largest value

def frequencyBarChart(minimum, maximum, scoreFrequency):
    """
    Creates a frequency bar chart that shows the frequency of each score in the range of dataset.
    :parameter  int, int, list
    """
    print('----Input Data---')
    print('Score: Frequency Bar Chart')
    print()

    for i in range(minimum, maximum + 1):       #range(inclusive, exclusive) max + 1 to included all values
        astericks = ""
        if scoreFrequency[i] != 0:              # creates asterisk if freq not = 0
            astericks = '*' * scoreFrequency[i] # num asterisks = freq x *
        if scoreFrequency[i] > 10:              # formatting for 2 digit frequencies
            print(i ,':', '     ', scoreFrequency[i], '    ' , astericks )
        else:
            print(i, ':', '      ', scoreFrequency[i], '    ', astericks)

def scoreBarChart(minFrequency, maxFrequency, scoreFrequency, minScore, maxScore):
    """
    Creates a frequency bar chart that shows the score of each frequency by the range of dataset.
    :parameter  int, int, list, int, int
    """
    print()
    print('Frequency: Score Bar Chart')
    print()

    for i in range(maxFrequency, minFrequency - 1, -1): # range(inclusive, exclusive), decrements from max to min freq
        if i >= 10:                                     # formatting for 2 digit frequencies
            print('   ', '^  ', i, ': ', end='')
        else:
            print('   ', '^   ', i, ': ', end='')
        for j in range(minScore, maxScore + 1):         # nested loop of freq and score, maxscore to minscore + 1
            if i <= scoreFrequency[j]:                  # compares frequency in list to frequency on current line
                print('  *', end ='')                   # 2 white spaces and 1 asterisk
            else:
                print('   ', end ='')                   # 3 white spaces
        print()

    dashCarrot = "--^" * (maxScore - (minScore - 1))
    print ('-----------:', dashCarrot)                  # creates the x axis

    scoreRange = ""
    for i in range(minScore, maxScore + 1):             # loops from min score to max score + 1
        scoreRange = scoreRange + str(i) + ' '
    print('     ', 'Score:' , '', scoreRange)           # prints range of scores

def main():
    """
    Introduces the user to program and calls the start function to start the program.
    """
    print('Welcome to the Quiz Score Frequency Analyzer, written by Henry Ang')    # intro to program
    start()

if __name__ == "__main__":
    main()




