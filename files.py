"""
Utils for file handling
"""
from distutils.dir_util import copy_tree
from glob import iglob
from os import remove
from os.path import isdir, isfile
from shutil import rmtree
from typing import Generator, Callable, TextIO, Tuple, Iterator


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


# noinspection PyUnusedFunction
def remove_folders(*folders: str):
    """
    Delete all the given folders

    :param folders: List of folders to be deleted
    """
    for f in folders:
        if isdir(f):
            rmtree(f)


# noinspection PyUnusedFunction
def remove_files(*files: str):
    """
    Delete all the given files

    :param files: List of files to be deleted
    """
    for file in files:
        if isfile(file):
            remove(file)


# noinspection PyUnusedFunction
def copy_folders(*folders: Tuple[str, str]):
    """
    Copy all files from one folder to another

    :param folders: A list of tuples with 2 strings
                with the first one representing the
                source folder and the second the destination
    """
    for (src, dest) in folders:
        if isdir(src) and isdir(dest):
            copy_tree(src, dest)


# noinspection PyUnusedFunction
def deep_replace_file_contents(root_folder: str, *content_replace: Tuple[str, str]):
    """
    Recursively iterate over all files inside the root_folder and
    its subdirectories and replace the content of all files with
    the given replace instructions

    :param root_folder: Folder within all subfiles will have its
                    contents replaced
    :param content_replace: List of tuples where each should have
                        2 strings, the first representing the
                        content to be replaced and and the second
                        representing what will be used instead
    """
    if isdir(root_folder):
        for file in list_files_in_dir(root_folder):
            with open(file) as fin:
                content = fin.read()
                for (original, replace) in content_replace:
                    content = content.replace(original, replace)
            with open(file, "w") as fout:
                fout.write(content)


# noinspection PyUnusedFunction
def chars_in_file(file_name: str) -> Iterator[chr]:
    """
    An iterator yielding all characters of a given file
    :param file_name: Name of the file to be read
    :return: An iterator iterating through all letters of the given file
    """
    with open(file_name) as file:
        for line in file.readlines():
            for letter in line:
                yield letter
