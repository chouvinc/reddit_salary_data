from classes.salary_grabber import SalaryGrabber
from classes.salary_aggregator import SalaryAggregator

import json

salaries = SalaryGrabber('https://www.reddit.com/r/cscareerquestions/comments/6ye3fs/official_salary_sharing_thread_for_new_grads.json')
salaries.save_JSON()
salaries.dump_full_data()
salaries.dump_no_formatting()

aggregator = SalaryAggregator()
aggregator.set_dataset()
aggregator.get_salary_info()
