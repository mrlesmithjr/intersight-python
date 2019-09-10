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
        'actual_used': 'int',
        'label': 'str',
        'licensed_limit': 'str',
        'sku': 'str'
    }

    attribute_map = {
        'actual_used': 'ActualUsed',
        'label': 'Label',
        'licensed_limit': 'LicensedLimit',
        'sku': 'Sku'
    }

    def __init__(self, actual_used=None, label=None, licensed_limit=None, sku=None):
        """
        IaasLicenseUtilizationInfo - a model defined in Swagger
        """

        self._actual_used = None
        self._label = None
        self._licensed_limit = None
        self._sku = None

        if actual_used is not None:
          self.actual_used = actual_used
        if label is not None:
          self.label = label
        if licensed_limit is not None:
          self.licensed_limit = licensed_limit
        if sku is not None:
          self.sku = sku

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
