from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import Token
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemMembersIdTokensEndpoint(ConnectWiseEndpoint, IPostable[Token, ConnectWiseManageRequestParams]):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "tokens", parent_endpoint=parent_endpoint)

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Token:
        """
        Performs a POST request against the /system/members/{id}/tokens endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Token: The parsed response data.
        """
        return self._parse_one(Token, super()._make_request("POST", data=data, params=params).json())
