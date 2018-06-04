# retrieval of new post urls
import json, requests

class PostGrabber:

    # TODO: create a scheduler to pull these posts every day at the start of the month until the monthly salary thread is found
    CSCQ_URL = "https://www.reddit.com/r/cscareerquestions/new/.json?limit=10"

    properties = {}

    def __init__(self):
        self.properties['url'] = self.CSCQ_URL

        # DELETE THIS AFTER
        self.get_JSON()
        self.save_JSON()
        # DELETE THIS AFTER

    # JSON Methods
    def get_JSON(self):
        # TODO: look up if python has abstracts -- we can make all grabbers extend AbstractGrabber
        json = requests.get(
            self.properties['url'],
            headers={'user-agent': 'Mozilla/5.0'}
        )

        self.append_to_property(json.json(), 'jsons')
        print(self.properties['jsons'])

    def save_JSON(self):
        with open('raw_datasets/posts', 'w') as f:
            f.write(json.dumps(self.properties['jsons'], indent=4, separators=(',', ': ')))

    # Utlity

    def append_to_property(self, data, property):
        if property not in self.properties:
            self.properties[property] = []
        self.properties[property].append(data)

    def assign_to_property(self, data, property):
        self.properties[property] = data        

    def print(self, property):
        try:
            print(self.properties[property])
        except KeyError:
            print('Key does not exist!') 