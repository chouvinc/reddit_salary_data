# retrieval of new post urls
import json, requests
from salary_grabber import SalaryGrabber

class PostGrabber(SalaryGrabber):

    # TODO: create a scheduler to pull these posts every day at the start of the month until the monthly salary thread is found
    CSCQ_URL = "https://www.reddit.com/r/cscareerquestions/new/.json?limit=10"

    properties = {}

    def __init__(self):
        self.properties['url'] = self.CSCQ_URL

        # DELETE THIS AFTER
        self.get_JSON()
        self.save_JSON()
        # DELETE THIS AFTER

    # Implement PostArr specific methods (find post by title, find post by month, etc.)
