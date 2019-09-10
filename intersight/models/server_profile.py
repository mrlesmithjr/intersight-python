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


class ServerProfile(object):
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
        'src_template': 'PolicyAbstractProfileRef',
        'type': 'str',
        'action': 'str',
        'config_context': 'PolicyConfigContext',
        'assigned_server': 'ComputeRackUnitRef',
        'associated_server': 'ComputeRackUnitRef',
        'config_change_details': 'list[ServerConfigChangeDetailRef]',
        'config_changes': 'PolicyConfigChange',
        'config_result': 'ServerConfigResultRef',
        'organization': 'IamAccountRef',
        'running_workflows': 'list[WorkflowWorkflowInfoRef]'
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
        'src_template': 'SrcTemplate',
        'type': 'Type',
        'action': 'Action',
        'config_context': 'ConfigContext',
        'assigned_server': 'AssignedServer',
        'associated_server': 'AssociatedServer',
        'config_change_details': 'ConfigChangeDetails',
        'config_changes': 'ConfigChanges',
        'config_result': 'ConfigResult',
        'organization': 'Organization',
        'running_workflows': 'RunningWorkflows'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, shared_scope=None, tags=None, version_context=None, description=None, name=None, src_template=None, type='instance', action=None, config_context=None, assigned_server=None, associated_server=None, config_change_details=None, config_changes=None, config_result=None, organization=None, running_workflows=None):
        """
        ServerProfile - a model defined in Swagger
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
        self._src_template = None
        self._type = None
        self._action = None
        self._config_context = None
        self._assigned_server = None
        self._associated_server = None
        self._config_change_details = None
        self._config_changes = None
        self._config_result = None
        self._organization = None
        self._running_workflows = None

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
        if src_template is not None:
          self.src_template = src_template
        if type is not None:
          self.type = type
        if action is not None:
          self.action = action
        if config_context is not None:
          self.config_context = config_context
        if assigned_server is not None:
          self.assigned_server = assigned_server
        if associated_server is not None:
          self.associated_server = associated_server
        if config_change_details is not None:
          self.config_change_details = config_change_details
        if config_changes is not None:
          self.config_changes = config_changes
        if config_result is not None:
          self.config_result = config_result
        if organization is not None:
          self.organization = organization
        if running_workflows is not None:
          self.running_workflows = running_workflows

    @property
    def account_moid(self):
        """
        Gets the account_moid of this ServerProfile.
        The Account ID for this managed object.  

        :return: The account_moid of this ServerProfile.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this ServerProfile.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this ServerProfile.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this ServerProfile.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this ServerProfile.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this ServerProfile.
        The array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this ServerProfile.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this ServerProfile.
        The time when this managed object was created.  

        :return: The create_time of this ServerProfile.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this ServerProfile.
        The time when this managed object was created.  

        :param create_time: The create_time of this ServerProfile.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this ServerProfile.
        The DomainGroup ID for this managed object.  

        :return: The domain_group_moid of this ServerProfile.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this ServerProfile.
        The DomainGroup ID for this managed object.  

        :param domain_group_moid: The domain_group_moid of this ServerProfile.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this ServerProfile.
        The time when this managed object was last modified.  

        :return: The mod_time of this ServerProfile.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this ServerProfile.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this ServerProfile.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this ServerProfile.
        The unique identifier of this Managed Object instance.  

        :return: The moid of this ServerProfile.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this ServerProfile.
        The unique identifier of this Managed Object instance.  

        :param moid: The moid of this ServerProfile.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this ServerProfile.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this ServerProfile.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this ServerProfile.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this ServerProfile.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this ServerProfile.
        The array of owners which represent effective ownership of this object.   

        :return: The owners of this ServerProfile.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this ServerProfile.
        The array of owners which represent effective ownership of this object.   

        :param owners: The owners of this ServerProfile.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this ServerProfile.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this ServerProfile.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this ServerProfile.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this ServerProfile.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this ServerProfile.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :return: The shared_scope of this ServerProfile.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this ServerProfile.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.  

        :param shared_scope: The shared_scope of this ServerProfile.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this ServerProfile.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :return: The tags of this ServerProfile.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ServerProfile.
        The array of tags, which allow to add key, value meta-data to managed objects.  

        :param tags: The tags of this ServerProfile.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this ServerProfile.
        The versioning info for this managed object.   

        :return: The version_context of this ServerProfile.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this ServerProfile.
        The versioning info for this managed object.   

        :param version_context: The version_context of this ServerProfile.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def description(self):
        """
        Gets the description of this ServerProfile.
        Description of the profile.  

        :return: The description of this ServerProfile.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ServerProfile.
        Description of the profile.  

        :param description: The description of this ServerProfile.
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """
        Gets the name of this ServerProfile.
        Name of the concrete profile.  

        :return: The name of this ServerProfile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ServerProfile.
        Name of the concrete profile.  

        :param name: The name of this ServerProfile.
        :type: str
        """

        self._name = name

    @property
    def src_template(self):
        """
        Gets the src_template of this ServerProfile.
        The source profile template to apply to the profile instance. All configuration settings from the profile template will be applied to the profile instance. 

        :return: The src_template of this ServerProfile.
        :rtype: PolicyAbstractProfileRef
        """
        return self._src_template

    @src_template.setter
    def src_template(self, src_template):
        """
        Sets the src_template of this ServerProfile.
        The source profile template to apply to the profile instance. All configuration settings from the profile template will be applied to the profile instance. 

        :param src_template: The src_template of this ServerProfile.
        :type: PolicyAbstractProfileRef
        """

        self._src_template = src_template

    @property
    def type(self):
        """
        Gets the type of this ServerProfile.
        Defines the type of the profile. Accepted value is instance.   

        :return: The type of this ServerProfile.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ServerProfile.
        Defines the type of the profile. Accepted value is instance.   

        :param type: The type of this ServerProfile.
        :type: str
        """
        allowed_values = ["instance"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def action(self):
        """
        Gets the action of this ServerProfile.
        User initiated action. Each profile type has its own supported actions. For HyperFlex cluster profile, the supported actions are -- Validate, Deploy, Continue, Retry, Abort, Unassign For server profile, the support actions are -- Deploy, Unassign.  

        :return: The action of this ServerProfile.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ServerProfile.
        User initiated action. Each profile type has its own supported actions. For HyperFlex cluster profile, the supported actions are -- Validate, Deploy, Continue, Retry, Abort, Unassign For server profile, the support actions are -- Deploy, Unassign.  

        :param action: The action of this ServerProfile.
        :type: str
        """

        self._action = action

    @property
    def config_context(self):
        """
        Gets the config_context of this ServerProfile.
        The configuration state and results of the last configuration operation.   

        :return: The config_context of this ServerProfile.
        :rtype: PolicyConfigContext
        """
        return self._config_context

    @config_context.setter
    def config_context(self, config_context):
        """
        Sets the config_context of this ServerProfile.
        The configuration state and results of the last configuration operation.   

        :param config_context: The config_context of this ServerProfile.
        :type: PolicyConfigContext
        """

        self._config_context = config_context

    @property
    def assigned_server(self):
        """
        Gets the assigned_server of this ServerProfile.
        The assigned physical server to the profile. A physical server can be assigned to more than one server profiles as long as it is only associated with one. 

        :return: The assigned_server of this ServerProfile.
        :rtype: ComputeRackUnitRef
        """
        return self._assigned_server

    @assigned_server.setter
    def assigned_server(self, assigned_server):
        """
        Sets the assigned_server of this ServerProfile.
        The assigned physical server to the profile. A physical server can be assigned to more than one server profiles as long as it is only associated with one. 

        :param assigned_server: The assigned_server of this ServerProfile.
        :type: ComputeRackUnitRef
        """

        self._assigned_server = assigned_server

    @property
    def associated_server(self):
        """
        Gets the associated_server of this ServerProfile.
        The associated physical server to the profile. A physical server can only be associated to one server profiles. 

        :return: The associated_server of this ServerProfile.
        :rtype: ComputeRackUnitRef
        """
        return self._associated_server

    @associated_server.setter
    def associated_server(self, associated_server):
        """
        Sets the associated_server of this ServerProfile.
        The associated physical server to the profile. A physical server can only be associated to one server profiles. 

        :param associated_server: The associated_server of this ServerProfile.
        :type: ComputeRackUnitRef
        """

        self._associated_server = associated_server

    @property
    def config_change_details(self):
        """
        Gets the config_change_details of this ServerProfile.
        The configuration change details are captured here. 

        :return: The config_change_details of this ServerProfile.
        :rtype: list[ServerConfigChangeDetailRef]
        """
        return self._config_change_details

    @config_change_details.setter
    def config_change_details(self, config_change_details):
        """
        Sets the config_change_details of this ServerProfile.
        The configuration change details are captured here. 

        :param config_change_details: The config_change_details of this ServerProfile.
        :type: list[ServerConfigChangeDetailRef]
        """

        self._config_change_details = config_change_details

    @property
    def config_changes(self):
        """
        Gets the config_changes of this ServerProfile.
        Pending configuration changes at the summary level. Detail changes are saved in configChangeDetails as a separate object.   

        :return: The config_changes of this ServerProfile.
        :rtype: PolicyConfigChange
        """
        return self._config_changes

    @config_changes.setter
    def config_changes(self, config_changes):
        """
        Sets the config_changes of this ServerProfile.
        Pending configuration changes at the summary level. Detail changes are saved in configChangeDetails as a separate object.   

        :param config_changes: The config_changes of this ServerProfile.
        :type: PolicyConfigChange
        """

        self._config_changes = config_changes

    @property
    def config_result(self):
        """
        Gets the config_result of this ServerProfile.
        The configuration results including deploy, undeploy and compliance-check results. The errors usually are detected and reported during the apply/deploy phases. 

        :return: The config_result of this ServerProfile.
        :rtype: ServerConfigResultRef
        """
        return self._config_result

    @config_result.setter
    def config_result(self, config_result):
        """
        Sets the config_result of this ServerProfile.
        The configuration results including deploy, undeploy and compliance-check results. The errors usually are detected and reported during the apply/deploy phases. 

        :param config_result: The config_result of this ServerProfile.
        :type: ServerConfigResultRef
        """

        self._config_result = config_result

    @property
    def organization(self):
        """
        Gets the organization of this ServerProfile.
        Relationship to the Organization that owns the Managed Object. 

        :return: The organization of this ServerProfile.
        :rtype: IamAccountRef
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """
        Sets the organization of this ServerProfile.
        Relationship to the Organization that owns the Managed Object. 

        :param organization: The organization of this ServerProfile.
        :type: IamAccountRef
        """

        self._organization = organization

    @property
    def running_workflows(self):
        """
        Gets the running_workflows of this ServerProfile.
        The WorkflowInfos in the workflow engine that are running for this server Profile. 

        :return: The running_workflows of this ServerProfile.
        :rtype: list[WorkflowWorkflowInfoRef]
        """
        return self._running_workflows

    @running_workflows.setter
    def running_workflows(self, running_workflows):
        """
        Sets the running_workflows of this ServerProfile.
        The WorkflowInfos in the workflow engine that are running for this server Profile. 

        :param running_workflows: The running_workflows of this ServerProfile.
        :type: list[WorkflowWorkflowInfoRef]
        """

        self._running_workflows = running_workflows

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
        if not isinstance(other, ServerProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
