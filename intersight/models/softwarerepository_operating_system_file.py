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


class SoftwarerepositoryOperatingSystemFile(object):
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
        'download_count': 'int',
        'import_action': 'str',
        'import_state': 'str',
        'imported_time': 'datetime',
        'last_access_time': 'datetime',
        'md5sum': 'str',
        'name': 'str',
        'release_date': 'datetime',
        'sha512sum': 'str',
        'size': 'int',
        'software_advisory_url': 'str',
        'source': 'SoftwarerepositoryFileServer',
        'version': 'str',
        'catalog': 'SoftwarerepositoryCatalogRef',
        'vendor': 'str'
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
        'download_count': 'DownloadCount',
        'import_action': 'ImportAction',
        'import_state': 'ImportState',
        'imported_time': 'ImportedTime',
        'last_access_time': 'LastAccessTime',
        'md5sum': 'Md5sum',
        'name': 'Name',
        'release_date': 'ReleaseDate',
        'sha512sum': 'Sha512sum',
        'size': 'Size',
        'software_advisory_url': 'SoftwareAdvisoryUrl',
        'source': 'Source',
        'version': 'Version',
        'catalog': 'Catalog',
        'vendor': 'Vendor'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, description=None, download_count=None, import_action='None', import_state='ReadyForImport', imported_time=None, last_access_time=None, md5sum=None, name=None, release_date=None, sha512sum=None, size=None, software_advisory_url=None, source=None, version=None, catalog=None, vendor=None):
        """
        SoftwarerepositoryOperatingSystemFile - a model defined in Swagger
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
        self._download_count = None
        self._import_action = None
        self._import_state = None
        self._imported_time = None
        self._last_access_time = None
        self._md5sum = None
        self._name = None
        self._release_date = None
        self._sha512sum = None
        self._size = None
        self._software_advisory_url = None
        self._source = None
        self._version = None
        self._catalog = None
        self._vendor = None

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
        if download_count is not None:
          self.download_count = download_count
        if import_action is not None:
          self.import_action = import_action
        if import_state is not None:
          self.import_state = import_state
        if imported_time is not None:
          self.imported_time = imported_time
        if last_access_time is not None:
          self.last_access_time = last_access_time
        if md5sum is not None:
          self.md5sum = md5sum
        if name is not None:
          self.name = name
        if release_date is not None:
          self.release_date = release_date
        if sha512sum is not None:
          self.sha512sum = sha512sum
        if size is not None:
          self.size = size
        if software_advisory_url is not None:
          self.software_advisory_url = software_advisory_url
        if source is not None:
          self.source = source
        if version is not None:
          self.version = version
        if catalog is not None:
          self.catalog = catalog
        if vendor is not None:
          self.vendor = vendor

    @property
    def account_moid(self):
        """
        Gets the account_moid of this SoftwarerepositoryOperatingSystemFile.
        The Account ID for this managed object.  

        :return: The account_moid of this SoftwarerepositoryOperatingSystemFile.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this SoftwarerepositoryOperatingSystemFile.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this SoftwarerepositoryOperatingSystemFile.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this SoftwarerepositoryOperatingSystemFile.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this SoftwarerepositoryOperatingSystemFile.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this SoftwarerepositoryOperatingSystemFile.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this SoftwarerepositoryOperatingSystemFile.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this SoftwarerepositoryOperatingSystemFile.
        The time when this managed object was created.  

        :return: The create_time of this SoftwarerepositoryOperatingSystemFile.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this SoftwarerepositoryOperatingSystemFile.
        The time when this managed object was created.  

        :param create_time: The create_time of this SoftwarerepositoryOperatingSystemFile.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this SoftwarerepositoryOperatingSystemFile.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this SoftwarerepositoryOperatingSystemFile.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this SoftwarerepositoryOperatingSystemFile.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this SoftwarerepositoryOperatingSystemFile.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this SoftwarerepositoryOperatingSystemFile.
        The time when this managed object was last modified.  

        :return: The mod_time of this SoftwarerepositoryOperatingSystemFile.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this SoftwarerepositoryOperatingSystemFile.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this SoftwarerepositoryOperatingSystemFile.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this SoftwarerepositoryOperatingSystemFile.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this SoftwarerepositoryOperatingSystemFile.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this SoftwarerepositoryOperatingSystemFile.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this SoftwarerepositoryOperatingSystemFile.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this SoftwarerepositoryOperatingSystemFile.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this SoftwarerepositoryOperatingSystemFile.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this SoftwarerepositoryOperatingSystemFile.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this SoftwarerepositoryOperatingSystemFile.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this SoftwarerepositoryOperatingSystemFile.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this SoftwarerepositoryOperatingSystemFile.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this SoftwarerepositoryOperatingSystemFile.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this SoftwarerepositoryOperatingSystemFile.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this SoftwarerepositoryOperatingSystemFile.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this SoftwarerepositoryOperatingSystemFile.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this SoftwarerepositoryOperatingSystemFile.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this SoftwarerepositoryOperatingSystemFile.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this SoftwarerepositoryOperatingSystemFile.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this SoftwarerepositoryOperatingSystemFile.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this SoftwarerepositoryOperatingSystemFile.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this SoftwarerepositoryOperatingSystemFile.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this SoftwarerepositoryOperatingSystemFile.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this SoftwarerepositoryOperatingSystemFile.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this SoftwarerepositoryOperatingSystemFile.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this SoftwarerepositoryOperatingSystemFile.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this SoftwarerepositoryOperatingSystemFile.
        The versioning info for this managed object.   

        :return: The version_context of this SoftwarerepositoryOperatingSystemFile.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this SoftwarerepositoryOperatingSystemFile.
        The versioning info for this managed object.   

        :param version_context: The version_context of this SoftwarerepositoryOperatingSystemFile.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def description(self):
        """
        Gets the description of this SoftwarerepositoryOperatingSystemFile.
        User provided description about the file. Cisco provided description for image inventoried from a Cisco repository.  

        :return: The description of this SoftwarerepositoryOperatingSystemFile.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SoftwarerepositoryOperatingSystemFile.
        User provided description about the file. Cisco provided description for image inventoried from a Cisco repository.  

        :param description: The description of this SoftwarerepositoryOperatingSystemFile.
        :type: str
        """

        self._description = description

    @property
    def download_count(self):
        """
        Gets the download_count of this SoftwarerepositoryOperatingSystemFile.
        The number of times this file has been downloaded from the local repository. It is used by the repository monitoring process to determine the files that are to be evicted from the cache.  

        :return: The download_count of this SoftwarerepositoryOperatingSystemFile.
        :rtype: int
        """
        return self._download_count

    @download_count.setter
    def download_count(self, download_count):
        """
        Sets the download_count of this SoftwarerepositoryOperatingSystemFile.
        The number of times this file has been downloaded from the local repository. It is used by the repository monitoring process to determine the files that are to be evicted from the cache.  

        :param download_count: The download_count of this SoftwarerepositoryOperatingSystemFile.
        :type: int
        """

        self._download_count = download_count

    @property
    def import_action(self):
        """
        Gets the import_action of this SoftwarerepositoryOperatingSystemFile.
        The action to be performed on the imported file. If 'PreCache' is set, the image will be cached in Appliance. Applicable in Intersight appliance deployment. If 'Evict' is set, the cached file will be removed. Applicable in Intersight appliance deployment. If 'GeneratePreSignedUploadUrl' is set, generates pre signed URL (s) for the file to be imported into the repository. Applicable for local machine source. The URL (s) will be populated under LocalMachine file server. If 'CompleteImportProcess' is set, the ImportState is marked as 'Imported'. Applicable for local machine source. If 'Cancel' is set, the ImportState is marked as 'Failed'. Applicable for local machine source.   

        :return: The import_action of this SoftwarerepositoryOperatingSystemFile.
        :rtype: str
        """
        return self._import_action

    @import_action.setter
    def import_action(self, import_action):
        """
        Sets the import_action of this SoftwarerepositoryOperatingSystemFile.
        The action to be performed on the imported file. If 'PreCache' is set, the image will be cached in Appliance. Applicable in Intersight appliance deployment. If 'Evict' is set, the cached file will be removed. Applicable in Intersight appliance deployment. If 'GeneratePreSignedUploadUrl' is set, generates pre signed URL (s) for the file to be imported into the repository. Applicable for local machine source. The URL (s) will be populated under LocalMachine file server. If 'CompleteImportProcess' is set, the ImportState is marked as 'Imported'. Applicable for local machine source. If 'Cancel' is set, the ImportState is marked as 'Failed'. Applicable for local machine source.   

        :param import_action: The import_action of this SoftwarerepositoryOperatingSystemFile.
        :type: str
        """
        allowed_values = ["None", "GeneratePreSignedUploadUrl", "CompleteImportProcess", "PreCache", "Cancel", "Evict"]
        if import_action not in allowed_values:
            raise ValueError(
                "Invalid value for `import_action` ({0}), must be one of {1}"
                .format(import_action, allowed_values)
            )

        self._import_action = import_action

    @property
    def import_state(self):
        """
        Gets the import_state of this SoftwarerepositoryOperatingSystemFile.
        The state  of this file in the repository or Appliance. The importState is updated during the import operation and as part of the repository monitoring process.  

        :return: The import_state of this SoftwarerepositoryOperatingSystemFile.
        :rtype: str
        """
        return self._import_state

    @import_state.setter
    def import_state(self, import_state):
        """
        Sets the import_state of this SoftwarerepositoryOperatingSystemFile.
        The state  of this file in the repository or Appliance. The importState is updated during the import operation and as part of the repository monitoring process.  

        :param import_state: The import_state of this SoftwarerepositoryOperatingSystemFile.
        :type: str
        """
        allowed_values = ["ReadyForImport", "Importing", "Imported", "Failed", "MetaOnly", "ReadyForCache", "Caching", "Cached", "CachingFailed", "Corrupted", "Evicted"]
        if import_state not in allowed_values:
            raise ValueError(
                "Invalid value for `import_state` ({0}), must be one of {1}"
                .format(import_state, allowed_values)
            )

        self._import_state = import_state

    @property
    def imported_time(self):
        """
        Gets the imported_time of this SoftwarerepositoryOperatingSystemFile.
        The time at which this image or file was imported/cached into the repositry. if the 'ImportState' is 'Imported', the time at which this image or file was imported. if the 'ImportState' is 'Cached', the time at which this image or file was cached.  

        :return: The imported_time of this SoftwarerepositoryOperatingSystemFile.
        :rtype: datetime
        """
        return self._imported_time

    @imported_time.setter
    def imported_time(self, imported_time):
        """
        Sets the imported_time of this SoftwarerepositoryOperatingSystemFile.
        The time at which this image or file was imported/cached into the repositry. if the 'ImportState' is 'Imported', the time at which this image or file was imported. if the 'ImportState' is 'Cached', the time at which this image or file was cached.  

        :param imported_time: The imported_time of this SoftwarerepositoryOperatingSystemFile.
        :type: datetime
        """

        self._imported_time = imported_time

    @property
    def last_access_time(self):
        """
        Gets the last_access_time of this SoftwarerepositoryOperatingSystemFile.
        The time at which this file was last downloaded from the local repository. It is used by the repository monitoring process to determine the files that are to be evicted from the cache.  

        :return: The last_access_time of this SoftwarerepositoryOperatingSystemFile.
        :rtype: datetime
        """
        return self._last_access_time

    @last_access_time.setter
    def last_access_time(self, last_access_time):
        """
        Sets the last_access_time of this SoftwarerepositoryOperatingSystemFile.
        The time at which this file was last downloaded from the local repository. It is used by the repository monitoring process to determine the files that are to be evicted from the cache.  

        :param last_access_time: The last_access_time of this SoftwarerepositoryOperatingSystemFile.
        :type: datetime
        """

        self._last_access_time = last_access_time

    @property
    def md5sum(self):
        """
        Gets the md5sum of this SoftwarerepositoryOperatingSystemFile.
        The md5sum checksum of the file. This information is available for all Cisco distributed images and files imported to the local repository.  

        :return: The md5sum of this SoftwarerepositoryOperatingSystemFile.
        :rtype: str
        """
        return self._md5sum

    @md5sum.setter
    def md5sum(self, md5sum):
        """
        Sets the md5sum of this SoftwarerepositoryOperatingSystemFile.
        The md5sum checksum of the file. This information is available for all Cisco distributed images and files imported to the local repository.  

        :param md5sum: The md5sum of this SoftwarerepositoryOperatingSystemFile.
        :type: str
        """

        self._md5sum = md5sum

    @property
    def name(self):
        """
        Gets the name of this SoftwarerepositoryOperatingSystemFile.
        The name of the file. It is populated as part of the image import operation.   

        :return: The name of this SoftwarerepositoryOperatingSystemFile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SoftwarerepositoryOperatingSystemFile.
        The name of the file. It is populated as part of the image import operation.   

        :param name: The name of this SoftwarerepositoryOperatingSystemFile.
        :type: str
        """

        self._name = name

    @property
    def release_date(self):
        """
        Gets the release_date of this SoftwarerepositoryOperatingSystemFile.
        The date on which the file was released or distributed by its vendor.  

        :return: The release_date of this SoftwarerepositoryOperatingSystemFile.
        :rtype: datetime
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """
        Sets the release_date of this SoftwarerepositoryOperatingSystemFile.
        The date on which the file was released or distributed by its vendor.  

        :param release_date: The release_date of this SoftwarerepositoryOperatingSystemFile.
        :type: datetime
        """

        self._release_date = release_date

    @property
    def sha512sum(self):
        """
        Gets the sha512sum of this SoftwarerepositoryOperatingSystemFile.
        The sha512sum of the file. This information is available for all Cisco distributed images and files imported to the local repository.  

        :return: The sha512sum of this SoftwarerepositoryOperatingSystemFile.
        :rtype: str
        """
        return self._sha512sum

    @sha512sum.setter
    def sha512sum(self, sha512sum):
        """
        Sets the sha512sum of this SoftwarerepositoryOperatingSystemFile.
        The sha512sum of the file. This information is available for all Cisco distributed images and files imported to the local repository.  

        :param sha512sum: The sha512sum of this SoftwarerepositoryOperatingSystemFile.
        :type: str
        """

        self._sha512sum = sha512sum

    @property
    def size(self):
        """
        Gets the size of this SoftwarerepositoryOperatingSystemFile.
        The size (in bytes) of the file. This information is available for all Cisco distributed images and files imported to the local repository.  

        :return: The size of this SoftwarerepositoryOperatingSystemFile.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this SoftwarerepositoryOperatingSystemFile.
        The size (in bytes) of the file. This information is available for all Cisco distributed images and files imported to the local repository.  

        :param size: The size of this SoftwarerepositoryOperatingSystemFile.
        :type: int
        """

        self._size = size

    @property
    def software_advisory_url(self):
        """
        Gets the software_advisory_url of this SoftwarerepositoryOperatingSystemFile.
        The software advisory, if any, provided by the vendor for this file.  

        :return: The software_advisory_url of this SoftwarerepositoryOperatingSystemFile.
        :rtype: str
        """
        return self._software_advisory_url

    @software_advisory_url.setter
    def software_advisory_url(self, software_advisory_url):
        """
        Sets the software_advisory_url of this SoftwarerepositoryOperatingSystemFile.
        The software advisory, if any, provided by the vendor for this file.  

        :param software_advisory_url: The software_advisory_url of this SoftwarerepositoryOperatingSystemFile.
        :type: str
        """

        self._software_advisory_url = software_advisory_url

    @property
    def source(self):
        """
        Gets the source of this SoftwarerepositoryOperatingSystemFile.
        Location of the file in an external repository.   

        :return: The source of this SoftwarerepositoryOperatingSystemFile.
        :rtype: SoftwarerepositoryFileServer
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this SoftwarerepositoryOperatingSystemFile.
        Location of the file in an external repository.   

        :param source: The source of this SoftwarerepositoryOperatingSystemFile.
        :type: SoftwarerepositoryFileServer
        """

        self._source = source

    @property
    def version(self):
        """
        Gets the version of this SoftwarerepositoryOperatingSystemFile.
        Vendor provided version for the file.   

        :return: The version of this SoftwarerepositoryOperatingSystemFile.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this SoftwarerepositoryOperatingSystemFile.
        Vendor provided version for the file.   

        :param version: The version of this SoftwarerepositoryOperatingSystemFile.
        :type: str
        """

        self._version = version

    @property
    def catalog(self):
        """
        Gets the catalog of this SoftwarerepositoryOperatingSystemFile.
        The catalog where this image is present. 

        :return: The catalog of this SoftwarerepositoryOperatingSystemFile.
        :rtype: SoftwarerepositoryCatalogRef
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        """
        Sets the catalog of this SoftwarerepositoryOperatingSystemFile.
        The catalog where this image is present. 

        :param catalog: The catalog of this SoftwarerepositoryOperatingSystemFile.
        :type: SoftwarerepositoryCatalogRef
        """

        self._catalog = catalog

    @property
    def vendor(self):
        """
        Gets the vendor of this SoftwarerepositoryOperatingSystemFile.
        The vendor or publisher of this file.   

        :return: The vendor of this SoftwarerepositoryOperatingSystemFile.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this SoftwarerepositoryOperatingSystemFile.
        The vendor or publisher of this file.   

        :param vendor: The vendor of this SoftwarerepositoryOperatingSystemFile.
        :type: str
        """

        self._vendor = vendor

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
        if not isinstance(other, SoftwarerepositoryOperatingSystemFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
