import csv
import requests


class Candidate:

    def __init__(self, first_name, last_name, email, tech_stack, main_skill, main_skill_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self):
        return f'Full name: {self.first_name} {self.last_name}'

    @classmethod
    def generate_candidates(cls, path_to_file):
        with requests.Session() as csv_data:
            download = csv_data.get(path_to_file)
            decoded_content = download.content.decode('utf-8')
            decoded_csv_data = csv.DictReader(decoded_content.splitlines(), delimiter=',')
            data_list = list(decoded_csv_data)
            candidates_data_list = []
            for record in data_list:
                candidate = dict(
                    first_name=record['Full Name'].split(maxsplit=1)[0],
                    last_name=record['Full Name'].split(maxsplit=1)[1],
                    email=record['Email'],
                    tech_stack=record['Technologies'].split('|'),
                    main_skill=record['Main Skill'],
                    main_skill_grade=record['Main Skill Grade']
                )
                candidates_data_list.append(candidate)
            return [cls(**x) for x in candidates_data_list]


if __name__ == '__main__':
    candidates = Candidate.generate_candidates(
        'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv')
    print([x.full_name for x in candidates])
