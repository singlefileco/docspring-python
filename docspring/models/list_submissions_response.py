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


class ListSubmissionsResponse(object):
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
        'next_cursor': 'str',
        'submissions': 'list[Submission]',
        'limit': 'float'
    }

    attribute_map = {
        'next_cursor': 'next_cursor',
        'submissions': 'submissions',
        'limit': 'limit'
    }

    def __init__(self, next_cursor=None, submissions=None, limit=None):  # noqa: E501
        """ListSubmissionsResponse - a model defined in OpenAPI"""  # noqa: E501

        self._next_cursor = None
        self._submissions = None
        self._limit = None
        self.discriminator = None

        self.next_cursor = next_cursor
        if submissions is not None:
            self.submissions = submissions
        if limit is not None:
            self.limit = limit

    @property
    def next_cursor(self):
        """Gets the next_cursor of this ListSubmissionsResponse.  # noqa: E501


        :return: The next_cursor of this ListSubmissionsResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_cursor

    @next_cursor.setter
    def next_cursor(self, next_cursor):
        """Sets the next_cursor of this ListSubmissionsResponse.


        :param next_cursor: The next_cursor of this ListSubmissionsResponse.  # noqa: E501
        :type: str
        """

        self._next_cursor = next_cursor

    @property
    def submissions(self):
        """Gets the submissions of this ListSubmissionsResponse.  # noqa: E501


        :return: The submissions of this ListSubmissionsResponse.  # noqa: E501
        :rtype: list[Submission]
        """
        return self._submissions

    @submissions.setter
    def submissions(self, submissions):
        """Sets the submissions of this ListSubmissionsResponse.


        :param submissions: The submissions of this ListSubmissionsResponse.  # noqa: E501
        :type: list[Submission]
        """

        self._submissions = submissions

    @property
    def limit(self):
        """Gets the limit of this ListSubmissionsResponse.  # noqa: E501


        :return: The limit of this ListSubmissionsResponse.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSubmissionsResponse.


        :param limit: The limit of this ListSubmissionsResponse.  # noqa: E501
        :type: float
        """

        self._limit = limit

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
        if not isinstance(other, ListSubmissionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other