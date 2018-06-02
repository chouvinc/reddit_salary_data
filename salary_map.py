# Flat hierarchy salary info object

import collections

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

    salary_regions = {
        'US High COL': comment_map, 'US Med COL': comment_map,
        'US Low COL': comment_map, 'Aus/NZ/Canada': comment_map,
        'Eastern Europe': comment_map, 'Western Europe': comment_map,
        'Latin America': comment_map, 'Asia': comment_map,
        'Other': comment_map
    }

    region = ''

    def __init__(self, salary_regions=None, current_region=''):
        if salary_regions:
            self.salary_regions = salary_regions
        self.region = current_region

    def set_region(self, region):
        self.region = region
    
    def set_full_comment_map(self, comment_map):
        self.salary_regions[self.region] = comment_map

    def set_comment_map_field(self, field, value):
        self.salary_regions[self.region][field] = value
