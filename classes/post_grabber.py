# retrieval of new post urls
import json, requests

class PostGrabber:

    CSCQ_URL = "https://www.reddit.com/r/cscareerquestions/new/.json?limit=100"

    properties = {}

    def __init__(self):
        self.properties['url'] = self.CSCQ_URL

    def get_JSON(self):
        # TODO: look up if python has abstracts -- we can make all grabbers extend AbstractGrabber
        json = requests.get(
            self.properties['url'],
            headers={'user-agent': 'Mozilla/5.0'}
        )

        self.properties['jsons'] = json.json()

    def print_JSON(self):
        pass

    # Utlity

    def append_to_property(self, data, property):
        if not self.properties[property]:
            self.properties[property] = []
        self.properties[property].append(data)

    def assign_to_property(self, data, property):
        self.properties[property] = data