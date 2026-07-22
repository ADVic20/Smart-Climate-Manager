from __future__ import annotations

from homeassistant.core import HomeAssistant


class ClimateController:

    def __init__(
        self,
        hass: HomeAssistant,
        climate,
        validator,
        confirmation,
        service,
    ):

        self.hass = hass
        self.climate = climate

        self.validator = validator
        self.confirmation = confirmation
        self.service = service

    async def turn_on(self):

        valid, sensor = await self.validator.validate(
            self.climate.block_sensors
        )

        if not valid:

            sensor_name = sensor.name

            if self.climate.allow_force:

                accepted = await self.confirmation.ask_force(
                    self.climate.name,
                    sensor_name,
                )

                if not accepted:
                    return

            else:

                await self.confirmation.notify_blocked(
                    self.climate.name,
                    sensor_name,
                )

                return

        await self.service.turn_on(
            self.climate.real_climate
        )

    async def turn_off(self):

        await self.service.turn_off(
            self.climate.real_climate
        )

    async def set_temperature(
        self,
        temperature,
    ):

        await self.service.set_temperature(
            self.climate.real_climate,
            temperature,
        )

    async def set_hvac_mode(
        self,
        hvac_mode,
    ):

        await self.service.set_hvac_mode(
            self.climate.real_climate,
            hvac_mode,
        )
