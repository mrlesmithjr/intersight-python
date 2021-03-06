# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1461
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IaasLicenseUtilizationInfo(object):
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
        'object_type': 'str',
        'actual_used': 'int',
        'label': 'str',
        'licensed_limit': 'str',
        'sku': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'actual_used': 'ActualUsed',
        'label': 'Label',
        'licensed_limit': 'LicensedLimit',
        'sku': 'Sku'
    }

    def __init__(self, object_type=None, actual_used=None, label=None, licensed_limit=None, sku=None):
        """
        IaasLicenseUtilizationInfo - a model defined in Swagger
        """

        self._object_type = None
        self._actual_used = None
        self._label = None
        self._licensed_limit = None
        self._sku = None

        if object_type is not None:
          self.object_type = object_type
        if actual_used is not None:
          self.actual_used = actual_used
        if label is not None:
          self.label = label
        if licensed_limit is not None:
          self.licensed_limit = licensed_limit
        if sku is not None:
          self.sku = sku

    @property
    def object_type(self):
        """
        Gets the object_type of this IaasLicenseUtilizationInfo.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :return: The object_type of this IaasLicenseUtilizationInfo.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this IaasLicenseUtilizationInfo.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :param object_type: The object_type of this IaasLicenseUtilizationInfo.
        :type: str
        """

        self._object_type = object_type

    @property
    def actual_used(self):
        """
        Gets the actual_used of this IaasLicenseUtilizationInfo.
        Number of licenses actually used for this feature.

        :return: The actual_used of this IaasLicenseUtilizationInfo.
        :rtype: int
        """
        return self._actual_used

    @actual_used.setter
    def actual_used(self, actual_used):
        """
        Sets the actual_used of this IaasLicenseUtilizationInfo.
        Number of licenses actually used for this feature.

        :param actual_used: The actual_used of this IaasLicenseUtilizationInfo.
        :type: int
        """

        self._actual_used = actual_used

    @property
    def label(self):
        """
        Gets the label of this IaasLicenseUtilizationInfo.
        License Label.

        :return: The label of this IaasLicenseUtilizationInfo.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this IaasLicenseUtilizationInfo.
        License Label.

        :param label: The label of this IaasLicenseUtilizationInfo.
        :type: str
        """

        self._label = label

    @property
    def licensed_limit(self):
        """
        Gets the licensed_limit of this IaasLicenseUtilizationInfo.
        License limit for this license feature.

        :return: The licensed_limit of this IaasLicenseUtilizationInfo.
        :rtype: str
        """
        return self._licensed_limit

    @licensed_limit.setter
    def licensed_limit(self, licensed_limit):
        """
        Sets the licensed_limit of this IaasLicenseUtilizationInfo.
        License limit for this license feature.

        :param licensed_limit: The licensed_limit of this IaasLicenseUtilizationInfo.
        :type: str
        """

        self._licensed_limit = licensed_limit

    @property
    def sku(self):
        """
        Gets the sku of this IaasLicenseUtilizationInfo.
        SKU for the license.

        :return: The sku of this IaasLicenseUtilizationInfo.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this IaasLicenseUtilizationInfo.
        SKU for the license.

        :param sku: The sku of this IaasLicenseUtilizationInfo.
        :type: str
        """

        self._sku = sku

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
        if not isinstance(other, IaasLicenseUtilizationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
