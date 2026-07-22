"""Validation logic for Smart Climate Manager."""

from __future__ import annotations

from dataclasses import dataclass

from homeassistant.core import HomeAssistant


@dataclass(slots=True)
class ValidationResult:
    """Result of climate validation."""

    allowed: bool

    sensor_id: str | None = None

    message: str | None = None


class SensorValidator:
    """Validate sensors before turning on climate."""

    def __init__(
        self,
        hass: HomeAssistant,
    ) -> None:

        self.hass = hass


    async def validate(
        self,
        sensors: list[str],
    ) -> ValidationResult:
        """
        Check all configured blocking sensors.

        Sensors are expected to be binary_sensor entities.
        """

        for sensor_id in sensors:

            state = self.hass.states.get(
                sensor_id
            )

            if state is None:
                continue


            # Open states that block climate

            if state.state in (
                "on",
                "open",
                "detected",
            ):

                return ValidationResult(
                    allowed=False,
                    sensor_id=sensor_id,
                    message=(
                        f"Sensor {sensor_id} is open"
                    ),
                )


        return ValidationResult(
            allowed=True
        )
