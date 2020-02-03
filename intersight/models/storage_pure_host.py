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


class StoragePureHost(object):
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
        'description': 'str',
        'initiators': 'list[StorageInitiator]',
        'name': 'str',
        'os_type': 'str',
        'storage_array': 'StorageGenericArrayRef',
        'host_group_name': 'str',
        'host_names': 'list[str]',
        'storage_utilization': 'StorageHostUtilization',
        'type': 'str',
        'host_group': 'StoragePureHostRef',
        'hosts': 'list[StoragePureHostRef]',
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
        'description': 'Description',
        'initiators': 'Initiators',
        'name': 'Name',
        'os_type': 'OsType',
        'storage_array': 'StorageArray',
        'host_group_name': 'HostGroupName',
        'host_names': 'HostNames',
        'storage_utilization': 'StorageUtilization',
        'type': 'Type',
        'host_group': 'HostGroup',
        'hosts': 'Hosts',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, description=None, initiators=None, name=None, os_type=None, storage_array=None, host_group_name=None, host_names=None, storage_utilization=None, type='Host', host_group=None, hosts=None, registered_device=None):
        """
        StoragePureHost - a model defined in Swagger
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
        self._description = None
        self._initiators = None
        self._name = None
        self._os_type = None
        self._storage_array = None
        self._host_group_name = None
        self._host_names = None
        self._storage_utilization = None
        self._type = None
        self._host_group = None
        self._hosts = None
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
        if description is not None:
          self.description = description
        if initiators is not None:
          self.initiators = initiators
        if name is not None:
          self.name = name
        if os_type is not None:
          self.os_type = os_type
        if storage_array is not None:
          self.storage_array = storage_array
        if host_group_name is not None:
          self.host_group_name = host_group_name
        if host_names is not None:
          self.host_names = host_names
        if storage_utilization is not None:
          self.storage_utilization = storage_utilization
        if type is not None:
          self.type = type
        if host_group is not None:
          self.host_group = host_group
        if hosts is not None:
          self.hosts = hosts
        if registered_device is not None:
          self.registered_device = registered_device

    @property
    def account_moid(self):
        """
        Gets the account_moid of this StoragePureHost.
        The Account ID for this managed object.  

        :return: The account_moid of this StoragePureHost.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this StoragePureHost.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this StoragePureHost.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this StoragePureHost.
        The time when this managed object was created.  

        :return: The create_time of this StoragePureHost.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this StoragePureHost.
        The time when this managed object was created.  

        :param create_time: The create_time of this StoragePureHost.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this StoragePureHost.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this StoragePureHost.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this StoragePureHost.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this StoragePureHost.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this StoragePureHost.
        The time when this managed object was last modified.  

        :return: The mod_time of this StoragePureHost.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this StoragePureHost.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this StoragePureHost.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this StoragePureHost.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this StoragePureHost.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this StoragePureHost.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this StoragePureHost.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this StoragePureHost.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this StoragePureHost.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StoragePureHost.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this StoragePureHost.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this StoragePureHost.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this StoragePureHost.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this StoragePureHost.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this StoragePureHost.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this StoragePureHost.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this StoragePureHost.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this StoragePureHost.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this StoragePureHost.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this StoragePureHost.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this StoragePureHost.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this StoragePureHost.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this StoragePureHost.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this StoragePureHost.
        The versioning info for this managed object.   

        :return: The version_context of this StoragePureHost.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this StoragePureHost.
        The versioning info for this managed object.   

        :param version_context: The version_context of this StoragePureHost.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this StoragePureHost.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this StoragePureHost.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this StoragePureHost.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this StoragePureHost.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this StoragePureHost.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this StoragePureHost.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this StoragePureHost.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this StoragePureHost.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this StoragePureHost.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this StoragePureHost.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this StoragePureHost.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this StoragePureHost.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def description(self):
        """
        Gets the description of this StoragePureHost.
        Short description about the host.  

        :return: The description of this StoragePureHost.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this StoragePureHost.
        Short description about the host.  

        :param description: The description of this StoragePureHost.
        :type: str
        """

        self._description = description

    @property
    def initiators(self):
        """
        Gets the initiators of this StoragePureHost.
        List of initiators which are associated with host.  

        :return: The initiators of this StoragePureHost.
        :rtype: list[StorageInitiator]
        """
        return self._initiators

    @initiators.setter
    def initiators(self, initiators):
        """
        Sets the initiators of this StoragePureHost.
        List of initiators which are associated with host.  

        :param initiators: The initiators of this StoragePureHost.
        :type: list[StorageInitiator]
        """

        self._initiators = initiators

    @property
    def name(self):
        """
        Gets the name of this StoragePureHost.
        Name of the host in storage array.  

        :return: The name of this StoragePureHost.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StoragePureHost.
        Name of the host in storage array.  

        :param name: The name of this StoragePureHost.
        :type: str
        """

        self._name = name

    @property
    def os_type(self):
        """
        Gets the os_type of this StoragePureHost.
        Operating system running on the host.   

        :return: The os_type of this StoragePureHost.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """
        Sets the os_type of this StoragePureHost.
        Operating system running on the host.   

        :param os_type: The os_type of this StoragePureHost.
        :type: str
        """

        self._os_type = os_type

    @property
    def storage_array(self):
        """
        Gets the storage_array of this StoragePureHost.
        Storage array managed object. 

        :return: The storage_array of this StoragePureHost.
        :rtype: StorageGenericArrayRef
        """
        return self._storage_array

    @storage_array.setter
    def storage_array(self, storage_array):
        """
        Sets the storage_array of this StoragePureHost.
        Storage array managed object. 

        :param storage_array: The storage_array of this StoragePureHost.
        :type: StorageGenericArrayRef
        """

        self._storage_array = storage_array

    @property
    def host_group_name(self):
        """
        Gets the host_group_name of this StoragePureHost.
        Name of host group where the host belongs to. Empty if HostType is set as HostGroup.  

        :return: The host_group_name of this StoragePureHost.
        :rtype: str
        """
        return self._host_group_name

    @host_group_name.setter
    def host_group_name(self, host_group_name):
        """
        Sets the host_group_name of this StoragePureHost.
        Name of host group where the host belongs to. Empty if HostType is set as HostGroup.  

        :param host_group_name: The host_group_name of this StoragePureHost.
        :type: str
        """

        self._host_group_name = host_group_name

    @property
    def host_names(self):
        """
        Gets the host_names of this StoragePureHost.
        Names of the host which are associated with the host group. Empty if HostType is set as Host.  

        :return: The host_names of this StoragePureHost.
        :rtype: list[str]
        """
        return self._host_names

    @host_names.setter
    def host_names(self, host_names):
        """
        Sets the host_names of this StoragePureHost.
        Names of the host which are associated with the host group. Empty if HostType is set as Host.  

        :param host_names: The host_names of this StoragePureHost.
        :type: list[str]
        """

        self._host_names = host_names

    @property
    def storage_utilization(self):
        """
        Gets the storage_utilization of this StoragePureHost.
        Storage space utilized by the host entity.  

        :return: The storage_utilization of this StoragePureHost.
        :rtype: StorageHostUtilization
        """
        return self._storage_utilization

    @storage_utilization.setter
    def storage_utilization(self, storage_utilization):
        """
        Sets the storage_utilization of this StoragePureHost.
        Storage space utilized by the host entity.  

        :param storage_utilization: The storage_utilization of this StoragePureHost.
        :type: StorageHostUtilization
        """

        self._storage_utilization = storage_utilization

    @property
    def type(self):
        """
        Gets the type of this StoragePureHost.
        Type of host entity whether it is a single host or host group (collection of host).   

        :return: The type of this StoragePureHost.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this StoragePureHost.
        Type of host entity whether it is a single host or host group (collection of host).   

        :param type: The type of this StoragePureHost.
        :type: str
        """
        allowed_values = ["Host", "HostGroup"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def host_group(self):
        """
        Gets the host_group of this StoragePureHost.
        A collection of references to the [storage.PureHost](mo://storage.PureHost) Managed Object.  When this managed object is deleted, the referenced [storage.PureHost](mo://storage.PureHost) MO unsets its reference to this deleted MO. 

        :return: The host_group of this StoragePureHost.
        :rtype: StoragePureHostRef
        """
        return self._host_group

    @host_group.setter
    def host_group(self, host_group):
        """
        Sets the host_group of this StoragePureHost.
        A collection of references to the [storage.PureHost](mo://storage.PureHost) Managed Object.  When this managed object is deleted, the referenced [storage.PureHost](mo://storage.PureHost) MO unsets its reference to this deleted MO. 

        :param host_group: The host_group of this StoragePureHost.
        :type: StoragePureHostRef
        """

        self._host_group = host_group

    @property
    def hosts(self):
        """
        Gets the hosts of this StoragePureHost.
        List of host object associated to the host group. 

        :return: The hosts of this StoragePureHost.
        :rtype: list[StoragePureHostRef]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """
        Sets the hosts of this StoragePureHost.
        List of host object associated to the host group. 

        :param hosts: The hosts of this StoragePureHost.
        :type: list[StoragePureHostRef]
        """

        self._hosts = hosts

    @property
    def registered_device(self):
        """
        Gets the registered_device of this StoragePureHost.
        Device registration managed object that represents this storage array connection to Intersight. 

        :return: The registered_device of this StoragePureHost.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this StoragePureHost.
        Device registration managed object that represents this storage array connection to Intersight. 

        :param registered_device: The registered_device of this StoragePureHost.
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
        if not isinstance(other, StoragePureHost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
