from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemQuotelinksetupCountEndpoint import (
    SystemQuotelinksetupCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemQuotelinksetupIdEndpoint import (
    SystemQuotelinksetupIdEndpoint,
)
from pyconnectwise.endpoints.manage.SystemQuotelinksetupTestconnectionEndpoint import (
    SystemQuotelinksetupTestconnectionEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import QuoteLink
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemQuotelinksetupEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[QuoteLink], ConnectWiseManageRequestParams],
    IPostable[QuoteLink, ConnectWiseManageRequestParams],
    IPaginateable[QuoteLink, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "quoteLinkSetup", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[QuoteLink])
        IPostable.__init__(self, QuoteLink)
        IPaginateable.__init__(self, QuoteLink)

        self.count = self._register_child_endpoint(
            SystemQuotelinksetupCountEndpoint(client, parent_endpoint=self)
        )
        self.test_connection = self._register_child_endpoint(
            SystemQuotelinksetupTestconnectionEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemQuotelinksetupIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SystemQuotelinksetupIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemQuotelinksetupIdEndpoint: The initialized SystemQuotelinksetupIdEndpoint object.
        """
        child = SystemQuotelinksetupIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[QuoteLink]:
        """
        Performs a GET request against the /system/quoteLinkSetup endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[QuoteLink]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            QuoteLink,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[QuoteLink]:
        """
        Performs a GET request against the /system/quoteLinkSetup endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[QuoteLink]: The parsed response data.
        """
        return self._parse_many(
            QuoteLink, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> QuoteLink:
        """
        Performs a POST request against the /system/quoteLinkSetup endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            QuoteLink: The parsed response data.
        """
        return self._parse_one(
            QuoteLink, super()._make_request("POST", data=data, params=params).json()
        )
