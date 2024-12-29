from dataclasses import dataclass
from pathlib import Path 

# in python calss actually if you are defining class variables you need to give self .
# if you want to define the variable you can use something called Data class 
#the same thing in yaml (variable will return)
#it's return data class 
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path 
    unzip_dir: Path 

@dataclass 
class DataValidationConfig: 
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: str
    all_schema: dict  