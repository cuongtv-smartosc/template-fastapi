from fastapi import status


class ErrorMessages:
    default = "Unhandled Error"
    bad_request = "Bad request"
    un_authorized = "Unauthorized"
    wrong = "Something went wrong"
    not_found = "Not found"
    method_not_allow = "Method not allowed"
    bad_request = "Bad request"


class APIException(Exception):
    def __init__(
        self,
        success=False,
        data=None,
        http_status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        message=ErrorMessages.default,
        extra=None,
    ):
        self.success = success
        self.data = data
        self.http_status = http_status
        self.message = message
        self.extra = extra
        super().__init__()


class NotFoundException(APIException):
    def __init__(self, message=ErrorMessages.not_found, extra=None):
        super().__init__(
            http_status=status.HTTP_404_NOT_FOUND, message=message, extra=extra
        )

    def __str__(self):
        return "Not Found errors"


class BadRequestException(APIException):
    http_status = status.HTTP_400_BAD_REQUEST

    def __init__(self, message=ErrorMessages.bad_request, extra=None):
        super().__init__(
            http_status=status.HTTP_400_BAD_REQUEST, message=message, extra=extra
        )

    def __str__(self):
        return "Bad Request Errors"


class MethodNotAllowed(APIException):
    def __int__(self, message=ErrorMessages.method_not_allow, extra=None):
        super().__init__(
            http_status=status.HTTP_405_METHOD_NOT_ALLOWED, message=message, extra=extra
        )

    def __str__(self):
        return "Method not allowed"
