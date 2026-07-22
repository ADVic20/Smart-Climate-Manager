"""Service layer for controlling real climate entities."""

from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.components.climate import (
    DOMAIN as CLIMATE_DOMAIN,
    SERVICE_TURN_ON,
    SERVICE_TURN_OFF,
    SERVICE_SET_TEMPERATURE,
    SERVICE_SET_HVAC_MODE,
)


class ClimateService:
    """Handle communication with Home Assistant climate services."""

    def __init__(
        self,
        hass: HomeAssistant,
    ) -> None:

        self.hass = hass


    async def turn_on(
        self,
        entity_id: str,
    ) -> None:
        """Turn on the real climate."""

        await self.hass.services.async_call(
            CLIMATE_DOMAIN,
            SERVICE_TURN_ON,
            {
                "entity_id": entity_id,
            },
            blocking=True,
        )


    async def turn_off(
        self,
        entity_id: str,
    ) -> None:
        """Turn off the real climate."""

        await self.hass.services.async_call(
            CLIMATE_DOMAIN,
            SERVICE_TURN_OFF,
            {
                "entity_id": entity_id,
            },
            blocking=True,
        )


    async def set_temperature(
        self,
        entity_id: str,
        temperature: float,
    ) -> None:
        """Set target temperature."""

        await self.hass.services.async_call(
            CLIMATE_DOMAIN,
            SERVICE_SET_TEMPERATURE,
            {
                "entity_id": entity_id,
                "temperature": temperature,
            },
            blocking=True,
        )


    async def set_hvac_mode(
        self,
        entity_id: str,
        hvac_mode: str,
    ) -> None:
        """Change HVAC mode."""

        await self.hass.services.async_call(
            CLIMATE_DOMAIN,
            SERVICE_SET_HVAC_MODE,
            {
                "entity_id": entity_id,
                "hvac_mode": hvac_mode,
            },
            blocking=True,
        )
