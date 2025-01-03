from pathlib import Path

# Get current working directory
current_dir = Path.cwd()

# Define paths
CONFIG_FILE_PATH = current_dir / "config" / "config.yaml"
PARAMS_FILE_PATH = current_dir / "params.yaml"