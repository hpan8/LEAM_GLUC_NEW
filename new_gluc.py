"""
This script will do:
1. Input: LU_Boundary, nogrowth map, curren LU map, population and employment output projections
2. Based on the above information, decide future land-use change (by class and by year)
3. Output: LU_change.txt, LU_year.txt

"""


import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from optparse import OptionParser
import time



def main():



if __name__ == "__main__":
    if (len(sys.argv) < 3):
        print "Required: Arg1 years, Arg2 population projections, Arg3 employment projections"
        exit(1)
    main()