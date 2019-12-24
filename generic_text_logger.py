#!/usr/bin/python3

import sys

###########################################
def write_log_header(title_array, file_handle):
		
	title_string = ""
	
	border_string = ""
	
	for index, title in enumerate(title_array):
		current_length = len(title) + 2
		border_string = border_string + "-"
		border_string = border_string + ("-" * current_length)
	# End For	
	border_string = border_string + "-"
	
	file_handle.write(border_string + "\n")
	
	for index, title in enumerate(title_array):
		title_string = title_string + "| " + title + " "
	# End For
	title_string = title_string + "|"
	
	border_string = ""
	
	file_handle.write(title_string + "\n")
	
	for index, title in enumerate(title_array):
		current_length = len(title) + 2
		border_string = border_string + "|"
		border_string = border_string + ("-" * current_length)
	# End For	
	border_string = border_string + "|"
	
	file_handle.write(border_string + "\n")
	
# End Function
###########################################
def write_log_entry(title_array, current_row_index, file_handle, value_array):
	
	if current_row_index % 40 == 0:
		write_log_header(title_array, file_handle)
	# End If
	
	for current_index, each_item in enumerate(value_array):
		value_array[current_index] = str(each_item)
	# End For
	
	string_length_array = []
	
	for each_item in value_array:		
		string_length_array.append(len(each_item))
	# End For		
	
	num_dashes = []
	
	for index, title in enumerate(title_array):
		num_dashes.append((len(title) + 2) - string_length_array[index] - 1)
	# End For
	
	final_string = "|"
	
	for current_index, each_item in enumerate(value_array):
		final_string = final_string + " " + each_item + (" " * num_dashes[current_index]) + "|"
	# End For	
	
	file_handle.write(final_string + "\n")	
	
# End Function
###########################################
