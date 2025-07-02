# Example: Reading and writing files as sequences of lines in Python.
# The 'os' module is used here to check if a file exists.
import os
filename = '18_test.yaml'
line_count = 0

# sample_data contains example lines to be written to the file if it does not exist
sample_data = """Sample line 1
Sample line 2
Sample line 3
"""

def ensure_sample_file(filename, sample_data):
    """
    Checks if the file exists, and if not, creates it with the provided sample data.
    """
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write(sample_data)
print(f"Reading from file: {filename}")

# Ensure the sample file exists before proceeding
ensure_sample_file(filename, sample_data)
