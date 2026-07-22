from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_NAME
from homeassistant.helpers import selector

from .const import (
    DOMAIN,
    CONF_ALLOW_FORCE,
    CONF_BLOCK_SENSORS,
    CONF_REAL_CLIMATE,
    CONF_VIRTUAL_CLIMATE,
)


class SmartClimateManagerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(
                title=user_input[CONF_NAME],
                data=user_input,
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_NAME): selector.TextSelector(),

                    vol.Required(
                        CONF_VIRTUAL_CLIMATE
                    ): selector.EntitySelector(
                        selector.EntitySelectorConfig(
                            domain="climate"
                        )
                    ),

                    vol.Required(
                        CONF_REAL_CLIMATE
                    ): selector.EntitySelector(
                        selector.EntitySelectorConfig(
                            domain="climate"
                        )
                    ),

                    vol.Optional(
                        CONF_BLOCK_SENSORS,
                        default=[],
                    ): selector.EntitySelector(
                        selector.EntitySelectorConfig(
                            domain="binary_sensor",
                            multiple=True,
                        )
                    ),

                    vol.Required(
                        CONF_ALLOW_FORCE,
                        default=False,
                    ): selector.BooleanSelector(),
                }
            ),
        )
