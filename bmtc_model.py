import pandas as pd
# import other packages here
from math import radians, cos, sin, asin, sqrt

"""
ILLUSTRATION: HOW TO USE RELATIVE PATH
Given the above mentioned assumptions, when you run the code, the following three commands will read the files 
containing data, input and, the ground truth.
"""
df = pd.read_parquet('./../data/BMTC.parquet.gzip', engine='pyarrow')  # This command loads BMTC data into a dataframe.
# In case of error, install pyarrow using:
# pip install pyarrow
dfInput = pd.read_csv('./../data/Input.csv')
dfGroundTruth = pd.read_csv('./../data/GroundTruth.csv')
# NOTE: The file GroundTruth.csv is for participants to assess the performance their own codes

"""
CODE SUBMISSION TEMPLATE
1. The submissions should have the function EstimatedTravelTime().
2. Function arguments:
    a. df: It is a pandas dataframe that contains the data from BMTC.parquet.gzip
    b. dfInput: It is a pandas dataframe that contains the input from Input.csv
3. Returns:
    a. dfOutput: It is a pandas dataframe that contains the output
"""


def EstimatedTravelTime(df, dfInput):  # The output of this function will be evaluated
    # Function body - Begins
    # Make changes here.
    dfOutput = pd.DataFrame()

    # Function body - Ends
    return dfOutput


"""
Other function definitions here: BEGINS
"""

"""
Other function definitions here: ENDS
"""

dfOutput = EstimatedTravelTime(df, dfInput)