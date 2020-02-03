# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1295
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VnicRoceSettings(object):
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
        'enabled': 'bool',
        'memory_regions': 'int',
        'queue_pairs': 'int',
        'resource_groups': 'int'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'enabled': 'Enabled',
        'memory_regions': 'MemoryRegions',
        'queue_pairs': 'QueuePairs',
        'resource_groups': 'ResourceGroups'
    }

    def __init__(self, object_type=None, enabled=None, memory_regions=None, queue_pairs=None, resource_groups=None):
        """
        VnicRoceSettings - a model defined in Swagger
        """

        self._object_type = None
        self._enabled = None
        self._memory_regions = None
        self._queue_pairs = None
        self._resource_groups = None

        if object_type is not None:
          self.object_type = object_type
        if enabled is not None:
          self.enabled = enabled
        if memory_regions is not None:
          self.memory_regions = memory_regions
        if queue_pairs is not None:
          self.queue_pairs = queue_pairs
        if resource_groups is not None:
          self.resource_groups = resource_groups

    @property
    def object_type(self):
        """
        Gets the object_type of this VnicRoceSettings.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this VnicRoceSettings.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this VnicRoceSettings.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this VnicRoceSettings.
        :type: str
        """

        self._object_type = object_type

    @property
    def enabled(self):
        """
        Gets the enabled of this VnicRoceSettings.
        If enabled sets RDMA over Converged Ethernet (RoCE) on this virtual interface.  

        :return: The enabled of this VnicRoceSettings.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this VnicRoceSettings.
        If enabled sets RDMA over Converged Ethernet (RoCE) on this virtual interface.  

        :param enabled: The enabled of this VnicRoceSettings.
        :type: bool
        """

        self._enabled = enabled

    @property
    def memory_regions(self):
        """
        Gets the memory_regions of this VnicRoceSettings.
        The number of memory regions per adapter. Recommended value = integer power of 2.  

        :return: The memory_regions of this VnicRoceSettings.
        :rtype: int
        """
        return self._memory_regions

    @memory_regions.setter
    def memory_regions(self, memory_regions):
        """
        Sets the memory_regions of this VnicRoceSettings.
        The number of memory regions per adapter. Recommended value = integer power of 2.  

        :param memory_regions: The memory_regions of this VnicRoceSettings.
        :type: int
        """

        self._memory_regions = memory_regions

    @property
    def queue_pairs(self):
        """
        Gets the queue_pairs of this VnicRoceSettings.
        The number of queue pairs per adapter. Recommended value = integer power of 2.  

        :return: The queue_pairs of this VnicRoceSettings.
        :rtype: int
        """
        return self._queue_pairs

    @queue_pairs.setter
    def queue_pairs(self, queue_pairs):
        """
        Sets the queue_pairs of this VnicRoceSettings.
        The number of queue pairs per adapter. Recommended value = integer power of 2.  

        :param queue_pairs: The queue_pairs of this VnicRoceSettings.
        :type: int
        """

        self._queue_pairs = queue_pairs

    @property
    def resource_groups(self):
        """
        Gets the resource_groups of this VnicRoceSettings.
        The number of resource groups per adapter. Recommended value = be an integer power of 2 greater than or equal to the number of CPU cores on the system for optimum performance.    

        :return: The resource_groups of this VnicRoceSettings.
        :rtype: int
        """
        return self._resource_groups

    @resource_groups.setter
    def resource_groups(self, resource_groups):
        """
        Sets the resource_groups of this VnicRoceSettings.
        The number of resource groups per adapter. Recommended value = be an integer power of 2 greater than or equal to the number of CPU cores on the system for optimum performance.    

        :param resource_groups: The resource_groups of this VnicRoceSettings.
        :type: int
        """

        self._resource_groups = resource_groups

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
        if not isinstance(other, VnicRoceSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
