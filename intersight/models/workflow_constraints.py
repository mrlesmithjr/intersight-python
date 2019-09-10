# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.9-961
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WorkflowConstraints(object):
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
        'enum_list': 'list[WorkflowEnumEntry]',
        'max': 'float',
        'min': 'float',
        'regex': 'str'
    }

    attribute_map = {
        'enum_list': 'EnumList',
        'max': 'Max',
        'min': 'Min',
        'regex': 'Regex'
    }

    def __init__(self, enum_list=None, max=None, min=None, regex=None):
        """
        WorkflowConstraints - a model defined in Swagger
        """

        self._enum_list = None
        self._max = None
        self._min = None
        self._regex = None

        if enum_list is not None:
          self.enum_list = enum_list
        if max is not None:
          self.max = max
        if min is not None:
          self.min = min
        if regex is not None:
          self.regex = regex

    @property
    def enum_list(self):
        """
        Gets the enum_list of this WorkflowConstraints.
        When the parameter is a enum then this list of enum entry is used to validate the input belongs to one of items in the list.  

        :return: The enum_list of this WorkflowConstraints.
        :rtype: list[WorkflowEnumEntry]
        """
        return self._enum_list

    @enum_list.setter
    def enum_list(self, enum_list):
        """
        Sets the enum_list of this WorkflowConstraints.
        When the parameter is a enum then this list of enum entry is used to validate the input belongs to one of items in the list.  

        :param enum_list: The enum_list of this WorkflowConstraints.
        :type: list[WorkflowEnumEntry]
        """

        self._enum_list = enum_list

    @property
    def max(self):
        """
        Gets the max of this WorkflowConstraints.
        Allowed maximum value of the parameter if parameter is integer/float or maximum length of the parameter if the parameter is string. When max and min are set to 0, then the limits are not checked.   

        :return: The max of this WorkflowConstraints.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this WorkflowConstraints.
        Allowed maximum value of the parameter if parameter is integer/float or maximum length of the parameter if the parameter is string. When max and min are set to 0, then the limits are not checked.   

        :param max: The max of this WorkflowConstraints.
        :type: float
        """

        self._max = max

    @property
    def min(self):
        """
        Gets the min of this WorkflowConstraints.
        Allowed minimum value of the parameter if parameter is integer/float or minimum length of the parameter if the parameter is string. When max and min are set to 0, then the limits are not checked.   

        :return: The min of this WorkflowConstraints.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this WorkflowConstraints.
        Allowed minimum value of the parameter if parameter is integer/float or minimum length of the parameter if the parameter is string. When max and min are set to 0, then the limits are not checked.   

        :param min: The min of this WorkflowConstraints.
        :type: float
        """

        self._min = min

    @property
    def regex(self):
        """
        Gets the regex of this WorkflowConstraints.
        When the parameter is a string this regular expression is used to ensure the value is valid.   

        :return: The regex of this WorkflowConstraints.
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """
        Sets the regex of this WorkflowConstraints.
        When the parameter is a string this regular expression is used to ensure the value is valid.   

        :param regex: The regex of this WorkflowConstraints.
        :type: str
        """

        self._regex = regex

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
        if not isinstance(other, WorkflowConstraints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
