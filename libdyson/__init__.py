"""Dyson Python library."""

from typing import Optional

from .const import (
    DEVICE_TYPE_360_EYE,
    DEVICE_TYPE_PURE_COOL,
    DEVICE_TYPE_PURE_COOL_DESK,
    DEVICE_TYPE_PURE_COOL_LINK,
    DEVICE_TYPE_PURE_COOL_LINK_DESK,
    DEVICE_TYPE_PURE_HOT_COOL,
    DEVICE_TYPE_PURE_HOT_COOL_LINK,
    DEVICE_TYPE_PURE_HUMIDIFY_COOL,
)
from .const import DEVICE_TYPE_NAMES  # noqa: F401
from .const import HumidifyOscillationMode  # noqa: F401
from .const import MessageType  # noqa: F401
from .const import WaterHardness  # noqa: F401
from .discovery import DysonDiscovery  # noqa: F401
from .dyson_360_eye import Dyson360Eye
from .dyson_360_eye import VacuumPowerMode  # noqa: F401
from .dyson_360_eye import VacuumState  # noqa: F401
from .dyson_device import DysonDevice
from .dyson_pure_cool import DysonPureCool
from .dyson_pure_cool_link import DysonPureCoolLink
from .dyson_pure_hot_cool import DysonPureHotCool
from .dyson_pure_hot_cool_link import DysonPureHotCoolLink
from .dyson_pure_humidify_cool import DysonPureHumidifyCool
from .utils import get_mqtt_info_from_wifi_info  # noqa: F401


def get_device(serial: str, credential: str, device_type: str) -> Optional[DysonDevice]:
    """Get a new DysonDevice instance."""
    if device_type == DEVICE_TYPE_360_EYE:
        return Dyson360Eye(serial, credential)
    if device_type in [
        DEVICE_TYPE_PURE_COOL_LINK_DESK,
        DEVICE_TYPE_PURE_COOL_LINK,
    ]:
        return DysonPureCoolLink(serial, credential, device_type)
    if device_type in [
        DEVICE_TYPE_PURE_COOL,
        DEVICE_TYPE_PURE_COOL_DESK,
    ]:
        return DysonPureCool(serial, credential, device_type)
    if device_type == DEVICE_TYPE_PURE_HOT_COOL_LINK:
        return DysonPureHotCoolLink(serial, credential, device_type)
    if device_type == DEVICE_TYPE_PURE_HOT_COOL:
        return DysonPureHotCool(serial, credential, device_type)
    if device_type == DEVICE_TYPE_PURE_HUMIDIFY_COOL:
        return DysonPureHumidifyCool(serial, credential, device_type)
    return None
