# Data Cleansing and Extraction Tool

## Overview

This Python script simplifies the process of cleansing data from a CSV file and extracting it into a JSON file. Below is a step-by-step guide on how to use the script.

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Sample Bash Script
If you want to automate the process using a Bash script, you can create a <run_script.sh> file with the following content:

```bash
#!/bin/bash

git clone https://github.com/your-username/your-repo.git
cd your-repo
python cleansing_data.py
```

Make the script executable:

```bash
chmod +x run_script.sh
```

Run the script:

```bash
./run_script.sh
```

### 3. Check the Output
After running the script, you'll find the cleaned data in JSON format in the specified output directory.