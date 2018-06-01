# Looks into datasets for some data to parse, sanatize, and possibly reformat if needed

class SalaryParser:

    def __init__(self, path="datasets/"):
        self.path = path

    # method to sanitize file of non-alphanumeric values
    def sanitize(self):
        # get the file from the datasets folder and read
        data = ''
        with open('datasets/salary_thread') as f:
            data = f.read()

        # do stuff with the dataset
        data.rstrip()

        # write it back to the file for future use
        with open('datasets/salary_thread') as f:
            f.write(data)



    # method to parse and format as list of key-value pairs <key: text_body>
    def parse_and_dict(self):
        pass
