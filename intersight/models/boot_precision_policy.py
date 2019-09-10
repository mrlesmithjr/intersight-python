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


class BootPrecisionPolicy(object):
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
        'description': 'str',
        'name': 'str',
        'boot_devices': 'list[BootDeviceBase]',
        'configured_boot_mode': 'str',
        'enforce_uefi_secure_boot': 'bool',
        'organization': 'IamAccountRef',
        'profiles': 'list[PolicyAbstractConfigProfileRef]'
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
        'description': 'Description',
        'name': 'Name',
        'boot_devices': 'BootDevices',
        'configured_boot_mode': 'ConfiguredBootMode',
        'enforce_uefi_secure_boot': 'EnforceUefiSecureBoot',
        'organization': 'Organization',
        'profiles': 'Profiles'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, description=None, name=None, boot_devices=None, configured_boot_mode='Legacy', enforce_uefi_secure_boot=None, organization=None, profiles=None):
        """
        BootPrecisionPolicy - a model defined in Swagger
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
        self._description = None
        self._name = None
        self._boot_devices = None
        self._configured_boot_mode = None
        self._enforce_uefi_secure_boot = None
        self._organization = None
        self._profiles = None

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
        if description is not None:
          self.description = description
        if name is not None:
          self.name = name
        if boot_devices is not None:
          self.boot_devices = boot_devices
        if configured_boot_mode is not None:
          self.configured_boot_mode = configured_boot_mode
        if enforce_uefi_secure_boot is not None:
          self.enforce_uefi_secure_boot = enforce_uefi_secure_boot
        if organization is not None:
          self.organization = organization
        if profiles is not None:
          self.profiles = profiles

    @property
    def account_moid(self):
        """
        Gets the account_moid of this BootPrecisionPolicy.
        The Account ID for this managed object.  

        :return: The account_moid of this BootPrecisionPolicy.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this BootPrecisionPolicy.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this BootPrecisionPolicy.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this BootPrecisionPolicy.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this BootPrecisionPolicy.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this BootPrecisionPolicy.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this BootPrecisionPolicy.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this BootPrecisionPolicy.
        The time when this managed object was created.  

        :return: The create_time of this BootPrecisionPolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this BootPrecisionPolicy.
        The time when this managed object was created.  

        :param create_time: The create_time of this BootPrecisionPolicy.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this BootPrecisionPolicy.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this BootPrecisionPolicy.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this BootPrecisionPolicy.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this BootPrecisionPolicy.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this BootPrecisionPolicy.
        The time when this managed object was last modified.  

        :return: The mod_time of this BootPrecisionPolicy.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this BootPrecisionPolicy.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this BootPrecisionPolicy.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this BootPrecisionPolicy.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this BootPrecisionPolicy.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this BootPrecisionPolicy.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this BootPrecisionPolicy.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this BootPrecisionPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this BootPrecisionPolicy.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this BootPrecisionPolicy.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this BootPrecisionPolicy.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this BootPrecisionPolicy.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this BootPrecisionPolicy.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this BootPrecisionPolicy.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this BootPrecisionPolicy.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this BootPrecisionPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this BootPrecisionPolicy.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this BootPrecisionPolicy.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this BootPrecisionPolicy.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this BootPrecisionPolicy.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this BootPrecisionPolicy.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this BootPrecisionPolicy.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this BootPrecisionPolicy.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this BootPrecisionPolicy.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this BootPrecisionPolicy.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this BootPrecisionPolicy.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this BootPrecisionPolicy.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this BootPrecisionPolicy.
        The versioning info for this managed object.   

        :return: The version_context of this BootPrecisionPolicy.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this BootPrecisionPolicy.
        The versioning info for this managed object.   

        :param version_context: The version_context of this BootPrecisionPolicy.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def description(self):
        """
        Gets the description of this BootPrecisionPolicy.
        Description of the policy.  

        :return: The description of this BootPrecisionPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BootPrecisionPolicy.
        Description of the policy.  

        :param description: The description of this BootPrecisionPolicy.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this BootPrecisionPolicy.
        Name of the concrete policy.   

        :return: The name of this BootPrecisionPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BootPrecisionPolicy.
        Name of the concrete policy.   

        :param name: The name of this BootPrecisionPolicy.
        :type: str
        """

        self._name = name

    @property
    def boot_devices(self):
        """
        Gets the boot_devices of this BootPrecisionPolicy.
        Set of boot devices to be configured.  

        :return: The boot_devices of this BootPrecisionPolicy.
        :rtype: list[BootDeviceBase]
        """
        return self._boot_devices

    @boot_devices.setter
    def boot_devices(self, boot_devices):
        """
        Sets the boot_devices of this BootPrecisionPolicy.
        Set of boot devices to be configured.  

        :param boot_devices: The boot_devices of this BootPrecisionPolicy.
        :type: list[BootDeviceBase]
        """

        self._boot_devices = boot_devices

    @property
    def configured_boot_mode(self):
        """
        Gets the configured_boot_mode of this BootPrecisionPolicy.
        Sets the BIOS boot mode. UEFI uses the GUID Partition Table (GPT) whereas Legacy mode uses the Master Boot Record (MBR) partitioning scheme.  

        :return: The configured_boot_mode of this BootPrecisionPolicy.
        :rtype: str
        """
        return self._configured_boot_mode

    @configured_boot_mode.setter
    def configured_boot_mode(self, configured_boot_mode):
        """
        Sets the configured_boot_mode of this BootPrecisionPolicy.
        Sets the BIOS boot mode. UEFI uses the GUID Partition Table (GPT) whereas Legacy mode uses the Master Boot Record (MBR) partitioning scheme.  

        :param configured_boot_mode: The configured_boot_mode of this BootPrecisionPolicy.
        :type: str
        """
        allowed_values = ["Legacy", "Uefi"]
        if configured_boot_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `configured_boot_mode` ({0}), must be one of {1}"
                .format(configured_boot_mode, allowed_values)
            )

        self._configured_boot_mode = configured_boot_mode

    @property
    def enforce_uefi_secure_boot(self):
        """
        Gets the enforce_uefi_secure_boot of this BootPrecisionPolicy.
        If UEFI secure boot is enabled, the boot mode is set to UEFI by default. Secure boot enforces that device boots using only software that is trusted by the Original Equipment Manufacturer (OEM).   

        :return: The enforce_uefi_secure_boot of this BootPrecisionPolicy.
        :rtype: bool
        """
        return self._enforce_uefi_secure_boot

    @enforce_uefi_secure_boot.setter
    def enforce_uefi_secure_boot(self, enforce_uefi_secure_boot):
        """
        Sets the enforce_uefi_secure_boot of this BootPrecisionPolicy.
        If UEFI secure boot is enabled, the boot mode is set to UEFI by default. Secure boot enforces that device boots using only software that is trusted by the Original Equipment Manufacturer (OEM).   

        :param enforce_uefi_secure_boot: The enforce_uefi_secure_boot of this BootPrecisionPolicy.
        :type: bool
        """

        self._enforce_uefi_secure_boot = enforce_uefi_secure_boot

    @property
    def organization(self):
        """
        Gets the organization of this BootPrecisionPolicy.
        Relationship to the Organization that owns the Managed Object. 

        :return: The organization of this BootPrecisionPolicy.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this BootPrecisionPolicy.
        Relationship to the Organization that owns the Managed Object. 

        :param organization: The organization of this BootPrecisionPolicy.
        :type: IamAccountRef
        """

        self._organization = organization

    @property
    def profiles(self):
        """
        Gets the profiles of this BootPrecisionPolicy.
        Reference to the profile objects that this policy is a part of. 

        :return: The profiles of this BootPrecisionPolicy.
        :rtype: list[PolicyAbstractConfigProfileRef]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """
        Sets the profiles of this BootPrecisionPolicy.
        Reference to the profile objects that this policy is a part of. 

        :param profiles: The profiles of this BootPrecisionPolicy.
        :type: list[PolicyAbstractConfigProfileRef]
        """

        self._profiles = profiles

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
        if not isinstance(other, BootPrecisionPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
