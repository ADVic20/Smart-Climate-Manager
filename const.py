"""Constants for Smart Climate Manager."""

from __future__ import annotations


# Domain name
DOMAIN = "smart_climate_manager"


# Platforms loaded by Home Assistant
PLATFORMS: list[str] = [
    "climate",
]


# Config keys

CONF_NAME = "name"

CONF_REAL_CLIMATE = "real_climate"

CONF_VIRTUAL_CLIMATE = "virtual_climate"

CONF_ALLOW_FORCE = "allow_force"

CONF_BLOCK_SENSORS = "block_sensors"


# Default values

DEFAULT_ALLOW_FORCE = False


# Events

EVENT_CONFIRMATION_REQUIRED = (
    "smart_climate_manager_confirmation_required"
)

EVENT_CONFIRMATION_RESPONSE = (
    "smart_climate_manager_confirmation_response"
)


# Version

VERSION = "0.1.0"
