import voluptuous as vol

from esphomeyaml.components import binary_sensor, display
from esphomeyaml.components.display.nextion import Nextion
import esphomeyaml.config_validation as cv
from esphomeyaml.const import CONF_COMPONENT_ID, CONF_NAME, CONF_PAGE_ID
from esphomeyaml.helpers import get_variable

DEPENDENCIES = ['display']

CONF_NEXTION_ID = 'nextion_id'

NextionTouchComponent = display.display_ns.NextionTouchComponent

PLATFORM_SCHEMA = cv.nameable(binary_sensor.BINARY_SENSOR_PLATFORM_SCHEMA.extend({
    cv.GenerateID(): cv.declare_variable_id(NextionTouchComponent),
    vol.Required(CONF_PAGE_ID): cv.uint8_t,
    vol.Required(CONF_COMPONENT_ID): cv.uint8_t,
    cv.GenerateID(CONF_NEXTION_ID): cv.use_variable_id(Nextion)
}))


def to_code(config):
    hub = None
    for hub in get_variable(config[CONF_NEXTION_ID]):
        yield
    rhs = hub.make_touch_component(config[CONF_NAME], config[CONF_PAGE_ID],
                                   config[CONF_COMPONENT_ID])
    binary_sensor.register_binary_sensor(rhs, config)


def to_hass_config(data, config):
    return binary_sensor.core_to_hass_config(data, config)