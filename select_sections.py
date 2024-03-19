def select_sections(occupancy_probability):
    """
    Function description: This function finds the n sections with the lowest total occupancy rate, where n is the number of rows in the input matrix. Each row
    must have one section removed, subject to the condition that sections selected for removal in two adjacent rows must be in the same or adjacent columns. 
    Only one section can be removed from each row. The function eturns a tuple containing the minimum total occupancy rate and the locations of the section 
    selected for removal.

    Approach description: First, we create a 2D array called memo, with dimensions n x m, to store the minimum total occupancy for removing i sections from the 
    top j columns of the first i rows. We extracted the n and m values from the occupancy_probability matrix.
    Next, the first row of the memo matrix is filled with the corresponding values from the occupancy_probability matrix. This serves as a base case for the dynamic
    programming approach.

    For each subsequent row of the occupancy_probability matrix, the function iterates over each section in the row and considers three possible options for selecting 
    a section to remove: the section directly above, the section diagonally above and to the left, and the section diagonally above and to the right.

    The function calculates the minimum total occupancy for each option, then it adds the occupancy probability of the current section to the minimum, and stores 
    those values in the corresponding cell of the memo matrix. Additionally, the function also keeps track of which option was chosen for each cell, by appending 
    the index of the chosen section to the select_sections list.

    Once all the cells in the memo matrix have been filled, the function finds the minimum value in the last row of the memo matrix, which represents the minimum 
    total occupancy rate for a set of n sections. The corresponding set of sections is then extracted from the select_sections list and returned, along with the minimum
    total occupancy rate as a tuple.

    
    The recurrence formula used in the code is:
    memo[i][j] = occupancy_probability[i][j] + min(memo[i-1][j-1]), memo[i-1][j], memo[i-1][j+1])
    The recurrence formula is used in the nested loop in the implementation to compute the minimum possible occupancy at each position in the memo list.


    Given that n is the number of rows and m is the number of columns in the occupancy_probability matrix:
    
    The time complexity for this algorithm is of O(nm), since we have a nested loop that iterates over each position in the memo list, which has dimensions n x m.

    The auxiliary space complexity for this algorithm is O(nm), since we created a memo list with dimensions n x m to store the minimum possible occupancy at each 
    position in the matrix.
    

    :Input: 
        occupancy_probability: A list of lists with columns of length 'm' and rows of length 'n'. occupancy_probability[i][j] is an integer number between 0 and 100 
        which represents the occupancy probability for a section located at rows 'i' and column 'j'.


    :Output: A tuple containing the minimum total occupancy rate and a list of tuples representing the locations of the sections selected for removal. Each tuple 
    contains two integers, the first representing the row index and the second representing the column index.


    :Time complexity: O(nm), where n is the number of rows and m is the number of columns

    :Aux space complexity: O(nm), where n is the number of rows and m is the number of columns
    """

    n = len(occupancy_probability)      # Length of occupacny_probability
    m = len(occupancy_probability[0])   # Width of occupancy_probability
    
    memo = [[None for j in range(m)] for i in range(n)]     # Initialises memo and elements in memo table to None
    memo[0] = occupancy_probability[0]  # Sets first row of memo to first row of occupancy_probability

    select_sections = []    # Initialises empty list used to keep track of sections selected

    # Iterates over remaining rows and columns of memo
    for i in range(1, n):
        for j in range(m):
            options = []    # Creates a list of options

            # If current element is not in left-most column, then append element that is above to the left to options
            if j > 0:
                options.append(memo[i-1][j-1])
            options.append(memo[i-1][j])

            # If current element is not in right-most column, the append element that is above to the right to options
            if j < m-1:
                options.append(memo[i-1][j+1])

            min_option = min(options)   # Finds smallest value in options and assign it to min_option
            memo[i][j] = occupancy_probability[i][j] + min_option   # Sets current element in memo to the sum of occupancy_probability at current position

            # Checls if smallest value in memo equal to element directly above to the left of current element
            if min_option == memo[i-1][j-1]:
                # Tuple is added to select_sections to record this path
                select_sections.append((i-1, j-1))
            
            # Checks if smallest value is equal to element directly above the current element
            elif min_option == memo[i-1][j]:
                # Tuple is added to select_sections to record this path
                select_sections.append((i-1, j))

            # If neither two conditions are true, smallest value is equal to the element directly above to the right of current element
            else:
                select_sections.append((i-1, j+1))

    # Determines minimum value in last row of memo and assigns it to min_total_occupancy
    min_total_occupancy = min(memo[n-1])

    # Returns minimal total occupancy and section locations
    return min_total_occupancy, select_sections
