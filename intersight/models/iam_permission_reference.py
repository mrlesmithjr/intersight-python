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


class IamPermissionReference(object):
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
        'permission_identifier': 'str',
        'permission_name': 'str'
    }

    attribute_map = {
        'permission_identifier': 'PermissionIdentifier',
        'permission_name': 'PermissionName'
    }

    def __init__(self, permission_identifier=None, permission_name=None):
        """
        IamPermissionReference - a model defined in Swagger
        """

        self._permission_identifier = None
        self._permission_name = None

        if permission_identifier is not None:
          self.permission_identifier = permission_identifier
        if permission_name is not None:
          self.permission_name = permission_name

    @property
    def permission_identifier(self):
        """
        Gets the permission_identifier of this IamPermissionReference.
        MOID of the permission which user has access to.  

        :return: The permission_identifier of this IamPermissionReference.
        :rtype: str
        """
        return self._permission_identifier

    @permission_identifier.setter
    def permission_identifier(self, permission_identifier):
        """
        Sets the permission_identifier of this IamPermissionReference.
        MOID of the permission which user has access to.  

        :param permission_identifier: The permission_identifier of this IamPermissionReference.
        :type: str
        """

        self._permission_identifier = permission_identifier

    @property
    def permission_name(self):
        """
        Gets the permission_name of this IamPermissionReference.
        Name of the permission which user has access to.   

        :return: The permission_name of this IamPermissionReference.
        :rtype: str
        """
        return self._permission_name

    @permission_name.setter
    def permission_name(self, permission_name):
        """
        Sets the permission_name of this IamPermissionReference.
        Name of the permission which user has access to.   

        :param permission_name: The permission_name of this IamPermissionReference.
        :type: str
        """

        self._permission_name = permission_name

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
        if not isinstance(other, IamPermissionReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
