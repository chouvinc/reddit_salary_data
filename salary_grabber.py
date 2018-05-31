import json, requests, pprint

class SalaryGrabber:
    salaries = []
    urls = []
    jsons = []
    text_bodies = []

    def __init__(self, urls):
        self.salaries = []
        self.urls = urls
        
        # list of jsons from salary thread
        self.jsons = []
        
        # get json from urls
        self.get_JSON(urls)

    # JSON Methods
    def get_JSON(self, urls):
        for url in urls:
            json = requests.get(
                url,
                headers={'user-agent': 'Mozilla/5.0'}
            )

            # need to call .json() after since above returns requests
            self.jsons.append(json.json())
    
    def print_JSON(self):
        for item in self.jsons:
            print(item.json())

    def save_JSON(self):
        self.r_find(self.jsons, 'body')
      
        with open('salary_thread', 'wt') as f:
            f.write(str(pprint.pformat(self.text_bodies)))


    def read_existing_JSON(self):
        # Assumes a well-formatted dict as a string in the JSON file
        with open('salary_thread') as f:
            print(f.read())

    def r_find(self, l_or_d, key):
        # recursively search a nested list/dict for a field

        if isinstance(l_or_d, list):
            for i in l_or_d:
                self.r_find(i, key)
        elif isinstance(l_or_d, dict):
            if key in l_or_d: 
                self.text_bodies.append(l_or_d[key])       
            for values in l_or_d.values():
                self.r_find(values, key)


        