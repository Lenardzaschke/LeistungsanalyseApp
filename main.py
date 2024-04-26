import json
import my_classes as mc
import os
import my_functions as mf


def create_experiment():
    name = input("Enter the experiment name: ")
    date = input("Enter the experiment date: ")
    supervisor = input("Enter the supervisor's first name: ")
    subject = input("Enter the subject's first name: ")


    experiment = {
        "name": name,
        "date": date,
        "supervisor": supervisor,
        "subject": subject}
    print(experiment)

    with open("experiment.json", "w") as file:
        json.dump(experiment, file)

create_experiment()
