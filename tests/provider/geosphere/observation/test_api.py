from datetime import datetime

import pytest

from wetterdienst import Parameter
from wetterdienst.provider.geosphere.observation import GeosphereObservationRequest, GeosphereObservationResolution


@pytest.mark.remote
def test_geopshere_observation_api():
    """Test the correct parsing of data, especially the dates -> thanks @mhuber89 for the discovery and fix"""
    stations_at = GeosphereObservationRequest(
        parameter=[Parameter.WIND_SPEED],
        resolution=GeosphereObservationResolution.HOURLY,
        start_date=datetime(2022, 6, 1),
        end_date=datetime(2022, 6, 2),
    )
    station_at = stations_at.filter_by_station_id("4821")
    df = station_at.values.all().df
    assert df.get_column("value").is_not_null().sum() == 25