# generic_text_logger

A tabular text-based logger for easy row by row logging, useful for debugging database and similar code.

Included sample.py gives example of usage:

```
from generic_text_logger import *

sample_title_array = ["Value 1", "Value 2", "Value 3", "Value 4"]
value_array = [1, 2, 3, 4]

rows = 10

for index in range(0,rows):
	
	for current_index, current_value in enumerate(value_array):
		value_array[current_index] = float(current_value) * 2
	# End For
	
	write_log_entry(sample_title_array, index, sys.stdout, value_array)

# End For
```
