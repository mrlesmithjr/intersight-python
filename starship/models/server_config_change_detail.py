# coding: utf-8

"""
    UCS Starship API

    This is the UCS Starship REST API

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ServerConfigChangeDetail(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'config_change_context': 'PolicyConfigResultContext',
        'config_change_type': 'str',
        'disruption_type': 'str',
        'message': 'str',
        'message_params': 'object'
    }

    attribute_map = {
        'config_change_context': 'ConfigChangeContext',
        'config_change_type': 'ConfigChangeType',
        'disruption_type': 'DisruptionType',
        'message': 'Message',
        'message_params': 'MessageParams'
    }

    def __init__(self, config_change_context=None, config_change_type=None, disruption_type=None, message=None, message_params=None):
        """
        ServerConfigChangeDetail - a model defined in Swagger
        """

        self._config_change_context = None
        self._config_change_type = None
        self._disruption_type = None
        self._message = None
        self._message_params = None

        if config_change_context is not None:
          self.config_change_context = config_change_context
        if config_change_type is not None:
          self.config_change_type = config_change_type
        if disruption_type is not None:
          self.disruption_type = disruption_type
        if message is not None:
          self.message = message
        if message_params is not None:
          self.message_params = message_params

    @property
    def config_change_context(self):
        """
        Gets the config_change_context of this ServerConfigChangeDetail.

        :return: The config_change_context of this ServerConfigChangeDetail.
        :rtype: PolicyConfigResultContext
        """
        return self._config_change_context

    @config_change_context.setter
    def config_change_context(self, config_change_context):
        """
        Sets the config_change_context of this ServerConfigChangeDetail.

        :param config_change_context: The config_change_context of this ServerConfigChangeDetail.
        :type: PolicyConfigResultContext
        """

        self._config_change_context = config_change_context

    @property
    def config_change_type(self):
        """
        Gets the config_change_type of this ServerConfigChangeDetail.

        :return: The config_change_type of this ServerConfigChangeDetail.
        :rtype: str
        """
        return self._config_change_type

    @config_change_type.setter
    def config_change_type(self, config_change_type):
        """
        Sets the config_change_type of this ServerConfigChangeDetail.

        :param config_change_type: The config_change_type of this ServerConfigChangeDetail.
        :type: str
        """

        self._config_change_type = config_change_type

    @property
    def disruption_type(self):
        """
        Gets the disruption_type of this ServerConfigChangeDetail.

        :return: The disruption_type of this ServerConfigChangeDetail.
        :rtype: str
        """
        return self._disruption_type

    @disruption_type.setter
    def disruption_type(self, disruption_type):
        """
        Sets the disruption_type of this ServerConfigChangeDetail.

        :param disruption_type: The disruption_type of this ServerConfigChangeDetail.
        :type: str
        """

        self._disruption_type = disruption_type

    @property
    def message(self):
        """
        Gets the message of this ServerConfigChangeDetail.

        :return: The message of this ServerConfigChangeDetail.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ServerConfigChangeDetail.

        :param message: The message of this ServerConfigChangeDetail.
        :type: str
        """

        self._message = message

    @property
    def message_params(self):
        """
        Gets the message_params of this ServerConfigChangeDetail.

        :return: The message_params of this ServerConfigChangeDetail.
        :rtype: object
        """
        return self._message_params

    @message_params.setter
    def message_params(self, message_params):
        """
        Sets the message_params of this ServerConfigChangeDetail.

        :param message_params: The message_params of this ServerConfigChangeDetail.
        :type: object
        """

        self._message_params = message_params

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ServerConfigChangeDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other