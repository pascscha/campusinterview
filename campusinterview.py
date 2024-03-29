import json
import getpass
import requests


class StudentProfile:
    URL = "https://api.campusinterview.ch/student"

    def __init__(self, mail=None, password=None, verify_ssl=False):

        # Ask for credentials if not provided
        if mail is None:
            mail = input("Please enter your mail address: ")
        if password is None:
            password = getpass.getpass("Please enter your password: ")

        # Wether or not the SSL Certificates should get verified.
        # Should be True to avoid MITM voulnerability.
        self._verify_ssl = verify_ssl

        # Private variables to cache results
        self._companies = None
        self._profile = None
        self._id = None
        self._interviews = None
        self._accepted_request_companies = None

        self.mail = mail
        self.password = password
        self.session = self._get_session(mail, password)

    def _get_session(self, mail, password):
        """Gets session which is logged into a student account at campusinterview.ch
        @param mail : The student mail address.
        @param password : The according password.
        @returns requests.session : The logged in session
        """

        # Login
        data = {
            "cmd": "loginStudent",
            "mail": mail,
            "password": password
        }
        session = requests.session()
        response = session.post(self.URL,
                                data=data,
                                verify=self._verify_ssl)

        # Check that data was transmitted successfully
        response.raise_for_status()

        return session

    def _load_companies(self):
        """Gets a list of all companies on campusinterview.ch
        @param session : A session with a valid login cookie
        @returns list : A list containing all companies
        """

        out = []
        page = 0
        # Iterate over all pages until no results come back
        while True:
            data = {
                "cmd": "getCompanies",
                "request": "",
                "name": "",
                "business": "",
                "area": "",
                "page": page
            }

            response = self.session.post(self.URL,
                                         data=data,
                                         verify=self._verify_ssl)

            # Check that data was transmitted successfully
            response.raise_for_status()

            new = json.loads(response.text)

            if len(new) == 0:
                # We reached the end
                return out
            else:
                out += new
                page += 1

    def _load_profile(self):
        data = {
            "cmd": "getStudent"
        }
        response = self.session.post(self.URL,
                                     data=data,
                                     verify=self._verify_ssl)

        # Check that data was transmitted successfully
        response.raise_for_status()

        return json.loads(response.text)

    def _load_interviews(self):
        data = {
            "cmd": "getInterviews",
            "studentId": "000000000000000000000000"  # Doesn't matter what you put here
        }
        response = self.session.post(self.URL,
                                     data=data,
                                     verify=self._verify_ssl)

        # Check that data was transmitted successfully
        response.raise_for_status()

        return json.loads(response.text)

    def _load_accepted_request_companies(self):
        data = {
            "cmd": "getAcceptedRequestCompanies"
        }
        response = self.session.post(self.URL,
                                     data=data,
                                     verify=self._verify_ssl)

        # Check that data was transmitted successfully
        response.raise_for_status()

        return json.loads(response.text)

    @property
    def companies(self):
        if self._companies is None:
            self._companies = self._load_companies()
        return self._companies

    @property
    def profile(self):
        if self._profile is None:
            self._profile = self._load_profile()
        return self._profile

    @property
    def id(self):
        return self.profile["_id"]

    @property
    def interviews(self):
        if self._interviews is None:
            self._interviews = self._load_interviews()
        return self._interviews

    @property
    def accepted_request_companies(self):
        if self._accepted_request_companies is None:
            self._accepted_request_companies = self._load_accepted_request_companies()
        return self._accepted_request_companies
