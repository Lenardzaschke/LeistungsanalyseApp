import json
import my_functions


# Function to create and print the experiment dictionary
def create_experiment():
    # Ask the user for the required data
    name = input("Enter the experiment name: ")
    date = input("Enter the experiment date: ")
    supervisor = input("Enter the supervisor's first name: ")
    subject = input("Enter the subject's first name: ")


    # Create the experiment dictionary
    experiment = {
        "name": name,
        "date": date,
        "supervisor": supervisor,
        "subject": subject
    }

    # Print the experiment dictionary
    print(experiment)

    # Save the experiment dictionary in a file
    with open("experiment.json", "w") as file:
        json.dump(experiment, file)

# Call the function to create and print the experiment dictionary
create_experiment()