# 2881. Create a New Column

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(bonus=2 * employees['salary'])
    return employees