import os
import sys
import datetime
import re
import shutil

# Created by Craig Cox
# 25th March 2023
# v1.0

the_dir = "C:\\photos"
extensions_tuple = (".raw", ".psd", ".tif", ".tiff", ".gif", ".jpg", ".png", ".bmp", ".cr2")

for root, subdirs, files in os.walk(the_dir):
    for filename in files:
        year_month_day = ""
        earlier_date = 0
        filename_split_tup = os.path.splitext(filename)
        filename_only = filename_split_tup[0]
        filename_ext = filename_split_tup[1]

        if filename_ext.lower().endswith(extensions_tuple):
            file_path_n_name = os.path.join(root, filename)

            file_modified_time = os.path.getmtime(file_path_n_name)
            dt_modified = datetime.datetime.fromtimestamp(file_modified_time)
            modified_year_month_day = str(dt_modified.year) + ("{:02d}".format(dt_modified.month)) + ("{:02d}".format(dt_modified.day))
            modified_date_underscore = modified_year_month_day + "_"

            create_time = os.path.getctime(file_path_n_name)
            # convert the creation timestamp into a DateTime object
            dt_create = datetime.datetime.fromtimestamp(create_time)
            create_year_month_day = str(dt_create.year) + ("{:02d}".format(dt_create.month)) + ("{:02d}".format(dt_create.day))

            if (modified_year_month_day < create_year_month_day):
                earlier_date = modified_year_month_day
            else:
                earlier_date = create_year_month_day

            earlier_date_underscore = earlier_date + "_"
            found = re.search("^" + earlier_date_underscore, filename)

            if not found:
                #print(f'{file_path_n_name} date was {year_month_day}')
                new_filename = earlier_date_underscore + filename
                new_file_path_n_name = os.path.join(root, new_filename)
                print(f'OLD = {file_path_n_name} New = {new_file_path_n_name}')
                shutil.move(file_path_n_name, new_file_path_n_name)
