class SmartClimateManager(ClimateEntity):

    ...

    async def async_turn_on(self):

        await self.controller.turn_on()

    async def async_turn_off(self):

        await self.controller.turn_off()

    async def async_set_temperature(self, **kwargs):

        await self.controller.set_temperature(
            kwargs.get("temperature")
        )

    async def async_set_hvac_mode(self, hvac_mode):

        await self.controller.set_hvac_mode(
            hvac_mode
        )
