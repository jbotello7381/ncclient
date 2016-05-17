from .default import DefaultDeviceHandler
from ncclient.operations.third_party.juniper.rpc import ExecuteRpc

class AluDeviceHandler(DefaultDeviceHandler):
    """
    Alcatel-Lucent 7x50 handler for device specific information.
    """

    def __init__(self, device_params):
        super(AluDeviceHandler, self).__init__(device_params)

    def add_additional_operations(self):
        dict = {}
        dict["rpc"] = ExecuteRpc
        return dict

    def get_capabilities(self):
        return [
            "urn:ietf:params:netconf:base:1.0",
        ]

