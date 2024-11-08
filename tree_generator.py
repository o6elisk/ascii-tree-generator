#!/usr/bin/env python3
import os
from pathlib import Path

# Directories and files to ignore
IGNORE_PATTERNS = {
    # Version Control
    '.git',
    '.gitignore',
    '.svn',
    
    # IDE and Editor files
    '.idea',
    '.vscode',
    '.sublime-*',
    
    # Python specific
    '__pycache__',
    'venv',
    'env',
    '.env',
    '.venv',
    '*.pyc',
    '*.pyo',
    '*.pyd',
    '.Python',
    'pip-log.txt',
    'pip-delete-this-directory.txt',
    '.tox',
    '.coverage',
    '.coverage.*',
    '.cache',
    'nosetests.xml',
    'coverage.xml',
    '*.cover',
    '.pytest_cache',
    '.python-version',
    
    # FastAPI/Python packages
    'dist',
    'build',
    '*.egg-info',
    'eggs',
    'parts',
    'bin',
    'var',
    'sdist',
    'develop-eggs',
    '.installed.cfg',
    
    # Logs and databases
    '*.log',
    '*.sqlite',
    '*.db',
    
    # OS specific
    '.DS_Store',
    'Thumbs.db',
    
    # Dependencies
    'node_modules',
    'bower_components',
    
    # Docker
    '.docker',
    
    # Virtual Environments
    '.python-version',  # pyenv
    '.env-*',          # custom envs
    
    # MyPy
    '.mypy_cache',
    '.dmypy.json',
    'dmypy.json',
    
    # IPython
    '.ipynb_checkpoints',
    
    # Celery
    'celerybeat-schedule',
    'celerybeat.pid'
}

def should_ignore(path):
    """Check if the path should be ignored based on IGNORE_PATTERNS."""
    return any(
        ignored in str(path) 
        for ignored in IGNORE_PATTERNS
    )

def generate_tree(directory='.', prefix='', is_last=True, file=None):
    """Generate a tree structure starting from the given directory."""
    # Get the directory path
    path = Path(directory)
    
    # Prepare the output line
    if directory != '.':
        connector = '└──' if is_last else '├──'
        line = f'{prefix}{connector} {path.name}{"/" if path.is_dir() else ""}'
    else:
        line = '.'
    
    # Print and write to file if specified
    print(line)
    if file:
        file.write(line + '\n')
    
    # If it's a directory, process its contents
    if path.is_dir():
        # Get all items in directory, excluding ignored ones
        items = [
            item for item in sorted(path.iterdir())
            if not should_ignore(item)
        ]
        
        # Process each item
        for index, item in enumerate(items):
            # Determine the new prefix for the next level
            if directory == '.':
                new_prefix = ''
            else:
                new_prefix = prefix + ('    ' if is_last else '│   ')
            
            # Recursively generate tree for this item
            generate_tree(
                item,
                prefix=new_prefix,
                is_last=(index == len(items) - 1),
                file=file
            )

if __name__ == '__main__':
    # Print to console and save to file
    with open('directory_structure.txt', 'w') as f:
        generate_tree(file=f) 
