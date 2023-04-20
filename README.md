# docker-compliance.py

Docker Compliance

Docker Compliance is a Python script that checks Docker environments against various compliance standards, such as CIS Docker Benchmark or NIST SP 800-190, to ensure that they meet the required security controls.
Prerequisites

Before running Docker Compliance, make sure that you have:

    Python 3.6 or higher installed
    Docker installed and running
    The docker Python package installed (pip install docker)

Usage

To run Docker Compliance, execute the docker-compliance.py script with the compliance standard you want to check as an argument:

python docker-compliance.py cis-docker-benchmark-v1.2.0

The script will automatically download and apply the specified compliance standard to the Docker environment and generate a report that indicates whether the environment meets the required security controls.
Supported Compliance Standards

Docker Compliance currently supports the following compliance standards:

    CIS Docker Benchmark v1.2.0

Contributing

If you want to contribute to Docker Compliance, feel free to fork the repository and submit a pull request.
License

Docker Compliance is licensed under the MIT License. See LICENSE for more information.

