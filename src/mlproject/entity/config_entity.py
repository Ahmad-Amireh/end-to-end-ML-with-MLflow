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

@dataclass(frozen=True)
class DataValidationConfig: 
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: str
    all_schema: dict  

@dataclass(frozen=True) 
class DataTransformationConfig :
    root_dir : Path
    data_path : Path

@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir : Path
    train_data_path : Path
    test_data_path : Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str 


@dataclass(frozen=True)
class ModelEvaluationConfig: 
    root_dir: Path
    test_data_path: Path
    model_path: Path
    metric_file_name: Path
    all_params: dict
    target_column: str 
    repo_owner: str 
    repo_name: str