import os
import shutil
import logging
from datetime import datetime


# -------------------------------
# Logging Configuration
# -------------------------------
logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# -------------------------------
# File Categories
# -------------------------------
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx"],
    "Text": [".txt"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Python": [".py"],
    "Excel": [".xls", ".xlsx"],
    "PowerPoint": [".ppt", ".pptx"]
}


# -------------------------------
# Find Category
# -------------------------------
def get_category(filename):
    extension = os.path.splitext(filename)[1].lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


# -------------------------------
# Organize Files
# -------------------------------
def organize_files(folder_path):

    if not os.path.exists(folder_path):
        print("Error: Folder does not exist.")
        logging.error(f"Folder does not exist: {folder_path}")
        return

    if not os.path.isdir(folder_path):
        print("Error: The provided path is not a folder.")
        logging.error(f"Path is not a folder: {folder_path}")
        return

    moved_count = 0

    try:
        for filename in os.listdir(folder_path):

            file_path = os.path.join(folder_path, filename)

            # Skip folders
            if os.path.isdir(file_path):
                continue

            category = get_category(filename)

            category_folder = os.path.join(folder_path, category)

            # Create category folder if it doesn't exist
            os.makedirs(category_folder, exist_ok=True)

            destination = os.path.join(category_folder, filename)

            # Handle duplicate filenames
            if os.path.exists(destination):
                name, extension = os.path.splitext(filename)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                new_filename = f"{name}_{timestamp}{extension}"
                destination = os.path.join(category_folder, new_filename)

            shutil.move(file_path, destination)

            moved_count += 1

            print(f"Moved: {filename} -> {category}/")

            logging.info(
                f"Moved {filename} -> {category}/{os.path.basename(destination)}"
            )

        print("\nFile organization completed successfully!")
        print(f"Total files organized: {moved_count}")

        logging.info(
            f"File organization completed. Total files moved: {moved_count}"
        )

    except PermissionError:
        print("Error: Permission denied while accessing a file or folder.")
        logging.exception("Permission error occurred.")

    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        logging.exception("Unexpected error occurred.")


# -------------------------------
# Main Program
# -------------------------------
def main():

    print("=" * 50)
    print("       PYTHON FILE ORGANIZER")
    print("=" * 50)

    folder_path = input(
        "\nEnter the folder path you want to organize: "
    ).strip()

    organize_files(folder_path)


if __name__ == "__main__":
    main()