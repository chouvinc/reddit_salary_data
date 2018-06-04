from classes.salary_grabber import SalaryGrabber
from classes.salary_aggregator import SalaryAggregator
from classes.post_grabber import PostGrabber

import json

# test salary grabber
salaries = SalaryGrabber('https://www.reddit.com/r/cscareerquestions/comments/6ye3fs/official_salary_sharing_thread_for_new_grads.json')
salaries.save_JSON()
salaries.dump_full_data()
salaries.dump_no_formatting()
salaries.get_post_title()

# test salary aggregator
aggregator = SalaryAggregator()
aggregator.set_dataset()
aggregator.get_salary_info()

# test post grabber
post_grabber = PostGrabber()
