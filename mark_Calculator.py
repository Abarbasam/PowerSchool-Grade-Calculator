import sys

rawTextFile = sys.argv[1]
textFile = open(rawTextFile, 'r')

marks = []

# Obtaining only the fractions from the file
for line in textFile:
    fraction = line.split()[-1]
    marks.append(str(fraction))

# To get the average, we must divide by the total numver of assessments
amountOfAssessments = len(marks)
sumOfMarks = 0



def numbify(string):
    return float(''.join(string))

# A more efficient eval() function
for i in marks: # Iterating through the fractions
    evaluatingDenominator = False

    numerator = [] # Contains the numerator number
    denominator = [] # Contains the denominator number

    # Evaluating the fraction itself
    for j in i:
        if j != '/' and not evaluatingDenominator: # Getting the numerator
            numerator.append(j)
        elif j != '/' and evaluatingDenominator: # Getting the denominator
            denominator.append(j)
        else:
            evaluatingDenominator = True

    sumOfMarks += (numbify(numerator) / numbify(denominator))

print (sumOfMarks / amountOfAssessments) * 100 # Average mark
