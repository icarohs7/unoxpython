"""
Utils for file handling
"""

from glob import iglob
from typing import Generator, Callable, TextIO


# noinspection PyUnusedFunction
def list_files_in_dir(dir_path: str) -> Generator:
    """
    List all files within a directory, including its subdirectories

    :param dir_path: Root directory to execute the search in
    :return: The Generator yielding the names of the directories
    """
    return iglob(dir_path + "/**/*.*", recursive=True)


# noinspection PyUnusedFunction
def open_in_out_files(
        input_file_path: str,
        output_file_path: str,
        handler: Callable[[TextIO, TextIO], None],
        output_file_permissions: str = "a"
):
    """
    Open the given files for input and output and invoke
    the given handler using then in the respective order,
    finally closing both

    :param input_file_path: Path of the input file
    :param output_file_path: Path of the output file
    :param handler: Handler used to operate on the files,
                    with its first parameter being the input
                    file and the second the output
    :param output_file_permissions: Permission used by the
                    output file, default to `a` (append)
    :return:
    """
    with open(input_file_path) as fin:
        with open(output_file_path, output_file_permissions) as fout:
            handler(fin, fout)
