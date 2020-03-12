# coding: utf-8

"""
    Skycoin REST API.

    Skycoin is a next-generation cryptocurrency.  # noqa: E501

    OpenAPI spec version: 0.26.0
    Contact: contact@skycoin.net
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse20010(object):
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
        'transaction': 'ApiV1PendingTxsTransaction',
        'received': 'str',
        'checked': 'str',
        'announced': 'str',
        'is_valid': 'bool'
    }

    attribute_map = {
        'transaction': 'transaction',
        'received': 'received',
        'checked': 'checked',
        'announced': 'announced',
        'is_valid': 'is_valid'
    }

    def __init__(self, transaction=None, received=None, checked=None, announced=None, is_valid=None):  # noqa: E501
        """InlineResponse20010 - a model defined in OpenAPI"""  # noqa: E501

        self._transaction = None
        self._received = None
        self._checked = None
        self._announced = None
        self._is_valid = None
        self.discriminator = None

        if transaction is not None:
            self.transaction = transaction
        if received is not None:
            self.received = received
        if checked is not None:
            self.checked = checked
        if announced is not None:
            self.announced = announced
        if is_valid is not None:
            self.is_valid = is_valid

    @property
    def transaction(self):
        """Gets the transaction of this InlineResponse20010.  # noqa: E501


        :return: The transaction of this InlineResponse20010.  # noqa: E501
        :rtype: ApiV1PendingTxsTransaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this InlineResponse20010.


        :param transaction: The transaction of this InlineResponse20010.  # noqa: E501
        :type: ApiV1PendingTxsTransaction
        """

        self._transaction = transaction

    @property
    def received(self):
        """Gets the received of this InlineResponse20010.  # noqa: E501


        :return: The received of this InlineResponse20010.  # noqa: E501
        :rtype: str
        """
        return self._received

    @received.setter
    def received(self, received):
        """Sets the received of this InlineResponse20010.


        :param received: The received of this InlineResponse20010.  # noqa: E501
        :type: str
        """

        self._received = received

    @property
    def checked(self):
        """Gets the checked of this InlineResponse20010.  # noqa: E501


        :return: The checked of this InlineResponse20010.  # noqa: E501
        :rtype: str
        """
        return self._checked

    @checked.setter
    def checked(self, checked):
        """Sets the checked of this InlineResponse20010.


        :param checked: The checked of this InlineResponse20010.  # noqa: E501
        :type: str
        """

        self._checked = checked

    @property
    def announced(self):
        """Gets the announced of this InlineResponse20010.  # noqa: E501


        :return: The announced of this InlineResponse20010.  # noqa: E501
        :rtype: str
        """
        return self._announced

    @announced.setter
    def announced(self, announced):
        """Sets the announced of this InlineResponse20010.


        :param announced: The announced of this InlineResponse20010.  # noqa: E501
        :type: str
        """

        self._announced = announced

    @property
    def is_valid(self):
        """Gets the is_valid of this InlineResponse20010.  # noqa: E501


        :return: The is_valid of this InlineResponse20010.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this InlineResponse20010.


        :param is_valid: The is_valid of this InlineResponse20010.  # noqa: E501
        :type: bool
        """

        self._is_valid = is_valid

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
        if not isinstance(other, InlineResponse20010):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
