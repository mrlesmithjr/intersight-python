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


class StorageSasExpanderAllOf(object):
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
        'expander_id': 'int',
        'name': 'str',
        'oper_state': 'str',
        'operability': 'str',
        'presence': 'str',
        'sas_address': 'str',
        'controller': 'ManagementController',
        'equipment_chassis': 'EquipmentChassis',
        'registered_device': 'AssetDeviceRegistration'
    }

    attribute_map = {
        'expander_id': 'ExpanderId',
        'name': 'Name',
        'oper_state': 'OperState',
        'operability': 'Operability',
        'presence': 'Presence',
        'sas_address': 'SasAddress',
        'controller': 'Controller',
        'equipment_chassis': 'EquipmentChassis',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self,
                 expander_id=None,
                 name=None,
                 oper_state=None,
                 operability=None,
                 presence=None,
                 sas_address=None,
                 controller=None,
                 equipment_chassis=None,
                 registered_device=None,
                 local_vars_configuration=None):  # noqa: E501
        """StorageSasExpanderAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._expander_id = None
        self._name = None
        self._oper_state = None
        self._operability = None
        self._presence = None
        self._sas_address = None
        self._controller = None
        self._equipment_chassis = None
        self._registered_device = None
        self.discriminator = None

        if expander_id is not None:
            self.expander_id = expander_id
        if name is not None:
            self.name = name
        if oper_state is not None:
            self.oper_state = oper_state
        if operability is not None:
            self.operability = operability
        if presence is not None:
            self.presence = presence
        if sas_address is not None:
            self.sas_address = sas_address
        if controller is not None:
            self.controller = controller
        if equipment_chassis is not None:
            self.equipment_chassis = equipment_chassis
        if registered_device is not None:
            self.registered_device = registered_device

    @property
    def expander_id(self):
        """Gets the expander_id of this StorageSasExpanderAllOf.  # noqa: E501


        :return: The expander_id of this StorageSasExpanderAllOf.  # noqa: E501
        :rtype: int
        """
        return self._expander_id

    @expander_id.setter
    def expander_id(self, expander_id):
        """Sets the expander_id of this StorageSasExpanderAllOf.


        :param expander_id: The expander_id of this StorageSasExpanderAllOf.  # noqa: E501
        :type: int
        """

        self._expander_id = expander_id

    @property
    def name(self):
        """Gets the name of this StorageSasExpanderAllOf.  # noqa: E501


        :return: The name of this StorageSasExpanderAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StorageSasExpanderAllOf.


        :param name: The name of this StorageSasExpanderAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def oper_state(self):
        """Gets the oper_state of this StorageSasExpanderAllOf.  # noqa: E501


        :return: The oper_state of this StorageSasExpanderAllOf.  # noqa: E501
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """Sets the oper_state of this StorageSasExpanderAllOf.


        :param oper_state: The oper_state of this StorageSasExpanderAllOf.  # noqa: E501
        :type: str
        """

        self._oper_state = oper_state

    @property
    def operability(self):
        """Gets the operability of this StorageSasExpanderAllOf.  # noqa: E501


        :return: The operability of this StorageSasExpanderAllOf.  # noqa: E501
        :rtype: str
        """
        return self._operability

    @operability.setter
    def operability(self, operability):
        """Sets the operability of this StorageSasExpanderAllOf.


        :param operability: The operability of this StorageSasExpanderAllOf.  # noqa: E501
        :type: str
        """

        self._operability = operability

    @property
    def presence(self):
        """Gets the presence of this StorageSasExpanderAllOf.  # noqa: E501


        :return: The presence of this StorageSasExpanderAllOf.  # noqa: E501
        :rtype: str
        """
        return self._presence

    @presence.setter
    def presence(self, presence):
        """Sets the presence of this StorageSasExpanderAllOf.


        :param presence: The presence of this StorageSasExpanderAllOf.  # noqa: E501
        :type: str
        """

        self._presence = presence

    @property
    def sas_address(self):
        """Gets the sas_address of this StorageSasExpanderAllOf.  # noqa: E501


        :return: The sas_address of this StorageSasExpanderAllOf.  # noqa: E501
        :rtype: str
        """
        return self._sas_address

    @sas_address.setter
    def sas_address(self, sas_address):
        """Sets the sas_address of this StorageSasExpanderAllOf.


        :param sas_address: The sas_address of this StorageSasExpanderAllOf.  # noqa: E501
        :type: str
        """

        self._sas_address = sas_address

    @property
    def controller(self):
        """Gets the controller of this StorageSasExpanderAllOf.  # noqa: E501


        :return: The controller of this StorageSasExpanderAllOf.  # noqa: E501
        :rtype: ManagementController
        """
        return self._controller

    @controller.setter
    def controller(self, controller):
        """Sets the controller of this StorageSasExpanderAllOf.


        :param controller: The controller of this StorageSasExpanderAllOf.  # noqa: E501
        :type: ManagementController
        """

        self._controller = controller

    @property
    def equipment_chassis(self):
        """Gets the equipment_chassis of this StorageSasExpanderAllOf.  # noqa: E501


        :return: The equipment_chassis of this StorageSasExpanderAllOf.  # noqa: E501
        :rtype: EquipmentChassis
        """
        return self._equipment_chassis

    @equipment_chassis.setter
    def equipment_chassis(self, equipment_chassis):
        """Sets the equipment_chassis of this StorageSasExpanderAllOf.


        :param equipment_chassis: The equipment_chassis of this StorageSasExpanderAllOf.  # noqa: E501
        :type: EquipmentChassis
        """

        self._equipment_chassis = equipment_chassis

    @property
    def registered_device(self):
        """Gets the registered_device of this StorageSasExpanderAllOf.  # noqa: E501


        :return: The registered_device of this StorageSasExpanderAllOf.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this StorageSasExpanderAllOf.


        :param registered_device: The registered_device of this StorageSasExpanderAllOf.  # noqa: E501
        :type: AssetDeviceRegistration
        """

        self._registered_device = registered_device

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
        if not isinstance(other, StorageSasExpanderAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageSasExpanderAllOf):
            return True

        return self.to_dict() != other.to_dict()