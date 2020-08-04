#!/usr/bin/python3


import csv
import os
import datetime


def process(input_file: str) -> None:
    basename, ext = input_file.rsplit('.', 1)
    output_file = f'{basename}-cleandates.{ext}'
    target_column_name = 'UpdateTime'
    target_column_index = -1
    valid_timestamp_formats = ["%Y-%m-%dT%H:%M:%S%z", "%m/%d/%Y %H:%M:%S %p", "%b %d %Y %H:%M%p"]
    
    with open(input_file, 'r') as infile, open(output_file,'w') as outfile:
        writer = csv.writer(outfile)
        
        for i, row in enumerate(csv.reader(infile)):
            if i == 0 and target_column_name in row:
                target_column_index = row.index(target_column_name)
            else:
                d = row[target_column_index]
                new_date = None
                
                for format in valid_timestamp_formats:
                    try:
                        new_date = datetime.datetime.strptime(d, format).isoformat()
                    except:
                        pass
                    else:
                        break                        
                                        
                if new_date is None:
                    raise ValueError(f'Date was not properly set! Value: {d}')
                    
                row[target_column_index] = new_date.split('+')[0] + 'Z'
                
            writer.writerow(row)
            

if __name__ == '__main__':
    process('PostMattChangesNew.csv')
