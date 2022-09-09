1. Create an *Candidate* class. 
2. *\__init__* method should take these attributes:
   1. first name
   2. last name
   3. email
   4. tech_stack
   5. salary_expectations
3. create @property method get_full_name. Method should return concatenated first and last names.
4. create @classmethod generate_candidates. As an argument method should receive path to csv file.
5. generate_candidates should return a list of Candidate objects.
6. ** update generate_candidates method to get file path or url to csv file.
   If url was passed - generate list of candidates from url. 
   File url: https://bitbucket.org/ivnukov/lesson2/src/master/candidates.csv

To use:

CSVDictReader - internal python tool
requests - pip install requests
