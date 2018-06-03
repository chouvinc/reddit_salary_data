import json, requests, pprint

# SalaryGrabber should only build & save the dataset. Utility methods are allowed
# if they improve the readability/usability of the dataset. 
class SalaryGrabber:
    properties = {
        'salaries': [],
        'url': None,
        'jsons': None,
        'text_bodies': []    
    }

    def __init__(self, url):
        self.properties['salaries'] = []
        self.properties['url'] = url
        
        # list of jsons from salary thread
        self.properties['jsons'] = []
        
        # get json from urls
        self.get_JSON()

    # JSON Methods
    def get_JSON(self):
        # TODO 2)
        json = requests.get(
            self.properties['url'],
            headers={'user-agent': 'Mozilla/5.0'}
        )

        # need to call .json() after since above returns requests
        self.properties['jsons'] = json.json()
    
    def print_JSON(self):
        print(self.properties['json'])

    def save_JSON(self, some_json={}):
        # TODO 1)
        self.r_find(self.properties['jsons'], 'body')
      
        with open('raw_datasets/salary_thread', 'wt') as f:
            f.write(json.dumps(self.properties['text_bodies'], indent=4, separators=(',', ': ')))

    def read_existing_JSON(self):
        # Assumes a well-formatted dict as a string in the JSON file
        with open('raw_datasets/salary_thread') as f:
            print(f.read())

    # Utility methods
    def r_find(self, l_or_d, key):
        # recursively search a nested list/dict for a key

        if isinstance(l_or_d, list):
            for i in l_or_d:
                self.r_find(i, key)
        elif isinstance(l_or_d, dict):
            if key in l_or_d: 
                self.append_to_property('text_bodies', l_or_d[key])       
            for values in l_or_d.values():
                self.r_find(values, key)

    def append_to_property(self, property, value):
        self.properties[property].append(value)

    # Sanity check that we're not leaking any data in r_find
    def dump_full_data(self):
        with open('misc_datasets/full_salary_thread', 'wt') as f:
            f.write(json.dumps(self.properties['jsons'], indent=4, separators=(',',':')))

    def dump_no_formatting(self):
        with open('misc_datasets/no_formatting_salary_thread', 'wt') as f:
            f.write(str(self.properties['text_bodies']))

# TODO: 
# 1) Make logic to build a different data set per new page of salary discussion
# 2) Fetch new salary threads automatically (either set min # of comments or min period of time that thread existed)