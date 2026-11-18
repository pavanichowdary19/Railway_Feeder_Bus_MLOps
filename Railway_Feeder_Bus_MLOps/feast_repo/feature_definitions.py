
from datetime import timedelta
from feast import Entity, FeatureView, Field, FileSource
from feast.types import Int64, Float64

transfer = Entity(
    name="transfer",
    join_keys=["transfer_id"]
)

transfer_source = FileSource(
    path="data/transfer_features.parquet",
    timestamp_field="event_timestamp"
)

transfer_features_view = FeatureView(
    name="railway_transfer_features",
    entities=[transfer],
    ttl=timedelta(days=365),
    schema=[
        Field(name="train_delay_min", dtype=Int64),
        Field(name="distance_m", dtype=Int64),
        Field(name="walking_speed_mps", dtype=Float64),
        Field(name="scheduled_transfer_min", dtype=Int64),
        Field(name="estimated_walking_time", dtype=Float64),
        Field(name="transfer_time_margin", dtype=Float64)
    ],
    source=transfer_source
)
