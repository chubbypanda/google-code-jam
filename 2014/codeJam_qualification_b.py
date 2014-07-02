# code jam Qualification Round 2014, Problem B. Cookie Clicker Alpha, by k., 06/30/2014
# description at: https://code.google.com/codejam/contest/2974486/dashboard
# re-used code from Principles of Computing class, Mini-project 1

import math

class ClickerState:
    '''
    simple class to keep track of the game state
    '''
    
    def __init__(self):
        self._current_amount_of_cookies = 0.0
        self._current_time = 0.0
        self._current_cps = 2.0

    def get_cps(self):
        '''
        get current CPS, returns it as a float
        '''
        return self._current_cps

    def get_time(self):
        '''
        get current time, returns it as a float
        '''
        return self._current_time

    def time_until(self, cookies):
        '''
        return time until you have the given number of cookies
        (could be 0 if you already have enough cookies);
        '''
        if self._current_amount_of_cookies >= cookies:
            return 0.0
        else:
            # consider only the given number of cookies (without current resource)
            return (cookies - self._current_amount_of_cookies) / self._current_cps

    def wait(self, time):
        '''
        wait for given amount of time and update state, does nothing if time <= 0
        '''
        if time <= 0:
            pass
        else:
            self._current_time += time
            self._current_amount_of_cookies += time * self._current_cps
                        
    def buy_item(self, cost, additional_cps):
        '''
        buy an item and update state, does nothing if you cannot afford the item
        '''
        if cost > self._current_amount_of_cookies:
            pass
        else:
            self._current_amount_of_cookies -= cost
            self._current_cps += additional_cps
            

def read_file(filename):
    '''
    read and checks file for consistency, returns its content as a list
    '''
    with open(filename, 'r') as datafile:
         content = datafile.readlines()
         content = [line.strip('\n') for line in content]
    # there shall be (test cases) * number of lines
    if len(content) == int(content[0]):
        print 'Input file is incomplete/corrupted.'
    return content


def feeding_in(content):
    '''
    parsing through the raw list,
    returns its content as a list with item_cost, item_cps, X
    '''
    # stores and removes # of test cases
    test_cases = int(content.pop(0))
    # omitts empty spaces and converts strings to integers
    content = [map(float, line.split(' ')) for line in content]
    given_input = []
    for i in range(0, test_cases):
        given_input.append(content[i])
    return given_input

def simulate_clicker(given_input):
    '''
    function to run a Cookie Clicker game for the given duration with buying Farm;
    returns minimized time to achieve given value X
    '''
    with open('B-large-practice.out', 'w') as datafile:
        for row in xrange(len(given_input)):
            item_cost, item_cps, X = given_input[row]

            # initialize variables, n is for arbitrary value to hopefully avoid of local minima
            fastest_to_X = float('+inf')
            new_click = ClickerState()
            time_to_X_list = []
            n = 0
            
            while True:
                wait_time = new_click.time_until(item_cost)
                time_to_X = X / new_click.get_cps() + new_click.get_time()
                time_to_X_list.append(time_to_X)
                n += 1
                if n < X * 5:
                    new_click.wait(wait_time)
                    new_click.buy_item(item_cost, item_cps)
                    fastest_to_X = time_to_X
                else:
                    break
                       
            print 'Case #{0}: {1}'.format(row + 1, min(time_to_X_list))
            datafile.write('Case #{0}: {1}\n'.format(row + 1, min(time_to_X_list)))

# let's run it!
#read = read_file('B-large-practice.in')
#print simulate_clicker(feeding_in(read))

# Judged response for input B-small: Correct!
# Judged response for input B-large: Correct!


def clicker_alpha(given_input):
    '''
    function to run a Cookie Clicker game for the given duration with buying Farm;
    returns minimized time to achieve given value X,
    better/faster math from:
    https://github.com/KirarinSnow/Google-Code-Jam/blob/master/Qualification%20Round%202014/B.js
    '''
    with open('B-large-practice.out', 'w') as datafile:
        for row in xrange(len(given_input)):
            item_cost, item_cps, X = given_input[row]

            optimum = max(1, math.ceil(X / item_cost - 2 / item_cps))
            fastest_to_X = (X - item_cost) / (2 + (optimum - 1) * item_cps)
            for j in range(int(optimum)):
                fastest_to_X += item_cost / (2 + j* item_cps);
            
            print 'Case #{0}: {1}'.format(row + 1, fastest_to_X)
            datafile.write('Case #{0}: {1}\n'.format(row + 1, fastest_to_X))

# let's run it!
#read = read_file('B-large-practice.in')
#print clicker_alpha(feeding_in(read))


# let's run it!
#print simulate_clicker(30.0, 1.0, 2.0)
#print simulate_clicker(30.0, 2.0, 100.0)
#print simulate_clicker(30.5, 3.14159, 1999.19990)
#print simulate_clicker(500.0, 4.0, 2000.0)
