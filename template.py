import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format='[(asctime)s]:%(messgae)s:')

project_name = "testsummarizer"
list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utlis/__init__.py',
    f'src/{project_name}/utlis/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/config.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb'  
]

for filepath in list_of_files:
    filepath = Path(filepath)
    if not filepath.parent.exists():
        logging.info(f"Creating directory: {filepath.parent} for file: {filepath.name}")
        os.makedirs(filepath.parent)

    if not filepath.exists() or os.path.getsize(filepath) == 0:
        logging.info(f"Creating file: {filepath}")
        filepath.touch()
    else:
        logging.warning(f"File already exists: {filepath}")
        continue    # Skip if file already exists       
logging.info("Project structure created successfully!")

    