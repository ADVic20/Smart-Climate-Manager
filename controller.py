from __future__ import annotations

from homeassistant.core import HomeAssistant


class ClimateController:

    def __init__(self, hass: HomeAssistant, climate):
        self.hass = hass
        self.climate = climate

    async def turn_on(self):
        pass

    async def turn_off(self):
        pass

    async def set_temperature(self, temperature):
        pass

    async def set_hvac_mode(self, hvac_mode):
        pass
