# removes whole column from data frame if column has any missing values
def dropEmptyValueColumn(dataFrame):
    try:
        dataFrame.dropna(inplace=True, axis=1)
    except:
        pass

# removes whole row from data frame if row has any missing values
def dropEmptyValueRow(dataFrame):
    try:
        dataFrame.dropna(inplace=True, axis=0)
    except:
        pass

# removes whole column from data frame by name
def dropColumnByName(dataFrame, columnName):
    try:
        dataFrame.drop(columnName, inplace=True, axis=1)
    except:
        pass

# replaces empty values in columns from the data frame with new value
def fillEmptyValueColumn(dataFrame, newValue):
    try:
        dataFrame.fillna(newValue, inplace=True)
    except:
        pass