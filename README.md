# Python File Organizer

A Python automation script that automatically organizes files into folders based on their file type.

## 📌 Project Overview

The Python File Organizer is a simple automation tool that reduces manual file management.

The user provides a folder path, and the program scans the files inside it and moves them into appropriate categories such as Images, Documents, Audio, Python, and Text.

## 🎯 Objective

The main objective is to automate common file management tasks such as:

- Organizing files
- Sorting files by extension
- Creating folders automatically
- Moving files safely
- Recording file operations
- Handling invalid user input

## 🛠️ Technologies Used

- Python 3
- OS module
- Shutil module
- Logging module
- Exception handling

## ✨ Features

### 1. Automatic File Organization
Files are automatically moved into folders based on their extensions.

### 2. Multiple File Categories

The program supports:

| Category | File Types |
|----------|------------|
| Images | JPG, JPEG, PNG, GIF, BMP |
| Documents | PDF, DOC, DOCX |
| Text | TXT |
| Audio | MP3, WAV, AAC |
| Videos | MP4, MKV, AVI |
| Python | PY |
| Excel | XLS, XLSX |
| PowerPoint | PPT, PPTX |
| Others | Unsupported file types |

### 3. User Input

The user enters the folder path that needs to be organized.

### 4. Error Handling

The program handles invalid folder paths and permission errors without crashing.

### 5. Operation Logging

All file operations are recorded in `automation.log`.

### 6. Duplicate File Handling

If a file with the same name already exists in the destination folder, the program creates a unique filename using a timestamp.

## 📂 Project Structure

```text
Python-File-Organizer/
│
├── file_organizer.py
├── automation.log
├── README.md
│
└── test_files/
    ├── Audio/
    ├── Documents/
    ├── Images/
    ├── Python/
    └── Text/