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


class AdapterAdapterConfigAllOf(object):
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
        'eth_settings': 'AdapterEthSettings',
        'fc_settings': 'AdapterFcSettings',
        'port_channel_settings': 'AdapterPortChannelSettings',
        'slot_id': 'str'
    }

    attribute_map = {
        'eth_settings': 'EthSettings',
        'fc_settings': 'FcSettings',
        'port_channel_settings': 'PortChannelSettings',
        'slot_id': 'SlotId'
    }

    def __init__(self,
                 eth_settings=None,
                 fc_settings=None,
                 port_channel_settings=None,
                 slot_id=None,
                 local_vars_configuration=None):  # noqa: E501
        """AdapterAdapterConfigAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._eth_settings = None
        self._fc_settings = None
        self._port_channel_settings = None
        self._slot_id = None
        self.discriminator = None

        if eth_settings is not None:
            self.eth_settings = eth_settings
        if fc_settings is not None:
            self.fc_settings = fc_settings
        if port_channel_settings is not None:
            self.port_channel_settings = port_channel_settings
        if slot_id is not None:
            self.slot_id = slot_id

    @property
    def eth_settings(self):
        """Gets the eth_settings of this AdapterAdapterConfigAllOf.  # noqa: E501


        :return: The eth_settings of this AdapterAdapterConfigAllOf.  # noqa: E501
        :rtype: AdapterEthSettings
        """
        return self._eth_settings

    @eth_settings.setter
    def eth_settings(self, eth_settings):
        """Sets the eth_settings of this AdapterAdapterConfigAllOf.


        :param eth_settings: The eth_settings of this AdapterAdapterConfigAllOf.  # noqa: E501
        :type: AdapterEthSettings
        """

        self._eth_settings = eth_settings

    @property
    def fc_settings(self):
        """Gets the fc_settings of this AdapterAdapterConfigAllOf.  # noqa: E501


        :return: The fc_settings of this AdapterAdapterConfigAllOf.  # noqa: E501
        :rtype: AdapterFcSettings
        """
        return self._fc_settings

    @fc_settings.setter
    def fc_settings(self, fc_settings):
        """Sets the fc_settings of this AdapterAdapterConfigAllOf.


        :param fc_settings: The fc_settings of this AdapterAdapterConfigAllOf.  # noqa: E501
        :type: AdapterFcSettings
        """

        self._fc_settings = fc_settings

    @property
    def port_channel_settings(self):
        """Gets the port_channel_settings of this AdapterAdapterConfigAllOf.  # noqa: E501


        :return: The port_channel_settings of this AdapterAdapterConfigAllOf.  # noqa: E501
        :rtype: AdapterPortChannelSettings
        """
        return self._port_channel_settings

    @port_channel_settings.setter
    def port_channel_settings(self, port_channel_settings):
        """Sets the port_channel_settings of this AdapterAdapterConfigAllOf.


        :param port_channel_settings: The port_channel_settings of this AdapterAdapterConfigAllOf.  # noqa: E501
        :type: AdapterPortChannelSettings
        """

        self._port_channel_settings = port_channel_settings

    @property
    def slot_id(self):
        """Gets the slot_id of this AdapterAdapterConfigAllOf.  # noqa: E501

        PCIe slot where the VIC adapter is installed. Supported values are (1-15) and MLOM.     # noqa: E501

        :return: The slot_id of this AdapterAdapterConfigAllOf.  # noqa: E501
        :rtype: str
        """
        return self._slot_id

    @slot_id.setter
    def slot_id(self, slot_id):
        """Sets the slot_id of this AdapterAdapterConfigAllOf.

        PCIe slot where the VIC adapter is installed. Supported values are (1-15) and MLOM.     # noqa: E501

        :param slot_id: The slot_id of this AdapterAdapterConfigAllOf.  # noqa: E501
        :type: str
        """

        self._slot_id = slot_id

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
        if not isinstance(other, AdapterAdapterConfigAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdapterAdapterConfigAllOf):
            return True

        return self.to_dict() != other.to_dict()