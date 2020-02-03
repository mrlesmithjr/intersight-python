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


class TopSystem(object):
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
        'account_moid': 'str',
        'create_time': 'datetime',
        'domain_group_moid': 'str',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'shared_scope': 'str',
        'tags': 'list[MoTag]',
        'version_context': 'MoVersionContext',
        'ancestors': 'list[MoBaseMoRef]',
        'parent': 'MoBaseMoRef',
        'permission_resources': 'list[MoBaseMoRef]',
        'device_mo_id': 'str',
        'dn': 'str',
        'rn': 'str',
        'ipv4_address': 'str',
        'ipv6_address': 'str',
        'mode': 'str',
        'name': 'str',
        'time_zone': 'str',
        'compute_blades': 'list[ComputeBladeRef]',
        'compute_rack_units': 'list[ComputeRackUnitRef]',
        'management_controller': 'ManagementControllerRef',
        'network_elements': 'list[NetworkElementRef]',
        'registered_device': 'AssetDeviceRegistrationRef'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'create_time': 'CreateTime',
        'domain_group_moid': 'DomainGroupMoid',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'shared_scope': 'SharedScope',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'ancestors': 'Ancestors',
        'parent': 'Parent',
        'permission_resources': 'PermissionResources',
        'device_mo_id': 'DeviceMoId',
        'dn': 'Dn',
        'rn': 'Rn',
        'ipv4_address': 'Ipv4Address',
        'ipv6_address': 'Ipv6Address',
        'mode': 'Mode',
        'name': 'Name',
        'time_zone': 'TimeZone',
        'compute_blades': 'ComputeBlades',
        'compute_rack_units': 'ComputeRackUnits',
        'management_controller': 'ManagementController',
        'network_elements': 'NetworkElements',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, device_mo_id=None, dn=None, rn=None, ipv4_address=None, ipv6_address=None, mode=None, name=None, time_zone=None, compute_blades=None, compute_rack_units=None, management_controller=None, network_elements=None, registered_device=None):
        """
        TopSystem - a model defined in Swagger
        """

        self._account_moid = None
        self._create_time = None
        self._domain_group_moid = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._shared_scope = None
        self._tags = None
        self._version_context = None
        self._ancestors = None
        self._parent = None
        self._permission_resources = None
        self._device_mo_id = None
        self._dn = None
        self._rn = None
        self._ipv4_address = None
        self._ipv6_address = None
        self._mode = None
        self._name = None
        self._time_zone = None
        self._compute_blades = None
        self._compute_rack_units = None
        self._management_controller = None
        self._network_elements = None
        self._registered_device = None

        if account_moid is not None:
          self.account_moid = account_moid
        if create_time is not None:
          self.create_time = create_time
        if domain_group_moid is not None:
          self.domain_group_moid = domain_group_moid
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if shared_scope is not None:
          self.shared_scope = shared_scope
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if ancestors is not None:
          self.ancestors = ancestors
        if parent is not None:
          self.parent = parent
        if permission_resources is not None:
          self.permission_resources = permission_resources
        if device_mo_id is not None:
          self.device_mo_id = device_mo_id
        if dn is not None:
          self.dn = dn
        if rn is not None:
          self.rn = rn
        if ipv4_address is not None:
          self.ipv4_address = ipv4_address
        if ipv6_address is not None:
          self.ipv6_address = ipv6_address
        if mode is not None:
          self.mode = mode
        if name is not None:
          self.name = name
        if time_zone is not None:
          self.time_zone = time_zone
        if compute_blades is not None:
          self.compute_blades = compute_blades
        if compute_rack_units is not None:
          self.compute_rack_units = compute_rack_units
        if management_controller is not None:
          self.management_controller = management_controller
        if network_elements is not None:
          self.network_elements = network_elements
        if registered_device is not None:
          self.registered_device = registered_device

    @property
    def account_moid(self):
        """
        Gets the account_moid of this TopSystem.
        The Account ID for this managed object.  

        :return: The account_moid of this TopSystem.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this TopSystem.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this TopSystem.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this TopSystem.
        The time when this managed object was created.  

        :return: The create_time of this TopSystem.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this TopSystem.
        The time when this managed object was created.  

        :param create_time: The create_time of this TopSystem.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this TopSystem.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this TopSystem.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this TopSystem.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this TopSystem.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this TopSystem.
        The time when this managed object was last modified.  

        :return: The mod_time of this TopSystem.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this TopSystem.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this TopSystem.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this TopSystem.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this TopSystem.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this TopSystem.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this TopSystem.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this TopSystem.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this TopSystem.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this TopSystem.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this TopSystem.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this TopSystem.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this TopSystem.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this TopSystem.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this TopSystem.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this TopSystem.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this TopSystem.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this TopSystem.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this TopSystem.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this TopSystem.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this TopSystem.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this TopSystem.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this TopSystem.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this TopSystem.
        The versioning info for this managed object.   

        :return: The version_context of this TopSystem.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this TopSystem.
        The versioning info for this managed object.   

        :param version_context: The version_context of this TopSystem.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this TopSystem.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this TopSystem.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this TopSystem.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this TopSystem.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this TopSystem.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this TopSystem.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this TopSystem.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this TopSystem.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this TopSystem.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this TopSystem.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this TopSystem.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this TopSystem.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this TopSystem.

        :return: The device_mo_id of this TopSystem.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this TopSystem.

        :param device_mo_id: The device_mo_id of this TopSystem.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this TopSystem.
        The Distinguished Name unambiguously identifies an object in the system.  

        :return: The dn of this TopSystem.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this TopSystem.
        The Distinguished Name unambiguously identifies an object in the system.  

        :param dn: The dn of this TopSystem.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this TopSystem.
        The Relative Name uniquely identifies an object within a given context.   

        :return: The rn of this TopSystem.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this TopSystem.
        The Relative Name uniquely identifies an object within a given context.   

        :param rn: The rn of this TopSystem.
        :type: str
        """

        self._rn = rn

    @property
    def ipv4_address(self):
        """
        Gets the ipv4_address of this TopSystem.
        The IPv4 address of system.  

        :return: The ipv4_address of this TopSystem.
        :rtype: str
        """
        return self._ipv4_address

    @ipv4_address.setter
    def ipv4_address(self, ipv4_address):
        """
        Sets the ipv4_address of this TopSystem.
        The IPv4 address of system.  

        :param ipv4_address: The ipv4_address of this TopSystem.
        :type: str
        """

        self._ipv4_address = ipv4_address

    @property
    def ipv6_address(self):
        """
        Gets the ipv6_address of this TopSystem.
        The IPv6 address of system.  

        :return: The ipv6_address of this TopSystem.
        :rtype: str
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        """
        Sets the ipv6_address of this TopSystem.
        The IPv6 address of system.  

        :param ipv6_address: The ipv6_address of this TopSystem.
        :type: str
        """

        self._ipv6_address = ipv6_address

    @property
    def mode(self):
        """
        Gets the mode of this TopSystem.

        :return: The mode of this TopSystem.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this TopSystem.

        :param mode: The mode of this TopSystem.
        :type: str
        """

        self._mode = mode

    @property
    def name(self):
        """
        Gets the name of this TopSystem.

        :return: The name of this TopSystem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TopSystem.

        :param name: The name of this TopSystem.
        :type: str
        """

        self._name = name

    @property
    def time_zone(self):
        """
        Gets the time_zone of this TopSystem.
        The operational timezone of the system, empty indicates no timezone has been set specifically.   

        :return: The time_zone of this TopSystem.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this TopSystem.
        The operational timezone of the system, empty indicates no timezone has been set specifically.   

        :param time_zone: The time_zone of this TopSystem.
        :type: str
        """

        self._time_zone = time_zone

    @property
    def compute_blades(self):
        """
        Gets the compute_blades of this TopSystem.

        :return: The compute_blades of this TopSystem.
        :rtype: list[ComputeBladeRef]
        """
        return self._compute_blades

    @compute_blades.setter
    def compute_blades(self, compute_blades):
        """
        Sets the compute_blades of this TopSystem.

        :param compute_blades: The compute_blades of this TopSystem.
        :type: list[ComputeBladeRef]
        """

        self._compute_blades = compute_blades

    @property
    def compute_rack_units(self):
        """
        Gets the compute_rack_units of this TopSystem.

        :return: The compute_rack_units of this TopSystem.
        :rtype: list[ComputeRackUnitRef]
        """
        return self._compute_rack_units

    @compute_rack_units.setter
    def compute_rack_units(self, compute_rack_units):
        """
        Sets the compute_rack_units of this TopSystem.

        :param compute_rack_units: The compute_rack_units of this TopSystem.
        :type: list[ComputeRackUnitRef]
        """

        self._compute_rack_units = compute_rack_units

    @property
    def management_controller(self):
        """
        Gets the management_controller of this TopSystem.

        :return: The management_controller of this TopSystem.
        :rtype: ManagementControllerRef
        """
        return self._management_controller

    @management_controller.setter
    def management_controller(self, management_controller):
        """
        Sets the management_controller of this TopSystem.

        :param management_controller: The management_controller of this TopSystem.
        :type: ManagementControllerRef
        """

        self._management_controller = management_controller

    @property
    def network_elements(self):
        """
        Gets the network_elements of this TopSystem.

        :return: The network_elements of this TopSystem.
        :rtype: list[NetworkElementRef]
        """
        return self._network_elements

    @network_elements.setter
    def network_elements(self, network_elements):
        """
        Sets the network_elements of this TopSystem.

        :param network_elements: The network_elements of this TopSystem.
        :type: list[NetworkElementRef]
        """

        self._network_elements = network_elements

    @property
    def registered_device(self):
        """
        Gets the registered_device of this TopSystem.
        The Device to which this Managed Object is associated. 

        :return: The registered_device of this TopSystem.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this TopSystem.
        The Device to which this Managed Object is associated. 

        :param registered_device: The registered_device of this TopSystem.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

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
        if not isinstance(other, TopSystem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
