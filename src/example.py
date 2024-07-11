import os
import pandas as pd

def read_disciplines_from_excel(file_path):
    # Load the Excel file
    data = pd.read_excel(file_path)
    
    # Get the list of disciplines
    disciplines = data['Discipline'].tolist()
    
    return disciplines

# Usage example
file_path = os.path.join('kaggle', 'input', '2021ol_in_tokyo', 'EntriesGender.xlsx')
disciplines = read_disciplines_from_excel(file_path)
print(disciplines)