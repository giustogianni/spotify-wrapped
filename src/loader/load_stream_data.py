import json
from pathlib import Path
from typing import Dict, List, Union

import psycopg2.extras as p

from utils.paths import STREAM_FILE, STREAM_DIR
from utils.db import WarehouseConnection
from utils.config import get_warehouse_creds

def _get_stream_data_insert_query() -> str:
    return """
    INSERT INTO spotify.stream(
        ts, 
        username, 
        platform, 
        ms_played, 
        conn_country,
        ip_addr_decrypted, 
        user_agent_decrypted,
        master_metadata_track_name,
        master_metadata_album_artist_name,
        master_metadata_album_album_name,
        spotify_track_uri, 
        episode_name,
        episode_show_name, 
        spotify_episode_uri, 
        reason_start,
        reason_end, 
        shuffle, 
        skipped, 
        offline, 
        offline_timestamp,
        incognito_mode
    )

    VALUES (
        %(ts)s,
        %(username)s,
        %(platform)s,
        %(ms_played)s,
        %(conn_country)s,
        %(ip_addr_decrypted)s,
        %(user_agent_decrypted)s,
        %(master_metadata_track_name)s,
        %(master_metadata_album_artist_name)s,
        %(master_metadata_album_album_name)s,
        %(spotify_track_uri)s,
        %(episode_name)s,
        %(episode_show_name)s,
        %(spotify_episode_uri)s,
        %(reason_start)s,
        %(reason_end)s,
        %(shuffle)s,
        %(skipped)s,
        %(offline)s,
        %(offline_timestamp)s,
        %(incognito_mode)s
    )
    """

def get_stream(stream_file: Path = STREAM_FILE) -> List[Dict[str, Union[str, int, bool]]]:
    f = open(stream_file)
    streams = json.load(f)

    return [stream for stream in streams]

def get_stream_data(stream_dir: Path = STREAM_DIR) -> List[Dict[str, Union[str, int, bool]]]:
    files = [file for file in stream_dir.iterdir() if file.suffix=='.json']
    
    history = []
    for file in files:
        streams = get_stream(file)
        history += streams

    return history

def load_stream_data():
    stream_data = get_stream_data()
    with WarehouseConnection(get_warehouse_creds()).managed_cursor() as curr:
        p.execute_batch(curr, _get_stream_data_insert_query(), stream_data)


if __name__ == "__main__":
    load_stream_data()