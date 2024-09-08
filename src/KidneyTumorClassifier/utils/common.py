import os
from box.exceptions import BoxValueError
import yaml
from KidneyTumorClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, versbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if versbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"Json file saved as: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as f:
        content = json.load(f)
    logger.info(f"Json file is loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} Kb"

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(crappedImagePath):
    with open(crappedImagePath, "rb") as f:
        return base64.b64encode(f.read())

