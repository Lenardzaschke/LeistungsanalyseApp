import json
import json
from datetime import datetime
from urllib import request

class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
       

    def save(self):
        data = self.__dict__
        with open('person.json', 'w') as file:
            json.dump(data, file)

    def estimate_max_hr(self, age, sex):
    
        if sex == "male":
            max_hr_bpm =  223 - 0.9 * age
        elif sex == "female":
            max_hr_bpm = 226 - 1.0 *  age
        else:
            
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)

    def put(self):
        data = {
            "name": self.first_name
        }
        data_json = json.dumps(data)
        response = requests.put(url, data=data_json)
        print(response.text)

class Experiment:
    def __init__(self, name, date, supervisor, subject):
        self.name = name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject


    def save(self):
        data = self.__dict__
        with open('experiment.json', 'w') as file:
            json.dump(data, file)

            class Person:
                def __init__(self, name, birthdate):
                    self.name = name
                    self.birthdate = birthdate

                def save(self):
                    data = self.__dict__
                    with open('person.json', 'w') as file:
                        json.dump(data, file)

                def calculate_max_hr(self):
                    age = self.calculate_age()
                    max_hr_bpm = 0
                    if age is not None:
                        if self.sex == "male":
                            max_hr_bpm = 223 - 0.9 * age
                        elif self.sex == "female":
                            max_hr_bpm = 226 - 1.0 * age
                    return int(max_hr_bpm)

                def calculate_age(self):
                    if self.birthdate is not None:
                        birthdate = datetime.strptime(self.birthdate, "%Y-%m-%d")
                        today = datetime.today()
                        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
                        return age
                    return None

class Subject(Person):
    def __init__(self, name, birthdate, sex):
        super().__init__(name, birthdate)
        self.sex = sex

    def update_email(self):
            data = {
                "name": self.first_name,
                "email": self.email
            }
            data_json = json.dumps(data)
            response = requests.post(url, data=data_json)
            print(response.text)


class Supervisor(Person):
    def __init__(self, name, birthdate):
        super().__init__(name, birthdate)

class Experiment:
    def __init__(self, name, date, supervisor, subject):
        self.name = name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def save(self):
        data = self.__dict__
        with open('experiment.json', 'w') as file:
            json.dump(data, file)

