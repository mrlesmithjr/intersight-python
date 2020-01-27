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


class MemoryPersistentMemoryConfiguration(object):
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
        'memory_capacity': 'str',
        'num_of_dimms': 'str',
        'num_of_regions': 'str',
        'persistent_memory_capacity': 'str',
        'reserved_capacity': 'str',
        'security_state': 'str',
        'total_capacity': 'str',
        'compute_board': 'ComputeBoard',
        'persistent_memory_config_result':
        'MemoryPersistentMemoryConfigResult',
        'persistent_memory_regions': 'list[MemoryPersistentMemoryRegion]',
        'registered_device': 'AssetDeviceRegistration'
    }

    attribute_map = {
        'memory_capacity': 'MemoryCapacity',
        'num_of_dimms': 'NumOfDimms',
        'num_of_regions': 'NumOfRegions',
        'persistent_memory_capacity': 'PersistentMemoryCapacity',
        'reserved_capacity': 'ReservedCapacity',
        'security_state': 'SecurityState',
        'total_capacity': 'TotalCapacity',
        'compute_board': 'ComputeBoard',
        'persistent_memory_config_result': 'PersistentMemoryConfigResult',
        'persistent_memory_regions': 'PersistentMemoryRegions',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self,
                 memory_capacity=None,
                 num_of_dimms=None,
                 num_of_regions=None,
                 persistent_memory_capacity=None,
                 reserved_capacity=None,
                 security_state=None,
                 total_capacity=None,
                 compute_board=None,
                 persistent_memory_config_result=None,
                 persistent_memory_regions=None,
                 registered_device=None,
                 local_vars_configuration=None):  # noqa: E501
        """MemoryPersistentMemoryConfiguration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._memory_capacity = None
        self._num_of_dimms = None
        self._num_of_regions = None
        self._persistent_memory_capacity = None
        self._reserved_capacity = None
        self._security_state = None
        self._total_capacity = None
        self._compute_board = None
        self._persistent_memory_config_result = None
        self._persistent_memory_regions = None
        self._registered_device = None
        self.discriminator = None

        if memory_capacity is not None:
            self.memory_capacity = memory_capacity
        if num_of_dimms is not None:
            self.num_of_dimms = num_of_dimms
        if num_of_regions is not None:
            self.num_of_regions = num_of_regions
        if persistent_memory_capacity is not None:
            self.persistent_memory_capacity = persistent_memory_capacity
        if reserved_capacity is not None:
            self.reserved_capacity = reserved_capacity
        if security_state is not None:
            self.security_state = security_state
        if total_capacity is not None:
            self.total_capacity = total_capacity
        if compute_board is not None:
            self.compute_board = compute_board
        if persistent_memory_config_result is not None:
            self.persistent_memory_config_result = persistent_memory_config_result
        if persistent_memory_regions is not None:
            self.persistent_memory_regions = persistent_memory_regions
        if registered_device is not None:
            self.registered_device = registered_device

    @property
    def memory_capacity(self):
        """Gets the memory_capacity of this MemoryPersistentMemoryConfiguration.  # noqa: E501

        This represents the memory capacity in GB of a persistent memory configuration on a server.    # noqa: E501

        :return: The memory_capacity of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._memory_capacity

    @memory_capacity.setter
    def memory_capacity(self, memory_capacity):
        """Sets the memory_capacity of this MemoryPersistentMemoryConfiguration.

        This represents the memory capacity in GB of a persistent memory configuration on a server.    # noqa: E501

        :param memory_capacity: The memory_capacity of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :type: str
        """

        self._memory_capacity = memory_capacity

    @property
    def num_of_dimms(self):
        """Gets the num_of_dimms of this MemoryPersistentMemoryConfiguration.  # noqa: E501

        This represents the number of persistent memory modules of a Persistent Memory Configuration on a server.    # noqa: E501

        :return: The num_of_dimms of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._num_of_dimms

    @num_of_dimms.setter
    def num_of_dimms(self, num_of_dimms):
        """Sets the num_of_dimms of this MemoryPersistentMemoryConfiguration.

        This represents the number of persistent memory modules of a Persistent Memory Configuration on a server.    # noqa: E501

        :param num_of_dimms: The num_of_dimms of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :type: str
        """

        self._num_of_dimms = num_of_dimms

    @property
    def num_of_regions(self):
        """Gets the num_of_regions of this MemoryPersistentMemoryConfiguration.  # noqa: E501

        This represents the number of regions of a Persistent Memory Configuration on a server.    # noqa: E501

        :return: The num_of_regions of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._num_of_regions

    @num_of_regions.setter
    def num_of_regions(self, num_of_regions):
        """Sets the num_of_regions of this MemoryPersistentMemoryConfiguration.

        This represents the number of regions of a Persistent Memory Configuration on a server.    # noqa: E501

        :param num_of_regions: The num_of_regions of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :type: str
        """

        self._num_of_regions = num_of_regions

    @property
    def persistent_memory_capacity(self):
        """Gets the persistent_memory_capacity of this MemoryPersistentMemoryConfiguration.  # noqa: E501

        This represents the persistent memory capacity in GB of a persistent memory configuration on a server.    # noqa: E501

        :return: The persistent_memory_capacity of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._persistent_memory_capacity

    @persistent_memory_capacity.setter
    def persistent_memory_capacity(self, persistent_memory_capacity):
        """Sets the persistent_memory_capacity of this MemoryPersistentMemoryConfiguration.

        This represents the persistent memory capacity in GB of a persistent memory configuration on a server.    # noqa: E501

        :param persistent_memory_capacity: The persistent_memory_capacity of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :type: str
        """

        self._persistent_memory_capacity = persistent_memory_capacity

    @property
    def reserved_capacity(self):
        """Gets the reserved_capacity of this MemoryPersistentMemoryConfiguration.  # noqa: E501

        This represents the reserved capacity in GB of a persistent memory configuration on a server.    # noqa: E501

        :return: The reserved_capacity of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._reserved_capacity

    @reserved_capacity.setter
    def reserved_capacity(self, reserved_capacity):
        """Sets the reserved_capacity of this MemoryPersistentMemoryConfiguration.

        This represents the reserved capacity in GB of a persistent memory configuration on a server.    # noqa: E501

        :param reserved_capacity: The reserved_capacity of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :type: str
        """

        self._reserved_capacity = reserved_capacity

    @property
    def security_state(self):
        """Gets the security_state of this MemoryPersistentMemoryConfiguration.  # noqa: E501

        This represents the collective security state of all persistent memory modules on a server.    # noqa: E501

        :return: The security_state of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._security_state

    @security_state.setter
    def security_state(self, security_state):
        """Sets the security_state of this MemoryPersistentMemoryConfiguration.

        This represents the collective security state of all persistent memory modules on a server.    # noqa: E501

        :param security_state: The security_state of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :type: str
        """

        self._security_state = security_state

    @property
    def total_capacity(self):
        """Gets the total_capacity of this MemoryPersistentMemoryConfiguration.  # noqa: E501

        This represents the total capacity in GB of a persistent memory configuration on a server.     # noqa: E501

        :return: The total_capacity of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._total_capacity

    @total_capacity.setter
    def total_capacity(self, total_capacity):
        """Sets the total_capacity of this MemoryPersistentMemoryConfiguration.

        This represents the total capacity in GB of a persistent memory configuration on a server.     # noqa: E501

        :param total_capacity: The total_capacity of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :type: str
        """

        self._total_capacity = total_capacity

    @property
    def compute_board(self):
        """Gets the compute_board of this MemoryPersistentMemoryConfiguration.  # noqa: E501


        :return: The compute_board of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :rtype: ComputeBoard
        """
        return self._compute_board

    @compute_board.setter
    def compute_board(self, compute_board):
        """Sets the compute_board of this MemoryPersistentMemoryConfiguration.


        :param compute_board: The compute_board of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :type: ComputeBoard
        """

        self._compute_board = compute_board

    @property
    def persistent_memory_config_result(self):
        """Gets the persistent_memory_config_result of this MemoryPersistentMemoryConfiguration.  # noqa: E501


        :return: The persistent_memory_config_result of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :rtype: MemoryPersistentMemoryConfigResult
        """
        return self._persistent_memory_config_result

    @persistent_memory_config_result.setter
    def persistent_memory_config_result(self, persistent_memory_config_result):
        """Sets the persistent_memory_config_result of this MemoryPersistentMemoryConfiguration.


        :param persistent_memory_config_result: The persistent_memory_config_result of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :type: MemoryPersistentMemoryConfigResult
        """

        self._persistent_memory_config_result = persistent_memory_config_result

    @property
    def persistent_memory_regions(self):
        """Gets the persistent_memory_regions of this MemoryPersistentMemoryConfiguration.  # noqa: E501

        A reference to a memoryPersistentMemoryRegion resource. When the $expand query parameter is specified, the referenced resource is returned inline. This represents the collection of all the persistent memory regions configured on a server.   # noqa: E501

        :return: The persistent_memory_regions of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :rtype: list[MemoryPersistentMemoryRegion]
        """
        return self._persistent_memory_regions

    @persistent_memory_regions.setter
    def persistent_memory_regions(self, persistent_memory_regions):
        """Sets the persistent_memory_regions of this MemoryPersistentMemoryConfiguration.

        A reference to a memoryPersistentMemoryRegion resource. When the $expand query parameter is specified, the referenced resource is returned inline. This represents the collection of all the persistent memory regions configured on a server.   # noqa: E501

        :param persistent_memory_regions: The persistent_memory_regions of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :type: list[MemoryPersistentMemoryRegion]
        """

        self._persistent_memory_regions = persistent_memory_regions

    @property
    def registered_device(self):
        """Gets the registered_device of this MemoryPersistentMemoryConfiguration.  # noqa: E501


        :return: The registered_device of this MemoryPersistentMemoryConfiguration.  # noqa: E501
        :rtype: AssetDeviceRegistration
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """Sets the registered_device of this MemoryPersistentMemoryConfiguration.


        :param registered_device: The registered_device of this MemoryPersistentMemoryConfiguration.  # noqa: E501
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
        if not isinstance(other, MemoryPersistentMemoryConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MemoryPersistentMemoryConfiguration):
            return True

        return self.to_dict() != other.to_dict()