from typing import List, Tuple

import pandas as pd

def getIndices(dfObj: pd.DataFrame, cond: pd.DataFrame) -> List[Tuple[str, str]]:
    ''' Get row, col positions of value in dataframe given condition.'''
    listOfPos = list()
    # Get bool dataframe with True at positions where the given value exists
    result = dfObj[cond]
    # Get list of columns that contains the value
    seriesObj = result.any()
    columnNames = list(seriesObj[seriesObj == True].index)
    # Iterate over list of columns and fetch the rows indexes where value exists
    for col in columnNames:        
        rows = list(result[col][result[col].notna()].index)
        for row in rows:
            listOfPos.append((row, col))
    # Return a list of tuples indicating the positions of value in the dataframe
    return listOfPos


def extractOtherCollinearPair(col_pairs: List[Tuple[str, str]]) -> List[str]:
    ''' Iterates through tuples of collinear pairs and extracts one of the pair. '''
    tmp = []
    collinear_other_pairs = []
    
    for pair in col_pairs:
        if set(pair) in tmp:
            collinear_other_pairs += [pair[1]]
        else:
            tmp += [set(pair)]
            
    return collinear_other_pairs