"""Climate context models for Smart Climate Manager."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class ClimateConfig:
    """Static configuration of a managed climate."""

    unique_id: str

    name: str

    virtual_climate: str

    real_climate: str

    allow_force: bool = False

    sensors: list[str] = field(
        default_factory=list
    )


@dataclass(slots=True)
class ClimateState:
    """Dynamic state of the climate."""

    available: bool = False

    is_on: bool = False

    hvac_mode: str | None = None

    hvac_action: str | None = None

    current_temperature: float | None = None

    target_temperature: float | None = None

    fan_mode: str | None = None

    swing_mode: str | None = None

    preset_mode: str | None = None

    current_humidity: int | None = None


class ClimateContext:
    """Main context shared between Smart Climate modules."""

    def __init__(
        self,
        config: ClimateConfig,
    ) -> None:

        self.config = config

        self.state = ClimateState()
