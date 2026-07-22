from __future__ import annotations

from homeassistant.components.climate import (
    DOMAIN,
    SERVICE_SET_HVAC_MODE,
    SERVICE_SET_TEMPERATURE,
    SERVICE_TURN_OFF,
    SERVICE_TURN_ON,
)


class ClimateService:

    def __init__(self, hass):
        self.hass = hass

    async def turn_on(self, entity_id):

        await self.hass.services.async_call(
            DOMAIN,
            SERVICE_TURN_ON,
            {
                "entity_id": entity_id,
            },
            blocking=True,
        )

    async def turn_off(self, entity_id):

        await self.hass.services.async_call(
            DOMAIN,
            SERVICE_TURN_OFF,
            {
                "entity_id": entity_id,
            },
            blocking=True,
        )

    async def set_temperature(
        self,
        entity_id,
        temperature,
    ):

        await self.hass.services.async_call(
            DOMAIN,
            SERVICE_SET_TEMPERATURE,
            {
                "entity_id": entity_id,
                "temperature": temperature,
            },
            blocking=True,
        )

    async def set_hvac_mode(
        self,
        entity_id,
        hvac_mode,
    ):

        await self.hass.services.async_call(
            DOMAIN,
            SERVICE_SET_HVAC_MODE,
            {
                "entity_id": entity_id,
                "hvac_mode": hvac_mode,
            },
            blocking=True,
        )
