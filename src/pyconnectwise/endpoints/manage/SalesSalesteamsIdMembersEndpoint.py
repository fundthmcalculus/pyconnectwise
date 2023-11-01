from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesSalesteamsIdMembersCountEndpoint import (
    SalesSalesteamsIdMembersCountEndpoint,
)
from pyconnectwise.endpoints.manage.SalesSalesteamsIdMembersIdEndpoint import (
    SalesSalesteamsIdMembersIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import SalesTeamMember
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SalesSalesteamsIdMembersEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[SalesTeamMember], ConnectWiseManageRequestParams],
    IPostable[SalesTeamMember, ConnectWiseManageRequestParams],
    IPaginateable[SalesTeamMember, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "members", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[SalesTeamMember])
        IPostable.__init__(self, SalesTeamMember)
        IPaginateable.__init__(self, SalesTeamMember)

        self.count = self._register_child_endpoint(
            SalesSalesteamsIdMembersCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SalesSalesteamsIdMembersIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SalesSalesteamsIdMembersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SalesSalesteamsIdMembersIdEndpoint: The initialized SalesSalesteamsIdMembersIdEndpoint object.
        """
        child = SalesSalesteamsIdMembersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[SalesTeamMember]:
        """
        Performs a GET request against the /sales/salesTeams/{id}/members endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SalesTeamMember]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SalesTeamMember,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[SalesTeamMember]:
        """
        Performs a GET request against the /sales/salesTeams/{id}/members endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SalesTeamMember]: The parsed response data.
        """
        return self._parse_many(
            SalesTeamMember,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> SalesTeamMember:
        """
        Performs a POST request against the /sales/salesTeams/{id}/members endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SalesTeamMember: The parsed response data.
        """
        return self._parse_one(
            SalesTeamMember,
            super()._make_request("POST", data=data, params=params).json(),
        )
