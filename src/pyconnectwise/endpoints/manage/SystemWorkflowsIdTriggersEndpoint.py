from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdTriggersCountEndpoint import (
    SystemWorkflowsIdTriggersCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemWorkflowsIdTriggersIdEndpoint import (
    SystemWorkflowsIdTriggersIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import WorkflowTrigger
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemWorkflowsIdTriggersEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[WorkflowTrigger], ConnectWiseManageRequestParams],
    IPaginateable[WorkflowTrigger, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "triggers", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[WorkflowTrigger])
        IPaginateable.__init__(self, WorkflowTrigger)

        self.count = self._register_child_endpoint(
            SystemWorkflowsIdTriggersCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemWorkflowsIdTriggersIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SystemWorkflowsIdTriggersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemWorkflowsIdTriggersIdEndpoint: The initialized SystemWorkflowsIdTriggersIdEndpoint object.
        """
        child = SystemWorkflowsIdTriggersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[WorkflowTrigger]:
        """
        Performs a GET request against the /system/workflows/{id}/triggers endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkflowTrigger]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            WorkflowTrigger,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[WorkflowTrigger]:
        """
        Performs a GET request against the /system/workflows/{id}/triggers endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[WorkflowTrigger]: The parsed response data.
        """
        return self._parse_many(
            WorkflowTrigger,
            super()._make_request("GET", data=data, params=params).json(),
        )
