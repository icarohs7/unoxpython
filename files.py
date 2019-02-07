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
def file_copy_content(
        input_file_path: str,
        output_file_path: str,
        input_processor: Callable[[str], str] = lambda s: s,
        output_file_permissions: str = "a"
):
    """
    Copy the contents of the given input file to
    the output file

    :param input_file_path: Path of the input file
    :param output_file_path: Path of the output file
    :param input_processor: Callable invoked on the content
                            on the input file, using the output
                            of the function as the content to be
                            written to the output file, default
                            to the original content of the input
    :param output_file_permissions: Permission used by the
                    output file, default to `a` (append)
    """
    with open(input_file_path) as fin:
        with open(output_file_path, output_file_permissions) as fout:
            fout.write(input_processor(fin.read()))


# noinspection PyUnusedFunction
def file_input(input_file_path: str, handler: Callable[[TextIO], None]):
    """
    Open the given file in input mode,
    invoke the handler on it and finally
    close it

    :param input_file_path: Path of the file to be opened
    :param handler: Callable handling the file input
    """
    with open(input_file_path) as fin:
        handler(fin)


# noinspection PyUnusedFunction
def file_output(
        output_file_path: str,
        handler: Callable[[TextIO], None],
        output_file_permissions: str = "a"
):
    """
    Open the given file in output mode,
    invoke the handler on it and finally
    close it

    :param output_file_path: Path of the file to be opened
    :param handler: Callable handling the file input
    :param output_file_permissions: Permission used by the
                                    file, default to `a` (append)
    """
    with open(output_file_path, output_file_permissions) as fout:
        handler(fout)


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
    """
    with open(input_file_path) as fin:
        with open(output_file_path, output_file_permissions) as fout:
            handler(fin, fout)
