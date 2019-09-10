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


class InventoryGenericInventory(object):
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
        'inventory_generic_inventory_holder': 'InventoryGenericInventoryHolderRef',
        'key': 'str',
        'registered_device': 'AssetDeviceRegistrationRef',
        'type': 'str',
        'value': 'str'
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
        'inventory_generic_inventory_holder': 'InventoryGenericInventoryHolder',
        'key': 'Key',
        'registered_device': 'RegisteredDevice',
        'type': 'Type',
        'value': 'Value'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, device_mo_id=None, dn=None, rn=None, inventory_generic_inventory_holder=None, key=None, registered_device=None, type=None, value=None):
        """
        InventoryGenericInventory - a model defined in Swagger
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
        self._inventory_generic_inventory_holder = None
        self._key = None
        self._registered_device = None
        self._type = None
        self._value = None

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
        if inventory_generic_inventory_holder is not None:
          self.inventory_generic_inventory_holder = inventory_generic_inventory_holder
        if key is not None:
          self.key = key
        if registered_device is not None:
          self.registered_device = registered_device
        if type is not None:
          self.type = type
        if value is not None:
          self.value = value

    @property
    def account_moid(self):
        """
        Gets the account_moid of this InventoryGenericInventory.
        The Account ID for this managed object.  

        :return: The account_moid of this InventoryGenericInventory.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this InventoryGenericInventory.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this InventoryGenericInventory.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this InventoryGenericInventory.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this InventoryGenericInventory.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this InventoryGenericInventory.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this InventoryGenericInventory.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this InventoryGenericInventory.
        The time when this managed object was created.  

        :return: The create_time of this InventoryGenericInventory.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this InventoryGenericInventory.
        The time when this managed object was created.  

        :param create_time: The create_time of this InventoryGenericInventory.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this InventoryGenericInventory.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this InventoryGenericInventory.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this InventoryGenericInventory.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this InventoryGenericInventory.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this InventoryGenericInventory.
        The time when this managed object was last modified.  

        :return: The mod_time of this InventoryGenericInventory.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this InventoryGenericInventory.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this InventoryGenericInventory.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this InventoryGenericInventory.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this InventoryGenericInventory.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this InventoryGenericInventory.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this InventoryGenericInventory.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this InventoryGenericInventory.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this InventoryGenericInventory.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this InventoryGenericInventory.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this InventoryGenericInventory.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this InventoryGenericInventory.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this InventoryGenericInventory.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this InventoryGenericInventory.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this InventoryGenericInventory.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this InventoryGenericInventory.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this InventoryGenericInventory.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this InventoryGenericInventory.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this InventoryGenericInventory.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this InventoryGenericInventory.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this InventoryGenericInventory.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this InventoryGenericInventory.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this InventoryGenericInventory.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this InventoryGenericInventory.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this InventoryGenericInventory.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this InventoryGenericInventory.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this InventoryGenericInventory.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this InventoryGenericInventory.
        The versioning info for this managed object.   

        :return: The version_context of this InventoryGenericInventory.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this InventoryGenericInventory.
        The versioning info for this managed object.   

        :param version_context: The version_context of this InventoryGenericInventory.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this InventoryGenericInventory.

        :return: The device_mo_id of this InventoryGenericInventory.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this InventoryGenericInventory.

        :param device_mo_id: The device_mo_id of this InventoryGenericInventory.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this InventoryGenericInventory.

        :return: The dn of this InventoryGenericInventory.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this InventoryGenericInventory.

        :param dn: The dn of this InventoryGenericInventory.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this InventoryGenericInventory.

        :return: The rn of this InventoryGenericInventory.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this InventoryGenericInventory.

        :param rn: The rn of this InventoryGenericInventory.
        :type: str
        """

        self._rn = rn

    @property
    def inventory_generic_inventory_holder(self):
        """
        Gets the inventory_generic_inventory_holder of this InventoryGenericInventory.
        A collection of references to the [inventory.GenericInventoryHolder](mo://inventory.GenericInventoryHolder) Managed Object.  When this managed object is deleted, the referenced [inventory.GenericInventoryHolder](mo://inventory.GenericInventoryHolder) MO unsets its reference to this deleted MO. 

        :return: The inventory_generic_inventory_holder of this InventoryGenericInventory.
        :rtype: InventoryGenericInventoryHolderRef
        """
        return self._inventory_generic_inventory_holder

    @inventory_generic_inventory_holder.setter
    def inventory_generic_inventory_holder(self, inventory_generic_inventory_holder):
        """
        Sets the inventory_generic_inventory_holder of this InventoryGenericInventory.
        A collection of references to the [inventory.GenericInventoryHolder](mo://inventory.GenericInventoryHolder) Managed Object.  When this managed object is deleted, the referenced [inventory.GenericInventoryHolder](mo://inventory.GenericInventoryHolder) MO unsets its reference to this deleted MO. 

        :param inventory_generic_inventory_holder: The inventory_generic_inventory_holder of this InventoryGenericInventory.
        :type: InventoryGenericInventoryHolderRef
        """

        self._inventory_generic_inventory_holder = inventory_generic_inventory_holder

    @property
    def key(self):
        """
        Gets the key of this InventoryGenericInventory.

        :return: The key of this InventoryGenericInventory.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this InventoryGenericInventory.

        :param key: The key of this InventoryGenericInventory.
        :type: str
        """

        self._key = key

    @property
    def registered_device(self):
        """
        Gets the registered_device of this InventoryGenericInventory.
        The Device to which this Managed Object is associated. 

        :return: The registered_device of this InventoryGenericInventory.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this InventoryGenericInventory.
        The Device to which this Managed Object is associated. 

        :param registered_device: The registered_device of this InventoryGenericInventory.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def type(self):
        """
        Gets the type of this InventoryGenericInventory.

        :return: The type of this InventoryGenericInventory.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this InventoryGenericInventory.

        :param type: The type of this InventoryGenericInventory.
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """
        Gets the value of this InventoryGenericInventory.

        :return: The value of this InventoryGenericInventory.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this InventoryGenericInventory.

        :param value: The value of this InventoryGenericInventory.
        :type: str
        """

        self._value = value

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
        if not isinstance(other, InventoryGenericInventory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
