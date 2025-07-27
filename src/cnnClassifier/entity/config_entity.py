 # src/cnnClassifier/entity/config_entity.py
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str  # Ensure this matches the key in config.yaml (source_URL vs source_url)
    file_id: str     # <--- THIS LINE IS CRUCIAL AND MUST BE PRESENT
    local_data_file: Path
    unzip_dir: Path

# Add other config classes below if they exist in your file
# For example:
# @dataclass(frozen=True)
# class PrepareBaseModelConfig:
#     root_dir: Path
#     base_model_path: Path
#     updated_base_model_path: Path
#
# @dataclass(frozen=True)
# class TrainingConfig:
#     root_dir: Path
#     trained_model_path: Path
