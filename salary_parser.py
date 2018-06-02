# Looks into datasets for some data to parse, sanatize, and possibly reformat if needed

from pprint import pprint
import json, collections

class SalaryParser:
    file_name = ''
    full_path = ''
    data = []
    comment_bodies = []

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
        self.get_comment()

    def get_comment(self):
        for i in range(len(self.data)):
            if 'Education' in self.data[i]:
                curr_comment = self.data[i]
                # some posts have multiple new lines in between categories so filter empty strings after splitting \n
                filtered_and_split = list(filter(None, curr_comment.split('\n')))
                # TODO: send to salary_map once finished

    def get_region(self):
        pass

    def get_post_title(self):
        pass

    # Utility methods
    def salary_info_mapper(self, filtered_data):
        pass