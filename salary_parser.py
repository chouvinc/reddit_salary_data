# Looks into datasets for some data to parse, sanatize, and possibly reformat if needed

from pprint import pprint
import json, collections, salary_map

class SalaryParser:
    file_name = ''
    full_path = ''
    data = []
    comment_bodies = []
    salary_map = salary_map.SalaryMap()

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
        self.get_comment_by_region()

    def get_comment_by_region(self):
        for i in range(len(self.data)):
            self.check_region(self.data[i])
            self.add_comment_to_region(self.data[i])

    def check_region(self, current_comment):
        if 'Region' in current_comment:
            # use a for-loop instead of regex in case reddit ever changes post markdown format from **<item>** to another format
            for region in self.salary_map.regions.keys():
                if region in current_comment:
                    self.salary_map.set_region(region)

    def add_comment_to_region(self, current_comment):
        # can use first term of salary_map.comment_map b/c categories always in order
        c_map = self.salary_map.comment_map
        if self.peek_od_keys(c_map) in current_comment:
            # some posts have multiple new lines in between categories so filter empty strings after splitting \n
            filtered_and_split = list(filter(None, current_comment.split('\n')))
            self.map_to_region(filtered_and_split, self.salary_map.selected_region)

    def map_to_region(self, filtered_data, region):
        c_map = self.salary_map.comment_map
        key_map = c_map.keys()
        counter = 0
        nested_info = []

        self.pop_until_key(filtered_data, self.peek_od_keys(c_map))

        # while filtered_data:
        #     first_word, comment_content = self.split_comment(filtered_data.pop(0))
        #     c_keys = c_map.keys()

        #     # TODO: consider using a suffix tree 
        #     key = self.get_key_from_substring(first_word, c_keys)
        #     if key == self.peek_od_keys(c_map):
        #         nested_info.append(comment_content)

        while filtered_data:
            curr_first_word, curr_content = self.split_comment(filtered_data.pop(0))
            curr_key = self.get_key_from_substring(curr_first_word, key_map)

            # TODO FINISH THIS IMMEDIATELY
            
        with open('datasets/so_purdy', 'w') as f:
            f.write(json.dumps(self.salary_map.regions, indent=4, separators=(',',':')))

    def get_post_title(self):
        pass

    # Utility methods
    def pop_until_key(self, data, key):
        while data:
            this_word = self.split_comment(data[0])
            key = self.get_key_from_substring(this_word, self.salary_map.comment_map.keys())

            if key:
                return
            data.pop(0)    

    def peek_od_keys(self, od):
        # takes an OrderdDict object and adds a peek (first) method
        # for some reasons od.keys() returns another od sub-class object and not another list, so we're
        # artificially returning the first item here
        for item in od.keys():
            return item 

    def split_comment(self, line):
        split = line.split(':')
        return (split[0], split[1:len(split)])

    def get_key_from_substring(self, sub, key_map):
        for key in key_map:
            if sub in key:
                return key

        return None