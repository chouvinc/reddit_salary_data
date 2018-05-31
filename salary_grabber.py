import json, requests, pprint

# SalaryGrabber should only build & save the dataset. Utility methods are allowed
# if they improve the readability/usability of the dataset. SalaryGrabber takes in
# a SalaryStrategy to determine which functionality to use (and thus the shape of
# the data).
class SalaryGrabber:
    properties = {
        'salaries': [],
        'urls': [],
        'jsons': [],
        'text_bodies': []    
    }

    def __init__(self, urls):
        self.properties['salaries'] = []
        self.properties['urls'] = urls
        
        # list of jsons from salary thread
        self.properties['jsons'] = []
        
        # get json from urls
        self.get_JSON(urls)

    # JSON Methods
    def get_JSON(self, urls):
        # TODO 2)
        for url in urls:
            json = requests.get(
                url,
                headers={'user-agent': 'Mozilla/5.0'}
            )

            # need to call .json() after since above returns requests
            self.properties['jsons'].append(json.json())
    
    def print_JSON(self):
        for item in self.properties['jsons']:
            print(item.json())

    def save_JSON(self, some_json={}):
        # TODO 1)
        self.r_find(self.properties['jsons'], 'body')
      
        with open('datasets/salary_thread', 'wt') as f:
            f.write(str(pprint.pformat(self.properties['text_bodies'])))


    def read_existing_JSON(self):
        # Assumes a well-formatted dict as a string in the JSON file
        with open('datasets/salary_thread') as f:
            print(f.read())

    # Utility methods
    def r_find(self, l_or_d, key):
        # recursively search a nested list/dict for a key

        if isinstance(l_or_d, list):
            for i in l_or_d:
                self.r_find(i, key)
        elif isinstance(l_or_d, dict):
            if key in l_or_d: 
                self.properties['text_bodies'].append(l_or_d[key])       
            for values in l_or_d.values():
                self.r_find(values, key)

# TODO: 
# 1) Make logic to build a different data set per new page of salary discussion
# 2) Fetch new salary threads automatically (either set min # of comments or min period of time that thread existed)