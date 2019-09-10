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


class StorageArrayDisk(object):
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
        'ancestors': 'list[MoBaseMoRef]',
        'create_time': 'datetime',
        'domain_group_moid': 'str',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoBaseMoRef',
        'shared_scope': 'str',
        'tags': 'list[MoTag]',
        'version_context': 'MoVersionContext',
        'device_mo_id': 'str',
        'dn': 'str',
        'rn': 'str',
        'model': 'str',
        'revision': 'str',
        'serial': 'str',
        'vendor': 'str',
        'name': 'str',
        'part_number': 'str',
        'protocol': 'str',
        'speed': 'int',
        'status': 'str',
        'storage_array': 'StorageGenericArrayRef',
        'storage_utilization': 'StorageCapacity',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'ancestors': 'Ancestors',
        'create_time': 'CreateTime',
        'domain_group_moid': 'DomainGroupMoid',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'parent': 'Parent',
        'shared_scope': 'SharedScope',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'device_mo_id': 'DeviceMoId',
        'dn': 'Dn',
        'rn': 'Rn',
        'model': 'Model',
        'revision': 'Revision',
        'serial': 'Serial',
        'vendor': 'Vendor',
        'name': 'Name',
        'part_number': 'PartNumber',
        'protocol': 'Protocol',
        'speed': 'Speed',
        'status': 'Status',
        'storage_array': 'StorageArray',
        'storage_utilization': 'StorageUtilization',
        'type': 'Type',
        'version': 'Version'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, name=None, part_number=None, protocol='Unknown', speed=None, status='Unknown', storage_array=None, storage_utilization=None, type='Unknown', version=None):
        """
        StorageArrayDisk - a model defined in Swagger
        """

        self._account_moid = None
        self._ancestors = None
        self._create_time = None
        self._domain_group_moid = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._parent = None
        self._shared_scope = None
        self._tags = None
        self._version_context = None
        self._device_mo_id = None
        self._dn = None
        self._rn = None
        self._model = None
        self._revision = None
        self._serial = None
        self._vendor = None
        self._name = None
        self._part_number = None
        self._protocol = None
        self._speed = None
        self._status = None
        self._storage_array = None
        self._storage_utilization = None
        self._type = None
        self._version = None

        if account_moid is not None:
          self.account_moid = account_moid
        if ancestors is not None:
          self.ancestors = ancestors
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
        if parent is not None:
          self.parent = parent
        if shared_scope is not None:
          self.shared_scope = shared_scope
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if device_mo_id is not None:
          self.device_mo_id = device_mo_id
        if dn is not None:
          self.dn = dn
        if rn is not None:
          self.rn = rn
        if model is not None:
          self.model = model
        if revision is not None:
          self.revision = revision
        if serial is not None:
          self.serial = serial
        if vendor is not None:
          self.vendor = vendor
        if name is not None:
          self.name = name
        if part_number is not None:
          self.part_number = part_number
        if protocol is not None:
          self.protocol = protocol
        if speed is not None:
          self.speed = speed
        if status is not None:
          self.status = status
        if storage_array is not None:
          self.storage_array = storage_array
        if storage_utilization is not None:
          self.storage_utilization = storage_utilization
        if type is not None:
          self.type = type
        if version is not None:
          self.version = version

    @property
    def account_moid(self):
        """
        Gets the account_moid of this StorageArrayDisk.
        The Account ID for this managed object.  

        :return: The account_moid of this StorageArrayDisk.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this StorageArrayDisk.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this StorageArrayDisk.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this StorageArrayDisk.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this StorageArrayDisk.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this StorageArrayDisk.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this StorageArrayDisk.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this StorageArrayDisk.
        The time when this managed object was created.  

        :return: The create_time of this StorageArrayDisk.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this StorageArrayDisk.
        The time when this managed object was created.  

        :param create_time: The create_time of this StorageArrayDisk.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this StorageArrayDisk.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this StorageArrayDisk.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this StorageArrayDisk.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this StorageArrayDisk.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this StorageArrayDisk.
        The time when this managed object was last modified.  

        :return: The mod_time of this StorageArrayDisk.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this StorageArrayDisk.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this StorageArrayDisk.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this StorageArrayDisk.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this StorageArrayDisk.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this StorageArrayDisk.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this StorageArrayDisk.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this StorageArrayDisk.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this StorageArrayDisk.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StorageArrayDisk.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this StorageArrayDisk.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this StorageArrayDisk.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this StorageArrayDisk.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this StorageArrayDisk.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this StorageArrayDisk.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this StorageArrayDisk.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this StorageArrayDisk.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this StorageArrayDisk.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this StorageArrayDisk.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this StorageArrayDisk.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this StorageArrayDisk.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this StorageArrayDisk.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this StorageArrayDisk.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this StorageArrayDisk.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this StorageArrayDisk.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this StorageArrayDisk.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this StorageArrayDisk.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this StorageArrayDisk.
        The versioning info for this managed object.   

        :return: The version_context of this StorageArrayDisk.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this StorageArrayDisk.
        The versioning info for this managed object.   

        :param version_context: The version_context of this StorageArrayDisk.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this StorageArrayDisk.

        :return: The device_mo_id of this StorageArrayDisk.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this StorageArrayDisk.

        :param device_mo_id: The device_mo_id of this StorageArrayDisk.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this StorageArrayDisk.

        :return: The dn of this StorageArrayDisk.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this StorageArrayDisk.

        :param dn: The dn of this StorageArrayDisk.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this StorageArrayDisk.

        :return: The rn of this StorageArrayDisk.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this StorageArrayDisk.

        :param rn: The rn of this StorageArrayDisk.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this StorageArrayDisk.
        This field identifies the model of the given component.  

        :return: The model of this StorageArrayDisk.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this StorageArrayDisk.
        This field identifies the model of the given component.  

        :param model: The model of this StorageArrayDisk.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this StorageArrayDisk.

        :return: The revision of this StorageArrayDisk.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this StorageArrayDisk.

        :param revision: The revision of this StorageArrayDisk.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this StorageArrayDisk.
        This field identifies the serial of the given component.  

        :return: The serial of this StorageArrayDisk.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this StorageArrayDisk.
        This field identifies the serial of the given component.  

        :param serial: The serial of this StorageArrayDisk.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this StorageArrayDisk.
        This field identifies the vendor of the given component.   

        :return: The vendor of this StorageArrayDisk.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this StorageArrayDisk.
        This field identifies the vendor of the given component.   

        :param vendor: The vendor of this StorageArrayDisk.
        :type: str
        """

        self._vendor = vendor

    @property
    def name(self):
        """
        Gets the name of this StorageArrayDisk.
        Disk name available in storage array.  

        :return: The name of this StorageArrayDisk.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StorageArrayDisk.
        Disk name available in storage array.  

        :param name: The name of this StorageArrayDisk.
        :type: str
        """

        self._name = name

    @property
    def part_number(self):
        """
        Gets the part_number of this StorageArrayDisk.
        Storage disk part number.  

        :return: The part_number of this StorageArrayDisk.
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """
        Sets the part_number of this StorageArrayDisk.
        Storage disk part number.  

        :param part_number: The part_number of this StorageArrayDisk.
        :type: str
        """

        self._part_number = part_number

    @property
    def protocol(self):
        """
        Gets the protocol of this StorageArrayDisk.
        Storage protocol used in disk for communication. Possible values are SAS, SATA and NVMe.  

        :return: The protocol of this StorageArrayDisk.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this StorageArrayDisk.
        Storage protocol used in disk for communication. Possible values are SAS, SATA and NVMe.  

        :param protocol: The protocol of this StorageArrayDisk.
        :type: str
        """
        allowed_values = ["Unknown", "SAS", "NVMe", "SATA"]
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def speed(self):
        """
        Gets the speed of this StorageArrayDisk.
        Disk speed for read or write operation measured in rpm.  

        :return: The speed of this StorageArrayDisk.
        :rtype: int
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """
        Sets the speed of this StorageArrayDisk.
        Disk speed for read or write operation measured in rpm.  

        :param speed: The speed of this StorageArrayDisk.
        :type: int
        """

        self._speed = speed

    @property
    def status(self):
        """
        Gets the status of this StorageArrayDisk.
        Storage disk health status.  

        :return: The status of this StorageArrayDisk.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this StorageArrayDisk.
        Storage disk health status.  

        :param status: The status of this StorageArrayDisk.
        :type: str
        """
        allowed_values = ["Unknown", "Ok", "Degraded", "Critical", "Offline", "Identifying", "NotAvailable", "Updating", "Unrecognized"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def storage_array(self):
        """
        Gets the storage_array of this StorageArrayDisk.
        Storage array managed object. 

        :return: The storage_array of this StorageArrayDisk.
        :rtype: StorageGenericArrayRef
        """
        return self._storage_array

    @storage_array.setter
    def storage_array(self, storage_array):
        """
        Sets the storage_array of this StorageArrayDisk.
        Storage array managed object. 

        :param storage_array: The storage_array of this StorageArrayDisk.
        :type: StorageGenericArrayRef
        """

        self._storage_array = storage_array

    @property
    def storage_utilization(self):
        """
        Gets the storage_utilization of this StorageArrayDisk.
        Storage utilization information of storage disk.  

        :return: The storage_utilization of this StorageArrayDisk.
        :rtype: StorageCapacity
        """
        return self._storage_utilization

    @storage_utilization.setter
    def storage_utilization(self, storage_utilization):
        """
        Sets the storage_utilization of this StorageArrayDisk.
        Storage utilization information of storage disk.  

        :param storage_utilization: The storage_utilization of this StorageArrayDisk.
        :type: StorageCapacity
        """

        self._storage_utilization = storage_utilization

    @property
    def type(self):
        """
        Gets the type of this StorageArrayDisk.
        Storage disk type, it can be SSD, HDD, NVRAM.  

        :return: The type of this StorageArrayDisk.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this StorageArrayDisk.
        Storage disk type, it can be SSD, HDD, NVRAM.  

        :param type: The type of this StorageArrayDisk.
        :type: str
        """
        allowed_values = ["Unknown", "SSD", "HDD", "NVRAM"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def version(self):
        """
        Gets the version of this StorageArrayDisk.
        Storage disk version number.   

        :return: The version of this StorageArrayDisk.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this StorageArrayDisk.
        Storage disk version number.   

        :param version: The version of this StorageArrayDisk.
        :type: str
        """

        self._version = version

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
        if not isinstance(other, StorageArrayDisk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
