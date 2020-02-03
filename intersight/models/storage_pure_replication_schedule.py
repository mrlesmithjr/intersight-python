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


class StoragePureReplicationSchedule(object):
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
        'frequency': 'str',
        'name': 'str',
        'replication_time': 'str',
        'retention_time': 'str',
        'protection_group': 'StorageProtectionGroupRef',
        'storage_array': 'StorageGenericArrayRef',
        'daily_limit': 'int',
        'replication_blackout_intervals': 'list[StorageReplicationBlackout]',
        'snapshot_expiry_time': 'str',
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
        'frequency': 'Frequency',
        'name': 'Name',
        'replication_time': 'ReplicationTime',
        'retention_time': 'RetentionTime',
        'protection_group': 'ProtectionGroup',
        'storage_array': 'StorageArray',
        'daily_limit': 'DailyLimit',
        'replication_blackout_intervals': 'ReplicationBlackoutIntervals',
        'snapshot_expiry_time': 'SnapshotExpiryTime',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, frequency=None, name=None, replication_time=None, retention_time=None, protection_group=None, storage_array=None, daily_limit=None, replication_blackout_intervals=None, snapshot_expiry_time=None, registered_device=None):
        """
        StoragePureReplicationSchedule - a model defined in Swagger
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
        self._frequency = None
        self._name = None
        self._replication_time = None
        self._retention_time = None
        self._protection_group = None
        self._storage_array = None
        self._daily_limit = None
        self._replication_blackout_intervals = None
        self._snapshot_expiry_time = None
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
        if frequency is not None:
          self.frequency = frequency
        if name is not None:
          self.name = name
        if replication_time is not None:
          self.replication_time = replication_time
        if retention_time is not None:
          self.retention_time = retention_time
        if protection_group is not None:
          self.protection_group = protection_group
        if storage_array is not None:
          self.storage_array = storage_array
        if daily_limit is not None:
          self.daily_limit = daily_limit
        if replication_blackout_intervals is not None:
          self.replication_blackout_intervals = replication_blackout_intervals
        if snapshot_expiry_time is not None:
          self.snapshot_expiry_time = snapshot_expiry_time
        if registered_device is not None:
          self.registered_device = registered_device

    @property
    def account_moid(self):
        """
        Gets the account_moid of this StoragePureReplicationSchedule.
        The Account ID for this managed object.  

        :return: The account_moid of this StoragePureReplicationSchedule.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this StoragePureReplicationSchedule.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this StoragePureReplicationSchedule.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this StoragePureReplicationSchedule.
        The time when this managed object was created.  

        :return: The create_time of this StoragePureReplicationSchedule.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this StoragePureReplicationSchedule.
        The time when this managed object was created.  

        :param create_time: The create_time of this StoragePureReplicationSchedule.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this StoragePureReplicationSchedule.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this StoragePureReplicationSchedule.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this StoragePureReplicationSchedule.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this StoragePureReplicationSchedule.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this StoragePureReplicationSchedule.
        The time when this managed object was last modified.  

        :return: The mod_time of this StoragePureReplicationSchedule.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this StoragePureReplicationSchedule.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this StoragePureReplicationSchedule.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this StoragePureReplicationSchedule.
        The unique identifier of this Managed Object instance.   

        :return: The moid of this StoragePureReplicationSchedule.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this StoragePureReplicationSchedule.
        The unique identifier of this Managed Object instance.   

        :param moid: The moid of this StoragePureReplicationSchedule.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this StoragePureReplicationSchedule.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :return: The object_type of this StoragePureReplicationSchedule.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StoragePureReplicationSchedule.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.   

        :param object_type: The object_type of this StoragePureReplicationSchedule.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this StoragePureReplicationSchedule.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this StoragePureReplicationSchedule.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this StoragePureReplicationSchedule.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this StoragePureReplicationSchedule.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this StoragePureReplicationSchedule.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this StoragePureReplicationSchedule.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this StoragePureReplicationSchedule.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this StoragePureReplicationSchedule.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this StoragePureReplicationSchedule.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this StoragePureReplicationSchedule.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this StoragePureReplicationSchedule.
        The array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this StoragePureReplicationSchedule.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this StoragePureReplicationSchedule.
        The versioning info for this managed object.   

        :return: The version_context of this StoragePureReplicationSchedule.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this StoragePureReplicationSchedule.
        The versioning info for this managed object.   

        :param version_context: The version_context of this StoragePureReplicationSchedule.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this StoragePureReplicationSchedule.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this StoragePureReplicationSchedule.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this StoragePureReplicationSchedule.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this StoragePureReplicationSchedule.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this StoragePureReplicationSchedule.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this StoragePureReplicationSchedule.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this StoragePureReplicationSchedule.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this StoragePureReplicationSchedule.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this StoragePureReplicationSchedule.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :return: The permission_resources of this StoragePureReplicationSchedule.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this StoragePureReplicationSchedule.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources. 

        :param permission_resources: The permission_resources of this StoragePureReplicationSchedule.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def frequency(self):
        """
        Gets the frequency of this StoragePureReplicationSchedule.
        Replication frequency. It is an interval on which replication is set to trigger. Examples:     PT2H, Snapshot is performed for every 2 hours.     P30D, Snapshot is scheduled for every 30 days.     PT2H34M56.123S is 2 hours, 34 minutes, 56 seconds and 123 milliseconds.   

        :return: The frequency of this StoragePureReplicationSchedule.
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """
        Sets the frequency of this StoragePureReplicationSchedule.
        Replication frequency. It is an interval on which replication is set to trigger. Examples:     PT2H, Snapshot is performed for every 2 hours.     P30D, Snapshot is scheduled for every 30 days.     PT2H34M56.123S is 2 hours, 34 minutes, 56 seconds and 123 milliseconds.   

        :param frequency: The frequency of this StoragePureReplicationSchedule.
        :type: str
        """

        self._frequency = frequency

    @property
    def name(self):
        """
        Gets the name of this StoragePureReplicationSchedule.
        Replication schedule name.  

        :return: The name of this StoragePureReplicationSchedule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StoragePureReplicationSchedule.
        Replication schedule name.  

        :param name: The name of this StoragePureReplicationSchedule.
        :type: str
        """

        self._name = name

    @property
    def replication_time(self):
        """
        Gets the replication_time of this StoragePureReplicationSchedule.
        Preferred time of day at which to replicate the snapshots on target array. It is applicable only if the replication frequency is set for a day or more. Format: hh:mm:ss Example: 15:00:00, Replication is set for 3:00 PM.   

        :return: The replication_time of this StoragePureReplicationSchedule.
        :rtype: str
        """
        return self._replication_time

    @replication_time.setter
    def replication_time(self, replication_time):
        """
        Sets the replication_time of this StoragePureReplicationSchedule.
        Preferred time of day at which to replicate the snapshots on target array. It is applicable only if the replication frequency is set for a day or more. Format: hh:mm:ss Example: 15:00:00, Replication is set for 3:00 PM.   

        :param replication_time: The replication_time of this StoragePureReplicationSchedule.
        :type: str
        """

        self._replication_time = replication_time

    @property
    def retention_time(self):
        """
        Gets the retention_time of this StoragePureReplicationSchedule.
        Duration to keep the replicated snapshots on the targets. Replicated snapshots are deleted from target array once mentioned rentention period is elapsed. Examples: P30D, Snapshots are available for 30 days. PT2H34M56.123S, 2 hours, 34 minutes, 56 seconds and 123 milliseconds.    

        :return: The retention_time of this StoragePureReplicationSchedule.
        :rtype: str
        """
        return self._retention_time

    @retention_time.setter
    def retention_time(self, retention_time):
        """
        Sets the retention_time of this StoragePureReplicationSchedule.
        Duration to keep the replicated snapshots on the targets. Replicated snapshots are deleted from target array once mentioned rentention period is elapsed. Examples: P30D, Snapshots are available for 30 days. PT2H34M56.123S, 2 hours, 34 minutes, 56 seconds and 123 milliseconds.    

        :param retention_time: The retention_time of this StoragePureReplicationSchedule.
        :type: str
        """

        self._retention_time = retention_time

    @property
    def protection_group(self):
        """
        Gets the protection_group of this StoragePureReplicationSchedule.
        Protection group relationship object. 

        :return: The protection_group of this StoragePureReplicationSchedule.
        :rtype: StorageProtectionGroupRef
        """
        return self._protection_group

    @protection_group.setter
    def protection_group(self, protection_group):
        """
        Sets the protection_group of this StoragePureReplicationSchedule.
        Protection group relationship object. 

        :param protection_group: The protection_group of this StoragePureReplicationSchedule.
        :type: StorageProtectionGroupRef
        """

        self._protection_group = protection_group

    @property
    def storage_array(self):
        """
        Gets the storage_array of this StoragePureReplicationSchedule.
        Storage array managed object. 

        :return: The storage_array of this StoragePureReplicationSchedule.
        :rtype: StorageGenericArrayRef
        """
        return self._storage_array

    @storage_array.setter
    def storage_array(self, storage_array):
        """
        Sets the storage_array of this StoragePureReplicationSchedule.
        Storage array managed object. 

        :param storage_array: The storage_array of this StoragePureReplicationSchedule.
        :type: StorageGenericArrayRef
        """

        self._storage_array = storage_array

    @property
    def daily_limit(self):
        """
        Gets the daily_limit of this StoragePureReplicationSchedule.
        Total number of snapshots per day to be available on target above and over the specified retention time. PureStorage FlashArray maintains all created snapshot until retention period. Daily limit is applied only on the snapshots once retention time is expired. In case of, daily limit is less than the number of snapshot available on source, system select snapshots evenly spaced out throughout the day.   

        :return: The daily_limit of this StoragePureReplicationSchedule.
        :rtype: int
        """
        return self._daily_limit

    @daily_limit.setter
    def daily_limit(self, daily_limit):
        """
        Sets the daily_limit of this StoragePureReplicationSchedule.
        Total number of snapshots per day to be available on target above and over the specified retention time. PureStorage FlashArray maintains all created snapshot until retention period. Daily limit is applied only on the snapshots once retention time is expired. In case of, daily limit is less than the number of snapshot available on source, system select snapshots evenly spaced out throughout the day.   

        :param daily_limit: The daily_limit of this StoragePureReplicationSchedule.
        :type: int
        """

        self._daily_limit = daily_limit

    @property
    def replication_blackout_intervals(self):
        """
        Gets the replication_blackout_intervals of this StoragePureReplicationSchedule.
        Blackout intervals for replication operation in PureStorage FlashArray. System disables replication during these intervals. Blackout periods only apply to scheduled replications. On-demand replications do not observe the blackout period.  

        :return: The replication_blackout_intervals of this StoragePureReplicationSchedule.
        :rtype: list[StorageReplicationBlackout]
        """
        return self._replication_blackout_intervals

    @replication_blackout_intervals.setter
    def replication_blackout_intervals(self, replication_blackout_intervals):
        """
        Sets the replication_blackout_intervals of this StoragePureReplicationSchedule.
        Blackout intervals for replication operation in PureStorage FlashArray. System disables replication during these intervals. Blackout periods only apply to scheduled replications. On-demand replications do not observe the blackout period.  

        :param replication_blackout_intervals: The replication_blackout_intervals of this StoragePureReplicationSchedule.
        :type: list[StorageReplicationBlackout]
        """

        self._replication_blackout_intervals = replication_blackout_intervals

    @property
    def snapshot_expiry_time(self):
        """
        Gets the snapshot_expiry_time of this StoragePureReplicationSchedule.
        Duration to keep the daily limit snapshots on target array. StorageArray deletes the snapshots permanently from the targets beyond this period.   

        :return: The snapshot_expiry_time of this StoragePureReplicationSchedule.
        :rtype: str
        """
        return self._snapshot_expiry_time

    @snapshot_expiry_time.setter
    def snapshot_expiry_time(self, snapshot_expiry_time):
        """
        Sets the snapshot_expiry_time of this StoragePureReplicationSchedule.
        Duration to keep the daily limit snapshots on target array. StorageArray deletes the snapshots permanently from the targets beyond this period.   

        :param snapshot_expiry_time: The snapshot_expiry_time of this StoragePureReplicationSchedule.
        :type: str
        """

        self._snapshot_expiry_time = snapshot_expiry_time

    @property
    def registered_device(self):
        """
        Gets the registered_device of this StoragePureReplicationSchedule.
        Device registration managed object that represents this storage array connection to Intersight. 

        :return: The registered_device of this StoragePureReplicationSchedule.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this StoragePureReplicationSchedule.
        Device registration managed object that represents this storage array connection to Intersight. 

        :param registered_device: The registered_device of this StoragePureReplicationSchedule.
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
        if not isinstance(other, StoragePureReplicationSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
