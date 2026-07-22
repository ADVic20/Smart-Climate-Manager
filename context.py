from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ClimateContext:

    #
    # Configuración
    #

    unique_id: str

    name: str

    virtual_climate: str

    real_climate: str

    allow_force: bool

    sensors: list[str] = field(default_factory=list)

    #
    # Estado
    #

    state: str | None = None

    current_temperature: float | None = None

    target_temperature: float | None = None

    hvac_mode: str | None = None

    fan_mode: str | None = None

    swing_mode: str | None = None
