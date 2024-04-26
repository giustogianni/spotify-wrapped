from pathlib import Path

# root directory
ROOT_DIR = Path(__file__).absolute().parents[1]

# data directory
DATA_DIR = ROOT_DIR.joinpath("data")
STREAM_DIR = DATA_DIR.joinpath("stream")
STREAM_FILE = DATA_DIR.joinpath('endsong_0_tiny.json')