from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ClimateConfig:

    unique_id: str

    name: str

    virtual_climate: str

    real_climate: str

    allow_force: bool

    sensors: list[str] = field(default_factory=list)


@dataclass(slots=True)
class ClimateState:

    available: bool = False

    is_on: bool = False

    hvac_mode: str | None = None

    hvac_action: str | None = None

    current_temperature: float | None = None

    target_temperature: float | None = None

    target_temperature_high: float | None = None

    target_temperature_low: float | None = None

    fan_mode: str | None = None

    swing_mode: str | None = None

    preset_mode: str | None = None

    humidity: int | None = None

    target_humidity: int | None = None


class ClimateContext:

    def __init__(self, config: ClimateConfig):

        self.config = config

        self.state = ClimateState()
