from salary_grabber import SalaryGrabber

salaries = SalaryGrabber(['https://www.reddit.com/r/cscareerquestions/comments/6ye3fs/official_salary_sharing_thread_for_new_grads.json'])
salaries.save_JSON()