# coding: utf-8
"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations.   # noqa: E501

    The version of the OpenAPI document: 1.0.9-1295
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from intersight.configuration import Configuration


class MoVersionContextAllOf(object):
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
        'interested_mos': 'list[MoMoRef]',
        'ref_mo': 'MoMoRef',
        'timestamp': 'datetime',
        'version': 'str',
        'version_type': 'str'
    }

    attribute_map = {
        'interested_mos': 'InterestedMos',
        'ref_mo': 'RefMo',
        'timestamp': 'Timestamp',
        'version': 'Version',
        'version_type': 'VersionType'
    }

    def __init__(self,
                 interested_mos=None,
                 ref_mo=None,
                 timestamp=None,
                 version=None,
                 version_type='Modified',
                 local_vars_configuration=None):  # noqa: E501
        """MoVersionContextAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._interested_mos = None
        self._ref_mo = None
        self._timestamp = None
        self._version = None
        self._version_type = None
        self.discriminator = None

        if interested_mos is not None:
            self.interested_mos = interested_mos
        if ref_mo is not None:
            self.ref_mo = ref_mo
        if timestamp is not None:
            self.timestamp = timestamp
        if version is not None:
            self.version = version
        if version_type is not None:
            self.version_type = version_type

    @property
    def interested_mos(self):
        """Gets the interested_mos of this MoVersionContextAllOf.  # noqa: E501


        :return: The interested_mos of this MoVersionContextAllOf.  # noqa: E501
        :rtype: list[MoMoRef]
        """
        return self._interested_mos

    @interested_mos.setter
    def interested_mos(self, interested_mos):
        """Sets the interested_mos of this MoVersionContextAllOf.


        :param interested_mos: The interested_mos of this MoVersionContextAllOf.  # noqa: E501
        :type: list[MoMoRef]
        """

        self._interested_mos = interested_mos

    @property
    def ref_mo(self):
        """Gets the ref_mo of this MoVersionContextAllOf.  # noqa: E501


        :return: The ref_mo of this MoVersionContextAllOf.  # noqa: E501
        :rtype: MoMoRef
        """
        return self._ref_mo

    @ref_mo.setter
    def ref_mo(self, ref_mo):
        """Sets the ref_mo of this MoVersionContextAllOf.


        :param ref_mo: The ref_mo of this MoVersionContextAllOf.  # noqa: E501
        :type: MoMoRef
        """

        self._ref_mo = ref_mo

    @property
    def timestamp(self):
        """Gets the timestamp of this MoVersionContextAllOf.  # noqa: E501

        The time this versioned Managed Object was created.    # noqa: E501

        :return: The timestamp of this MoVersionContextAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this MoVersionContextAllOf.

        The time this versioned Managed Object was created.    # noqa: E501

        :param timestamp: The timestamp of this MoVersionContextAllOf.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def version(self):
        """Gets the version of this MoVersionContextAllOf.  # noqa: E501

        The version of the Managed Object, e.g. an incrementing number or a hash id.    # noqa: E501

        :return: The version of this MoVersionContextAllOf.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this MoVersionContextAllOf.

        The version of the Managed Object, e.g. an incrementing number or a hash id.    # noqa: E501

        :param version: The version of this MoVersionContextAllOf.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def version_type(self):
        """Gets the version_type of this MoVersionContextAllOf.  # noqa: E501

        Specifies type of version. Currently the only supported value is \"Configured\" that is used to keep track of snapshots of policies and profiles that are intended to be configured to target endpoints.      # noqa: E501

        :return: The version_type of this MoVersionContextAllOf.  # noqa: E501
        :rtype: str
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        """Sets the version_type of this MoVersionContextAllOf.

        Specifies type of version. Currently the only supported value is \"Configured\" that is used to keep track of snapshots of policies and profiles that are intended to be configured to target endpoints.      # noqa: E501

        :param version_type: The version_type of this MoVersionContextAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["Modified", "Configured", "Deployed"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and version_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `version_type` ({0}), must be one of {1}"  # noqa: E501
                .format(version_type, allowed_values))

        self._version_type = version_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()))
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
        if not isinstance(other, MoVersionContextAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MoVersionContextAllOf):
            return True

        return self.to_dict() != other.to_dict()