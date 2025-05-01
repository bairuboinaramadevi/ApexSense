# ApexSense - Smart Prescription Handling

[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
![Microsoft Agentic Framework](https://img.shields.io/badge/Framework-Microsoft%20Agentic-brightgreen)
![Semantic Kernel](https://img.shields.io/badge/Semantic%20Kernel-v1.0+-blueviolet)
![ChromaDB](https://img.shields.io/badge/ChromaDB-v0.4+-orange)
![OpenAI](https://img.shields.io/badge/OpenAI-API-lightgrey)

## Overview

ApexSense is an intelligent system designed to automate and simplify the handling of prescription information. By leveraging AI and a multi-agent architecture built with the Microsoft Agentic Framework and Semantic Kernel, ApexSense can process prescriptions from various formats, extract crucial details, provide intelligent instructions, and send timely reminders to patients.

## Key Features

* **Intelligent Prescription Ingestion:** Handles prescription files in PDF, JPEG, and plain text formats.
* **Automated Data Extraction:** Utilizes an Extraction Agent to identify and extract key information (medication names, dosages, timings, follow-ups, precautions) and stores it in a structured JSON format.
* **AI-Powered Processing:** Employs a Processing Agent powered by Semantic Kernel and OpenAI to interpret extracted data and generate clear instructions and actions.
* **Efficient Memory:** Integrates ChromaDB for storing and retrieving previously processed information, improving efficiency and personalization.
* **Timely Patient Reminders:** An Email Agent sends scheduled reminders for medication intake and follow-up appointments.
* **Modular Design:** Built with Semantic Kernel local functions, ensuring a well-organized and maintainable codebase.

## Architecture

ApexSense utilizes a multi-agent system:

1.  **Extraction Agent:** Ingests and extracts data from prescription files (PDF, JPEG, TXT) into JSON format.
2.  **Processing Agent:**
    * Powered by Semantic Kernel.
    * Uses the `Generate_Instructions` plugin with OpenAI prompt templates to interpret data.
    * Checks ChromaDB for existing instructions for similar prescriptions.
    * Generates new instructions and stores them in ChromaDB if not found.
3.  **Email Agent:**
    * Receives time-based actions from the Processing Agent.
    * Uses the `Email_Reminder` plugin and a scheduler to send reminders to patients.

## Getting Started

### Prerequisites

* Python 3.8 or higher
* pip package installer
* Azure subscription (optional, for cloud-based OpenAI)
* OpenAI API key
* Installation of required Python libraries (see Installation)
* ChromaDB instance (local or remote)
* Email sending service credentials (for the Email Agent)

### Installation

1.  Clone the repository:
    ```bash
    git clone <your_repository_url>
    cd apexsense
    ```

2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
    *(You will need to create a `requirements.txt` file listing dependencies like `pypdf2`, `tesseract`, `fpdf`, `semantic-kernel`, `chromadb`, email libraries, etc.)*

3.  Configure environment variables or configuration files for:
    * OpenAI API key
    * ChromaDB connection details
    * Email service credentials (SMTP server, email address, password)

### Configuration

* **OpenAI:** Set your OpenAI API key in the appropriate environment variable or configuration file.
* **ChromaDB:** Configure the ChromaDB client with the desired settings (e.g., persistence path, client type).
* **Email:** Configure the SMTP server details, sender email address, and password for the Email Agent.
* **Agent Configuration:** Review and adjust any specific configurations for each agent (e.g., prompt templates for the Processing Agent).

### Running ApexSense

Provide instructions on how to run your application. This might involve running a main Python script or separate scripts for each agent.

```bash
# Example: Running the main application
python main.py
