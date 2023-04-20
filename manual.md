Introduction

Docker-Compliance is a Python script to automate compliance checks in Docker environments against various security standards, including CIS Docker Benchmark and NIST SP 800-190. It generates a JSON report of the compliance checks and can also generate an HTML report for easy readability.
Installation

The script requires Docker and Python3 installed on your system. To install Docker, follow the instructions in the Docker documentation: https://docs.docker.com/get-docker/.

To install Python3, run the following command in your terminal:

arduino

sudo apt-get install python3

After installing Docker and Python3, clone the repository to your system using the following command:

bash

git clone https://github.com/yourusername/docker-compliance.git

Usage

To use the script, navigate to the cloned repository directory and run the following command:

python3 docker-compliance.py

This will display a menu with the following options:

    Check Docker compliance against a specific standard
    Generate HTML report from compliance JSON file
    Send compliance report via email
    Clean up compliance report files
    Exit

Option 1: Check Docker compliance against a specific standard

To check Docker compliance against a specific standard, select option 1 from the menu and enter the name of the standard when prompted (e.g. cis-docker). The script will pull the Docker compliance image and run it with the specified standard, generating a JSON report in the "reports" directory.
Option 2: Generate HTML report from compliance JSON file

To generate an HTML report from the compliance JSON file, select option 2 from the menu. The script will use the compliance report JSON file generated in the "reports" directory to generate an HTML report in the "output" directory.
Option 3: Send compliance report via email

To send the compliance report via email, select option 3 from the menu. Add the code to send email with compliance report as an attachment in the "send_report()" function.
Option 4: Clean up compliance report files

To clean up compliance report files, select option 4 from the menu. The script will delete the compliance report JSON and HTML files from the "reports" and "output" directories, respectively.
Option 5: Exit

To exit the script, select option 5 from the menu.
Compliance Standards

The script currently supports the following compliance standards:

    cis-docker: CIS Docker Community Edition Benchmark v1.2.0
    nist-800-190: NIST SP 800-190 Application Container Security Guide v1.1

The compliance standards are implemented in the "check_compliance()" function. You can add new standards by following the pattern in the existing code.
Conclusion

Docker-Compliance is a useful tool to automate compliance checks in Docker environments against various security standards. With its ability to generate compliance reports in JSON and HTML formats, it can help ensure that Docker environments meet required security controls.
