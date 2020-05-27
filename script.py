from datetime import datetime
import requests
import os
import sys

r = requests.get("https://python.org")
print(r.status_code)
