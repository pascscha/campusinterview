#!/usr/bin/python3
from campusinterview import StudentProfile
import datetime
import json
import sys


def display_id():
    """Displays your Campusinterview ID.
    """
    student = StudentProfile()

    print("Your ID is: {}".format(student.id))


def company_acceptance_count():
    """Sorts all companies by acceptance count and shows which
    of them accepted you.
    """
    student = StudentProfile()
    # Create a list with the names of the companies and their acceptance count
    acceptedRequests = []
    for company in student.companies:
        acceptedRequests.append((company["name"], company["acceptedRequests"]))

    # Sort accepted requests by acceptand count
    acceptedRequests.sort(key=lambda x: len(x[1]), reverse=True)

    # Display sorted list
    today = datetime.date.today().strftime("%d.%m.%Y")
    print("\nFirmen, Akzeptierte Bewerbungen (Stand {})".format(today))

    accepted_by = 0
    for name, requests in acceptedRequests:
        accepted = False
        for request in requests:
            if request['student'] == student.id:
                accepted = True
                accepted_by += 1
                break

        if accepted:
            print("X", len(requests), name)
        else:
            print(" ", len(requests), name)

    print("You are accepted by {} companies.".format(accepted_by))


def save_company_data():
    """Saves all available company data to companies.json
    """
    # Save data to file

    student = StudentProfile()

    savefile = "companies.json"

    with open(savefile, "w+") as f:
        json.dump(student.companies, f, indent=1)
    print("\nSaved data to {}.".format(savefile))


def save_student_data():
    """Saves all available student data to student.json
    """
    # Save data to file

    student = StudentProfile()

    savefile = "student.json"

    with open(savefile, "w+") as f:
        json.dump(student.profile, f, indent=1)
    print("\nSaved data to {}.".format(savefile))


def help(functions):
    print("Example: ./main.py company_acceptance_count")
    print("\nAvailable functions:")
    for function in functions:
        print("{}:\n    {}".format(function.__name__, function.__doc__))


if __name__ == "__main__":
    available_functions = [display_id, company_acceptance_count, save_company_data, save_student_data]

    if len(sys.argv) != 2:
        print("Invalid number of arguments.")
        help(available_functions)
        exit()

    function = sys.argv[1]

    for f in available_functions:
        if function == f.__name__:
            f()
            break
    else:
        print("Function {} not found.".format(function))
        help(available_functions)
