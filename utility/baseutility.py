import json
import logging


class Baseutility:
    # log information
    def log_info(self, informationmessage):
        logging.info(informationmessage)

    # log error
    def log_error(self, errormessage):
        logging.error(errormessage)

    # logging for debugging
    def log_debug(self, debugmessage):
        logging.debug(debugmessage)

    # logging for warning
    def log_warning(self, warningmessage):
        logging.warning(warningmessage)

    # logging for critical
    def log_critical(self, criticalmessage):
        logging.critical(criticalmessage)

    # Set window size
    def set_windowsize(self, driver, height, width):
        window_height = int(height)
        window_width = int(width)
        self.log_info("setting window size to " + str(window_width) + "x" + str(window_height))
        driver.set_window_size(window_height, window_width)

    def parse_config(self, config_type, p_datatype, c_datatype):
        try:
            json_obj = ""
            config_path = "configurations/"
            if config_type == "project_config":
                json_config_path = config_path + "projectconfig.json"
                #configurations/projectconfig.json
                with open(json_config_path, "r") as jsonobj:
                    jsondata = json.load(jsonobj)
                    json_obj = jsondata.get(p_datatype).get(c_datatype)
            return json_obj
        except KeyError as e:
            self.log_error(e)