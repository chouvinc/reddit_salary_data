# Takes in well-formatted salary data and maps to the given categories.

class SalaryAggregator:
    categories = {}

    def __init__(self, categories, salary_grabber):
        self.categories = categories

    def map_by_categories(self):
        print('in progress')
