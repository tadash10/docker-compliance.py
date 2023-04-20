#!/usr/bin/env python3

# docker-compliance.py - A script to check Docker environments against various compliance standards, such as CIS Docker Benchmark or NIST SP 800-190, to ensure that they meet the required security controls.

# Disclaimer: This script is provided as-is and without warranty of any kind. Use at your own risk.

# Proudly created by [t1] 04/2023

import os
import subprocess
import logging

# Configure logging
logging.basicConfig(filename='docker-compliance.log', level=logging.INFO)

#!/usr/bin/env python3

import os
import subprocess
import logging

# Configure logging
logging.basicConfig(filename='docker-compliance.log', level=logging.INFO)

# Define list of supported compliance standards
STANDARDS = {
    'cis-docker': 'CIS Docker Benchmark',
    'nist-800-190': 'NIST SP 800-190',
    'nist-800-53': 'NIST SP 800-53',
    'pci-dss': 'PCI DSS',
    'hipaa': 'HIPAA',
    'sox': 'SOX',
}

# Define function to list available compliance standards
def list_standards():
    logging.info("Listing available compliance standards")
    for key, value in STANDARDS.items():
        print(f"{key}: {value}")

# Define function to display Docker version information
def display_version():
    logging.info("Displaying Docker version information")
    subprocess.run(['docker', 'version'])

# Define function to check Docker compliance against a specific standard
def check_compliance(standard):
    if standard not in STANDARDS:
        print("Invalid compliance standard")
        return
    logging.info(f"Checking Docker compliance against {STANDARDS[standard]} standard")
    subprocess.run(['docker', 'pull', 'docker/compliance'])
    subprocess.run(['docker', 'run', '--rm', '-v', '/var/run/docker.sock:/var/run/docker.sock', '-v', f'{os.getcwd()}/reports:/reports', f'docker/compliance', f'--{standard}', '--json', '/reports/report.json'])

# Define function to generate HTML report from compliance JSON file
def generate_report():
    logging.info("Generating compliance report")
    subprocess.run(['docker', 'run', '--rm', '-v', f'{os.getcwd()}/reports:/reports', '-v', f'{os.getcwd()}/templates:/templates', '-v', f'{os.getcwd()}/output:/output', 'eliaslecomte/docker-compliance-report', '-j', '/reports/report.json', '-t', '/templates/report.html', '-o', '/output/report.html'])

# Define function to send compliance report via email
def send_report():
    logging.info("Sending compliance report via email")
    # Add code here to send email with compliance report as attachment

# Define function to clean up compliance report files
def cleanup():
    logging.info("Cleaning up compliance report files")
    os.remove('./reports/report.json')
    os.remove('./output/report.html')

# Display menu options
def menu():
    print("\nSelect an option:")
    print("1. List available compliance standards")
    print("2. Display Docker version information")
    print("3. Check Docker compliance against a specific standard")
    print("4. Generate HTML report from compliance JSON file")
    print("5. Send compliance report via email")
    print("6. Clean up compliance report files")
    print("7. Exit")

# Define main function
def main():
    # Create directories for compliance report files
    if not os.path.exists("./reports"):
        os.makedirs("./reports")
    if not os.path.exists("./output"):
        os.makedirs("./output")

    while True:
        # Display menu and get user input
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            list_standards()
