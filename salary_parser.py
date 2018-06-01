# Looks into datasets for some data to parse, sanatize, and possibly reformat if needed

from pprint import pprint
import json, collections

class SalaryParser:
    # string that specifies current dataset
    file_name = ''
    full_path = ''
    data = []
    # TODO (Maybe?): make these properties dynamically adjustable
    mapped = collections.OrderedDict([
        ('Education', []),
        ('Prior Experience', []),
        ('Company/Industry', []),
        ('Title', []),
        ('Tenure Length', []),
        ('Location', []),
        ('Salary', []),
        ('Relocation/Signing Bonus', []),
        ('Stock and/or Recurring Bonuses', []),
        ('Total Comp', [])
    ])

    def __init__(self, path="datasets/", file_name=""):
        self.path = path
        self.file_name = file_name

        if file_name:
            self.full_path = path + file_name

    # method to grab a particular dataset to parse
    # TODO: remove default for file_name after figuring out what to do if not given file
    def set_dataset(self, file_name='salary_thread'):
        with open('datasets/' + file_name, 'rb') as f:
            self.data = json.loads(f.read())
        
        self.file_name = file_name
        self.full_path = self.path + file_name

    # method to parse and format as list of key-value pairs <key: text_body>
    def parse_and_dict(self):
        pass

    # data logger (in case you don't know which dataset you're using)
    def print_data(self):
        pprint(self.data)
    
    def get_salary_info(self):
        for i in range(len(self.data)):
            if 'Education' in self.data[i]:
                # current post (with the correct format)
                curr_block = self.data[i]
                # some posts have multiple new lines in between categories so filter after splitting \n
                filtered_and_split = list(filter(None, curr_block.split('\n')))
                # filtered now but categories not necessarily next to text body. Send to utility method

                self.mapped = self.salary_info_mapper(filtered_and_split)

    # Utility methods
    def salary_info_mapper(self, filtered_data):
        pass