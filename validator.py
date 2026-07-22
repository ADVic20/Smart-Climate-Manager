from __future__ import annotations


class SensorValidator:

    def __init__(self, hass):
        self.hass = hass

    async def validate(self, sensors):

        for entity_id in sensors:

            state = self.hass.states.get(entity_id)

            if state and state.state == "on":
                return False, state

        return True, None
