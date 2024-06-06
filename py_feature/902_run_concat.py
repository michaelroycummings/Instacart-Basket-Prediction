"""
nohup python -u 902_run_concat.py > log_run_concat.txt &
"""

import os
import utils
utils.start(__file__)

os.system('python -u 501_concat.py')
os.system('python -u 502_concat.py')

utils.end(__file__)