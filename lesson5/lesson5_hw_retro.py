import csv
from io import StringIO

import requests

FILE_URL = 'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv'


class Candidate:
    def __init__(self, first_name, last_name, email, tech_stack, m_skill, m_skill_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.m_skill = m_skill
        self.m_skill_grade = m_skill_grade

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f"{self.full_name} | {self.tech_stack}"

    @staticmethod
    def _prepare_data(source):
        data = []
        reader = csv.DictReader(source)
        for entry in reader:
            data.append(dict(
                first_name=entry['Full Name'].split()[0],
                last_name=entry['Full Name'].split()[1],
                email=entry['Email'],
                tech_stack=entry['Technologies'].split('|'),
                m_skill=entry['Main Skill'],
                m_skill_grade=entry['Main Skill Grade']
            ))
        return data

    @classmethod
    def from_csv(cls, path_to_file=None, url=None):
        result = []
        if path_to_file is not None and path_to_file.startswith('http'):
            url = path_to_file
            path_to_file = None
        if path_to_file is None and url is None:
            raise ValueError('fp or url required')
        if url:
            response = requests.get(url=url)
            result = cls._prepare_data(StringIO(response.text))
        if path_to_file:
            with open(path_to_file) as fp:
                result = cls._prepare_data(fp)
        return [cls(**x) for x in result]


if __name__ == '__main__':
    # candidate_list = Candidate.from_csv('candidates.csv')
    candidate_list = Candidate.from_csv(FILE_URL)
    print('AAAAAAAAAAaaaaaaaaaAAAAAAA')
    [print(x.first_name, x.tech_stack) for x in candidate_list]

    # cls(**kwargs) == Candidate(**kwargs)
