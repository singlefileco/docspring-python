# coding: utf-8

"""
    API v1

    DocSpring is a service that helps you fill out and sign PDF templates.  # noqa: E501

    OpenAPI spec version: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CreateSubmissionBatchSubmissionsResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'submission': 'Submission',
        'errors': 'list[str]',
        'status': 'str'
    }

    attribute_map = {
        'submission': 'submission',
        'errors': 'errors',
        'status': 'status'
    }

    def __init__(self, submission=None, errors=None, status=None):  # noqa: E501
        """CreateSubmissionBatchSubmissionsResponse - a model defined in OpenAPI"""  # noqa: E501

        self._submission = None
        self._errors = None
        self._status = None
        self.discriminator = None

        if submission is not None:
            self.submission = submission
        if errors is not None:
            self.errors = errors
        if status is not None:
            self.status = status

    @property
    def submission(self):
        """Gets the submission of this CreateSubmissionBatchSubmissionsResponse.  # noqa: E501


        :return: The submission of this CreateSubmissionBatchSubmissionsResponse.  # noqa: E501
        :rtype: Submission
        """
        return self._submission

    @submission.setter
    def submission(self, submission):
        """Sets the submission of this CreateSubmissionBatchSubmissionsResponse.


        :param submission: The submission of this CreateSubmissionBatchSubmissionsResponse.  # noqa: E501
        :type: Submission
        """

        self._submission = submission

    @property
    def errors(self):
        """Gets the errors of this CreateSubmissionBatchSubmissionsResponse.  # noqa: E501


        :return: The errors of this CreateSubmissionBatchSubmissionsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this CreateSubmissionBatchSubmissionsResponse.


        :param errors: The errors of this CreateSubmissionBatchSubmissionsResponse.  # noqa: E501
        :type: list[str]
        """

        self._errors = errors

    @property
    def status(self):
        """Gets the status of this CreateSubmissionBatchSubmissionsResponse.  # noqa: E501


        :return: The status of this CreateSubmissionBatchSubmissionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateSubmissionBatchSubmissionsResponse.


        :param status: The status of this CreateSubmissionBatchSubmissionsResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["success", "error", "valid_but_not_saved"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateSubmissionBatchSubmissionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other