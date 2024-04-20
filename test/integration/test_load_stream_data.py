import pytest
from src.loader.load_stream_data import load_stream_data
from utils.db import WarehouseConnection
from utils.config import get_warehouse_creds


def _truncate_stream_data():
    with WarehouseConnection(get_warehouse_creds()).managed_cursor() as curr:
        curr.execute("Truncate table spotify.stream;")


@pytest.fixture()
def set_up_tear_down():
    # Clean up existing data
    _truncate_stream_data()
    yield
    _truncate_stream_data()


class TestLoadStreamData:
    def test_load_stream_data(self, set_up_tear_down):
        load_stream_data()
        with WarehouseConnection(
            get_warehouse_creds()
        ).managed_cursor() as curr:
            curr.execute("select count(*) from spotify.stream;")
            d = curr.fetchone()

        assert d[0] == 17