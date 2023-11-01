from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class ProcurementRmastatusesIdEmailtemplatesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "emailTemplates", parent_endpoint=parent_endpoint
        )
