# code jam Qualification Round 2014, Problem A. Magic Trick, by k., 06/28/2014
# description at: http://code.google.com/codejam/contest/2974486/dashboard


def read_file(filename):
    '''
    read and checks file for consistency, returns its content as a list
    '''
    with open(filename, 'r') as datafile:
         content = datafile.readlines()
         content = [line.strip('\n') for line in content]
    # there shall be (test cases) * 5 (4 rows + card) * 2 (twice) + 1 (test cases line) lines
    if len(content) != int(content[0]) * 5 * 2 + 1:
        print 'Input file is incomplete/corrupted.'
    return content
    
def feeding_in(content):
    '''
    parsing through the raw list, returns two lists of first and second rows
    '''
    # stores and removes # of test cases
    test_cases = int(content.pop(0))
    # omitts empty spaces and converts strings to integers
    content = [map(int, line.split(' ')) for line in content]
    first_row = []
    second_row = []
    # first answer is always at 0th, 10th, 20th, ... position, pointing to a row
    for i in range(0, test_cases * 10, 10):
        index = int(content[i][0])
        row = content[i + index]
        first_row.append(row)
    # second answer is always at 5th, 15th, 25th, ... position, pointing to a row
    for j in range(5, test_cases * 10, 10):
        index = int(content[j][0])
        row = content[j + index]
        second_row.append(row)
    return first_row, second_row

def compare_rows(pairs):
    '''
    unpacks & compare two given lists (rows) against each other,
    returns info on the screen and file with results
    '''
    first_row, second_row = pairs
    result = ''
    with open('codeJam_a_results.txt', 'w') as datafile:
        for row in xrange(len(first_row)):
            # converts a list (row) from each list to a set and intersects them
            first_set = set(first_row[row])
            second_set = set(second_row[row])
            intersection = list(first_set & second_set)
            if not intersection:
                result = 'Volunteer cheated!'
            elif len(intersection) == 1:
                result = intersection[0]
            else:
                result = 'Bad magician!'
                
            print 'Case #{0}: {1}'.format(row + 1, result)
            datafile.write('Case #{0}: {1}\n'.format(row + 1, result))

# let's run it!
read = read_file('A-small-practice.in')
compare_rows(feeding_in(read))

# Judged response for input A-small: Correct!
