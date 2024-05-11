# System Monitoring Tool with Nagios Integration

## Description

The System Monitoring Tool is a Python-based solution designed to monitor CPU, memory, and disk usage of systems in real-time. It leverages the psutil library to gather system metrics and includes features such as customizable threshold configurations, error handling, and logging mechanisms. Moreover, it seamlessly integrates with Nagios, a widely-used monitoring system, to enable centralized monitoring and alerting.

## Features

- Monitor CPU, memory, and disk usage of systems.
- Customizable threshold configurations for monitoring alerts.
- Error handling and logging mechanisms for robustness.
- Seamless integration with Nagios for centralized monitoring and alerting.
- Modular design for scalability and flexibility.

## Installation

1. Ensure Python (version X.X.X or higher) is installed on your system.
2. Install the required dependencies using the following command:
pip install psutil
3. Clone the repository to your local machine:
git clone https://github.com/yourusername/system-monitoring-tool.git
4. Navigate to the project directory:
cd system-monitoring-tool

## Usage

1. Configure monitoring thresholds in the `config.ini` file.
2. Run the monitoring script `monitor.py` using Python:
python monitor.py

## Configuration

The `config.ini` file allows you to customize monitoring thresholds for CPU, memory, and disk usage.

## Screenshots

![Screenshot 1](screenshots/screenshot1.png)
*Caption for Screenshot 1*

![Screenshot 2](screenshots/screenshot2.png)
*Caption for Screenshot 2*

## Acknowledgements

- psutil library: [https://github.com/giampaolo/psutil](https://github.com/giampaolo/psutil)
- Nagios: [https://www.nagios.org/](https://www.nagios.org/)

