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


class WorkflowCustomDataProperty(object):
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
        'custom_data_type_name': 'str'
    }

    attribute_map = {
        'custom_data_type_name': 'CustomDataTypeName'
    }

    def __init__(self, custom_data_type_name=None):
        """
        WorkflowCustomDataProperty - a model defined in Swagger
        """

        self._custom_data_type_name = None

        if custom_data_type_name is not None:
          self.custom_data_type_name = custom_data_type_name

    @property
    def custom_data_type_name(self):
        """
        Gets the custom_data_type_name of this WorkflowCustomDataProperty.
        Name of the custom data type for this input.   

        :return: The custom_data_type_name of this WorkflowCustomDataProperty.
        :rtype: str
        """
        return self._custom_data_type_name

    @custom_data_type_name.setter
    def custom_data_type_name(self, custom_data_type_name):
        """
        Sets the custom_data_type_name of this WorkflowCustomDataProperty.
        Name of the custom data type for this input.   

        :param custom_data_type_name: The custom_data_type_name of this WorkflowCustomDataProperty.
        :type: str
        """

        self._custom_data_type_name = custom_data_type_name

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
        if not isinstance(other, WorkflowCustomDataProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
