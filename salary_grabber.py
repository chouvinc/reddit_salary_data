import json, requests, pprint

class SalaryGrabber:
    salaries = []
    urls = []
    jsons =[]
    pp = pprint.PrettyPrinter(indent=4)

    def __init__(self, urls):
        self.salaries = []
        self.urls = urls
        self.jsons = []
        
        # get json from urls
        self.get_JSON(urls)

    def get_JSON(self, urls):
        for url in urls:
            json = requests.get(
                url,
                headers={'user-agent': 'Mozilla/5.0'}
            )

            self.jsons.append(json)
    
    def print_JSON(self):
        for item in self.jsons:
            print(item.json())

    def obj_keys(self):
        first_item = self.jsons[0].json()[0]

        for key, value in first_item['data'].items():
            self.pp.pprint(key)
        
            