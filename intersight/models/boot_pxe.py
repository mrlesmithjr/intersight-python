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


class BootPxe(object):
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
        'enabled': 'bool',
        'name': 'str',
        'mac_address': 'str',
        'port': 'int',
        'slot': 'str'
    }

    attribute_map = {
        'enabled': 'Enabled',
        'name': 'Name',
        'mac_address': 'MacAddress',
        'port': 'Port',
        'slot': 'Slot'
    }

    def __init__(self, enabled=None, name=None, mac_address=None, port=None, slot=None):
        """
        BootPxe - a model defined in Swagger
        """

        self._enabled = None
        self._name = None
        self._mac_address = None
        self._port = None
        self._slot = None

        if enabled is not None:
          self.enabled = enabled
        if name is not None:
          self.name = name
        if mac_address is not None:
          self.mac_address = mac_address
        if port is not None:
          self.port = port
        if slot is not None:
          self.slot = slot

    @property
    def enabled(self):
        """
        Gets the enabled of this BootPxe.
        Specifies if the boot device is enabled or disabled.  

        :return: The enabled of this BootPxe.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this BootPxe.
        Specifies if the boot device is enabled or disabled.  

        :param enabled: The enabled of this BootPxe.
        :type: bool
        """

        self._enabled = enabled

    @property
    def name(self):
        """
        Gets the name of this BootPxe.
        Specifies the name of the boot device. It should start and end with an alphanumeric character. It can have underscores and hyphens. It cannot be more than 30 characters.   

        :return: The name of this BootPxe.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BootPxe.
        Specifies the name of the boot device. It should start and end with an alphanumeric character. It can have underscores and hyphens. It cannot be more than 30 characters.   

        :param name: The name of this BootPxe.
        :type: str
        """

        self._name = name

    @property
    def mac_address(self):
        """
        Gets the mac_address of this BootPxe.
        Specifies the MAC Address  

        :return: The mac_address of this BootPxe.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """
        Sets the mac_address of this BootPxe.
        Specifies the MAC Address  

        :param mac_address: The mac_address of this BootPxe.
        :type: str
        """

        self._mac_address = mac_address

    @property
    def port(self):
        """
        Gets the port of this BootPxe.
        Specifies the port id of the device.  

        :return: The port of this BootPxe.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this BootPxe.
        Specifies the port id of the device.  

        :param port: The port of this BootPxe.
        :type: int
        """

        self._port = port

    @property
    def slot(self):
        """
        Gets the slot of this BootPxe.
        Specifies the slot id of the device. Supported values are (1 - 255, \"MLOM\", \"L\")   

        :return: The slot of this BootPxe.
        :rtype: str
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """
        Sets the slot of this BootPxe.
        Specifies the slot id of the device. Supported values are (1 - 255, \"MLOM\", \"L\")   

        :param slot: The slot of this BootPxe.
        :type: str
        """

        self._slot = slot

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
        if not isinstance(other, BootPxe):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other