# Calculate legibility of a txt file using Gulpease Index

import re
import glob
import os
import sys
import json


def gulpease_index(words, letters, points):
    """
    As written in https://it.wikipedia.org/wiki/Indice_Gulpease
    """
    index = 89 + ((300 * points) - (10 * letters)) / words
    return 100 if index > 100 else index


def strip_folder_name(filename):
    """
    Remove initial folder name from the given filename.
    """
    return filename.split('/')[-1]


def txt_extension_to_pdf(filename):
    return f'{filename[:-3]}pdf'


def gulpease(filename):
    result_dict = {}

    print(f'Type filename: f{type(filename)}, {filename}')

    filename_pdf = strip_folder_name(txt_extension_to_pdf(filename))
    result_dict['filename'] = filename_pdf

    with open(filename, encoding='utf-8', mode='r') as f:
        file_text = f.read()

        words = len(file_text.split())
        letters = len(re.findall(r'\w', file_text))
        points = len(re.findall('[.]+\s', file_text)) + \
                 len(re.findall('[;]+\s', file_text)) - \
                 len(re.findall('[.]+\s+[.]', file_text))

        result_dict['words'] = words
        result_dict['letters'] = letters
        result_dict['points'] = points

        if words == 0:
            raise AssertionError('Error calculating Gulpease index!')
        else:
            index = gulpease_index(words, letters, points)
            result_dict['index'] = index

            points = len(re.findall('[.]', file_text)) + \
                len(re.findall('[;]', file_text))
            non_restrictive_index = gulpease_index(words, letters, points)
            result_dict['non_restrictive_index'] = non_restrictive_index
    f.close()
    return result_dict


def gulpease_for_folder(folder_path, file_extension):
    result_list = []
    for filename in glob.glob(os.path.join(folder_path, f'*.{file_extension}'), recursive=False):
        print(f'Found file {filename}')
        result_list.append(gulpease(filename))
    return result_list


def stringify_set(input_list):
    return '\n'.join(input_list)

default_pdf_path = '/pdf'
default_report_folder = '/report'
report_file_name = 'report.json'

pdf_path = sys.argv[1] or default_pdf_path
report_folder = sys.argv[2] or default_report_folder

if os.path.isdir(pdf_path):
    print(f'Looking for txt files in {pdf_path}')
    # we expect PDF files to have already been converted to txt files at this point
    results = gulpease_for_folder(pdf_path, 'txt')

    if len(results) is 0:
        print(f'No txt files found in {pdf_path}')

    with open(os.path.join(report_folder, report_file_name), \
              mode='w', encoding='utf-8') as f:
      # ensure_ascii=False allows to write properly filenames
      # with accents
      json.dump(results, f, sort_keys=True, indent=4, ensure_ascii=False)

    print(f'Generated file {report_file_name}')
else:
    print(f'{pdf_path} is not a directory! Exiting')
