#!/usr/bin/python3

# @begin MergeSqlAndData  @desc Merges the schema from the sql file with the cleaned data
# @in csv @file file:PostOpenRefineFinal.csv
# @in sql  @file file:PostOpenRefine.sql
# @out final_sql  @file file:FarmersMarket.sql

import csv
import os
from pathlib import Path

def rip_schema(sql_in):
    return [line for line in sql_in if '(' != line[0]]


def wrap_csv_field(field):
    if field is None or field == '':
        return 'null'
        
    try:
        float(field)
    except ValueError:
        new_field = field.replace("'", "''")
        return f"'{new_field}'"
    else:
        return field if len(str(field)) != 5 else f"'{field}'"
    
def csv_record_clean(record):
    start_record = '( '
    mid_record = [wrap_csv_field(field) for field in record]
    end_record = ' )'
    
    return start_record + ','.join(mid_record) + end_record
    
    
def load_csv(csv_in):
    return [row for row in csv.reader(csv_in)][1:]
    

# @begin merge_files  @desc Merges the schema from the SQL file and data from CSV
# @in csv @file file:PostOpenRefineFinal.csv
# @in sql  @file file:PostOpenRefine.sql
# @out final_sql  @file file:FarmersMarket.sql
# @end merge_files
def merge_files(sql_path: Path, csv_path: Path) -> None:
    with open(sql_path, 'r') as sql_in, open(csv_path, 'r') as csv_in, open('FarmersMarket.sql', 'w') as sql_out:        
        
        # isolate schema liens
        schema = [line for line in rip_schema(sql_in)]            
            
        # convert new data to sql records
        new_rows = [csv_record_clean(row) for row in load_csv(csv_in)]
        
        # write schema
        sql_out.write(''.join(schema))
        
        # write data
        sql_out.write(',\n'.join(new_rows))
        
    
if __name__ == "__main__":
    csv_path = Path('PostOpenRefineFinal.csv')
    sql_path = Path('PostOpenRefine.sql')
    merge_files(sql_path, csv_path)
    
# @end MergeSqlAndData
