# Flat hierarchy salary info object

import collections, copy

class SalaryMap:
    # TODO (Maybe?): make these properties dynamically adjustable
    # use orderedDict to preserve print/iteration order
    comment_map = collections.OrderedDict([
        ('Education', []),
        ('Prior Experience', []),
        ('Company/Industry', []),
        ('Title', []),
        ('Tenure Length', []),
        ('Location', []),
        ('Salary', []),
        ('Relocation/Signing Bonus', []),
        ('Stock and/or Recurring Bonuses', []),
        ('Total Comp', [])
    ])

    # TODO: make regions dynamically allocated
    regions = {
        'US High CoL': None, 'US Med CoL': None,
        'US Low CoL': None, 'Aus/NZ/Canada': None,
        'Eastern Europe': None, 'Western Europe': None,
        'Latin America': None, 'Asia': None,
        'Other': None
    }

    selected_region = ''

    # stores (erroneous or extra) categories not listed in the initial post body of the reddit thread
    discarded = []

    def __init__(self, regions=None, current_region=''):
        if regions:
            self.regions = regions
        self.selected_region = current_region

        for key in self.regions.keys():
            self.regions[key] = copy.deepcopy(self.comment_map)

    def set_region(self, selected_region):
        self.selected_region = selected_region
    
    def set_full_comment_map(self, comment_map):
        self.regions[self.selected_region] = comment_map

    def set_comment_map_field(self, field, value):
        self.regions[self.selected_region][field] = value
