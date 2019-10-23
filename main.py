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


def save_accepted_request_companies():
    """Saves all company data for accepted requests to companies_accepted.json
    """
    # Save data to file

    student = StudentProfile()

    savefile = "companies_accepted.json"

    with open(savefile, "w+") as f:
        json.dump(student.accepted_request_companies, f, indent=1)
    print("\nSaved data to {}.".format(savefile))


def display_interview_stats():
    """Displays useful stats for upcoming interviews
    """

    student = StudentProfile()

    data = student.accepted_request_companies

    for company in data:
        name = company["name"]
        website = company["website"]
        n_rejected = len(company["rejectedRequests"])
        n_accepted = len(company["acceptedRequests"])
        n_ignored = len(company["gotRequests"])
        is_business = company["isBusiness"]

        print()
        print("{} ({})".format(name, website))
        if is_business:
            print("Package: Business")
        else:
            print("Package: Economy")

        print("Accepted: {}, Rejected: {}".format(n_accepted, n_rejected + n_ignored))

        print("Recruiters:")
        for participant in company["participants"]:
            name = participant["name"]
            position = participant["position"]
            print(" {} - {}".format(name, position))

        interview_goal = company["interview"]
        print("Interview Goal:\n{}".format(interview_goal))


def display_company_comments():
    """Displays comments made my companies
    """

    student = StudentProfile()

    data = student.accepted_request_companies

    for company in data:
        name = company["name"]
        comments = company["comments"]

        print()
        print(name)

        for comment in comments:
            student = comment["student"]
            text = comment["comment"]
            print("{}: {}".format(student, text))


def save_student_data():
    """Saves all available student data about yourself to student.json
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
    available_functions = [
        display_id,
        company_acceptance_count,
        save_company_data,
        save_student_data,
        save_accepted_request_companies,
        display_interview_stats,
        display_company_comments
    ]

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
