from pathlib import Path

base = Path(".").resolve()
rename_map = {
    'Python 1': {
        'ex1.py': 'password_validator.py',
        'ex2.py': 'string_slice_demo.py',
        'q1.py': 'arithmetic_operations.py',
        'q2.py': 'string_concat_replication.py',
        'q3.py': 'variable_types_demo.py',
        'q4.py': 'age_group_classifier.py',
        'q5.py': 'even_odd_checker.py',
        'q6.py': 'comparison_operators_demo.py',
        'q7.py': 'boolean_operators_demo.py',
        'q8.py': 'sqrt_calculator.py',
        'q9.py': 'factorial_using_for_loop.py',
        'q10.py': 'add_two_numbers_function.py',
        'q11.py': 'list_tuple_sum.py',
        'q12.py': 'find_element_indices.py',
        'q13.py': 'build_list_tuple_from_input.py',
        'q14.py': 'list_tuple_slicing.py',
        'q15.py': 'list_insert_demo.py',
        'q16.py': 'list_append_demo.py',
        'q17.py': 'student_marks_dictionary.py',
        'q18.py': 'palindrome_checker.py',
        'q19.py': 'string_to_list_tuple.py',
        'q20.py': 'list_mutation_demo.py',
        'q21.py': 'string_analyzer.py',
        'q22.py': 'title_formatter.py',
        'q23.py': 'character_frequency_counter.py',
        'q24.py': 'password_strength_checker.py',
        'q25.py': 'reverse_word_order.py',
        'q26.py': 'append_data_to_file.py',
        'q27.py': 'search_word_in_file.py',
        'q28.py': 'filepath_analyzer.py',
        'q29.py': 'copy_file_content.py',
        'q30.py': 'file_word_counter.py',
        'q31.py': 'copy_txt_files.py',
        'q32.py': 'move_image_files.py',
        'q33.py': 'character_frequency_counter_dict.py',
        'q34.py': 'directory_traversal_os_walk.py',
        'q35.py': 'compress_folder_to_zip.py',
        'q36.py': 'positive_number_validator.py',
        'q37.py': 'traceback_example.py',
        'q38.py': 'assert_non_empty_list.py',
        'q40.py': 'debug_average_max.py',
        'q41.py': 'logging_example.py',
        'qa.py': 'screen_capture_cv2.py',
        'script.py': 'dummy_script.py',
        'sp.py': 'pdf_demo_fpdf.py',
    },
    'Python 2': {
        'ex1.py': 'hello_world_demo.py',
        'google.py': 'google_selenium_example.py',
        'python_basics.py': 'python_basics_notes.py',
        'requirement.txt': 'requirements.txt',
    },
}

for folder, files in rename_map.items():
    src_folder = base / folder
    if not src_folder.exists():
        print(f'MISSING FOLDER: {folder}')
        continue
    for old_name, new_name in files.items():
        old_path = src_folder / old_name
        new_path = src_folder / new_name
        if not old_path.exists():
            print(f'MISSING FILE: {old_path}')
            continue
        if new_path.exists():
            print(f'SKIP (target exists): {new_path}')
            continue
        old_path.rename(new_path)
        print(f'RENAMED: {old_path} -> {new_path}')

folder_renames = [('Python 1', 'semester_2'), ('Python 2', 'semester_5')]
for old_folder, new_folder in folder_renames:
    old_path = base / old_folder
    new_path = base / new_folder
    if not old_path.exists():
        print(f'MISSING FOLDER: {old_folder}')
        continue
    if new_path.exists():
        print(f'SKIP FOLDER RENAME (target exists): {new_path}')
        continue
    old_path.rename(new_path)
    print(f'RENAMED FOLDER: {old_path} -> {new_path}')
