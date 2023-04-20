#!/usr/bin/env python3

import os
import subprocess
import logging

# Configure logging
logging.basicConfig(filename='docker-compliance.log', level=logging.INFO)

# Define function to check Docker compliance against a specific standard
def check_compliance(standard):
    logging.info(f"Checking Docker compliance against {standard} standard")
    subprocess.run(['docker', 'pull', 'docker/compliance'])
    subprocess.run(['docker', 'run', '--rm', '-v', '/var/run/docker.sock:/var/run/docker.sock', '-v', f'{os.getcwd()}/reports:/reports', f'docker/compliance', f'--cis={standard}', '--json', '/reports/report.json'])

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
    print("1. Check Docker compliance against a specific standard")
    print("2. Generate HTML report from compliance JSON file")
    print("3. Send compliance report via email")
    print("4. Clean up compliance report files")
    print("5. Exit")

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
            standard = input("Enter the name of the compliance standard to check (e.g. cis-docker): ")
            check_compliance(standard)

        elif choice == "2":
            generate_report()

        elif choice == "3":
            send_report()

        elif choice == "4":
            cleanup()

        elif choice == "5":
            break

if __name__ == '__main__':
    main()
