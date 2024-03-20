import os
import io
import hashlib
import zipfile


def create_directory(directory_path: str) -> None:
    """This function creates directory if it doesn't exist"""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def create_hash_key(input_string: str) -> str:
    """This function creates md5 hash key based on input string"""
    return hashlib.md5(input_string.encode("utf-8")).hexdigest()


def unzip_bytes_data(zip_data, extract_path) -> None:
    """This function unzips bytes and extracts into a folder"""

    zip_buffer = io.BytesIO(zip_data)
    with zipfile.ZipFile(zip_buffer, "r") as zip_ref:
        zip_ref.extractall(extract_path)

