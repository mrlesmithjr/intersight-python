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


class WorkflowWorkflowDefinitionAllOf(object):
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
        'default_version': 'bool',
        'description': 'str',
        'input_definition': 'list[WorkflowBaseDataType]',
        'label': 'str',
        'license_entitlement': 'str',
        'name': 'str',
        'output_definition': 'list[WorkflowBaseDataType]',
        'output_parameters': 'object',
        'tasks': 'list[WorkflowWorkflowTask]',
        'ui_rendering_data': 'object',
        'validation_information': 'WorkflowValidationInformation',
        'version': 'int',
        'catalog': 'WorkflowCatalog'
    }

    attribute_map = {
        'default_version': 'DefaultVersion',
        'description': 'Description',
        'input_definition': 'InputDefinition',
        'label': 'Label',
        'license_entitlement': 'LicenseEntitlement',
        'name': 'Name',
        'output_definition': 'OutputDefinition',
        'output_parameters': 'OutputParameters',
        'tasks': 'Tasks',
        'ui_rendering_data': 'UiRenderingData',
        'validation_information': 'ValidationInformation',
        'version': 'Version',
        'catalog': 'Catalog'
    }

    def __init__(self,
                 default_version=None,
                 description=None,
                 input_definition=None,
                 label=None,
                 license_entitlement='Base',
                 name=None,
                 output_definition=None,
                 output_parameters=None,
                 tasks=None,
                 ui_rendering_data=None,
                 validation_information=None,
                 version=None,
                 catalog=None,
                 local_vars_configuration=None):  # noqa: E501
        """WorkflowWorkflowDefinitionAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._default_version = None
        self._description = None
        self._input_definition = None
        self._label = None
        self._license_entitlement = None
        self._name = None
        self._output_definition = None
        self._output_parameters = None
        self._tasks = None
        self._ui_rendering_data = None
        self._validation_information = None
        self._version = None
        self._catalog = None
        self.discriminator = None

        if default_version is not None:
            self.default_version = default_version
        if description is not None:
            self.description = description
        if input_definition is not None:
            self.input_definition = input_definition
        if label is not None:
            self.label = label
        if license_entitlement is not None:
            self.license_entitlement = license_entitlement
        if name is not None:
            self.name = name
        if output_definition is not None:
            self.output_definition = output_definition
        if output_parameters is not None:
            self.output_parameters = output_parameters
        if tasks is not None:
            self.tasks = tasks
        if ui_rendering_data is not None:
            self.ui_rendering_data = ui_rendering_data
        if validation_information is not None:
            self.validation_information = validation_information
        if version is not None:
            self.version = version
        if catalog is not None:
            self.catalog = catalog

    @property
    def default_version(self):
        """Gets the default_version of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501

        When true this will be the workflow version that is used when a specific workflow definition version is not specified. The default version is used when user executes a workflow without specifying a version or when workflow is included in another workflow without a specific version. The very first workflow definition created with a name will be set as the default version, after that user can explicitly set any version of the workflow definition as the default version.    # noqa: E501

        :return: The default_version of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._default_version

    @default_version.setter
    def default_version(self, default_version):
        """Sets the default_version of this WorkflowWorkflowDefinitionAllOf.

        When true this will be the workflow version that is used when a specific workflow definition version is not specified. The default version is used when user executes a workflow without specifying a version or when workflow is included in another workflow without a specific version. The very first workflow definition created with a name will be set as the default version, after that user can explicitly set any version of the workflow definition as the default version.    # noqa: E501

        :param default_version: The default_version of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :type: bool
        """

        self._default_version = default_version

    @property
    def description(self):
        """Gets the description of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501

        The description for this workflow.    # noqa: E501

        :return: The description of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WorkflowWorkflowDefinitionAllOf.

        The description for this workflow.    # noqa: E501

        :param description: The description of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def input_definition(self):
        """Gets the input_definition of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501


        :return: The input_definition of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :rtype: list[WorkflowBaseDataType]
        """
        return self._input_definition

    @input_definition.setter
    def input_definition(self, input_definition):
        """Sets the input_definition of this WorkflowWorkflowDefinitionAllOf.


        :param input_definition: The input_definition of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :type: list[WorkflowBaseDataType]
        """

        self._input_definition = input_definition

    @property
    def label(self):
        """Gets the label of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501

        A user friendly short name to identify the workflow.    # noqa: E501

        :return: The label of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this WorkflowWorkflowDefinitionAllOf.

        A user friendly short name to identify the workflow.    # noqa: E501

        :param label: The label of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def license_entitlement(self):
        """Gets the license_entitlement of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501

        License entitlement required to run this workflow. It is calculated based on the highest license requirement of all its tasks.    # noqa: E501

        :return: The license_entitlement of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._license_entitlement

    @license_entitlement.setter
    def license_entitlement(self, license_entitlement):
        """Sets the license_entitlement of this WorkflowWorkflowDefinitionAllOf.

        License entitlement required to run this workflow. It is calculated based on the highest license requirement of all its tasks.    # noqa: E501

        :param license_entitlement: The license_entitlement of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["Base", "Essential", "Standard",
                          "Advantage"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and license_entitlement not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `license_entitlement` ({0}), must be one of {1}"  # noqa: E501
                .format(license_entitlement, allowed_values))

        self._license_entitlement = license_entitlement

    @property
    def name(self):
        """Gets the name of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501

        The name for this workflow. You can have multiple version of the workflow with the same name.    # noqa: E501

        :return: The name of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowWorkflowDefinitionAllOf.

        The name for this workflow. You can have multiple version of the workflow with the same name.    # noqa: E501

        :param name: The name of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def output_definition(self):
        """Gets the output_definition of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501


        :return: The output_definition of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :rtype: list[WorkflowBaseDataType]
        """
        return self._output_definition

    @output_definition.setter
    def output_definition(self, output_definition):
        """Sets the output_definition of this WorkflowWorkflowDefinitionAllOf.


        :param output_definition: The output_definition of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :type: list[WorkflowBaseDataType]
        """

        self._output_definition = output_definition

    @property
    def output_parameters(self):
        """Gets the output_parameters of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501

        The output mappings for the workflow. The outputs for worflows will generally be task output variables that we want to export out at the end of the workflow. The format to specify the mapping is '${Source.output.JsonPath}'. 'Source' is the name of the task within the workflow. You can map any task output to a workflow output as long as the types are compatible. Following this is JSON path expression to extract JSON fragment from source's output.    # noqa: E501

        :return: The output_parameters of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :rtype: object
        """
        return self._output_parameters

    @output_parameters.setter
    def output_parameters(self, output_parameters):
        """Sets the output_parameters of this WorkflowWorkflowDefinitionAllOf.

        The output mappings for the workflow. The outputs for worflows will generally be task output variables that we want to export out at the end of the workflow. The format to specify the mapping is '${Source.output.JsonPath}'. 'Source' is the name of the task within the workflow. You can map any task output to a workflow output as long as the types are compatible. Following this is JSON path expression to extract JSON fragment from source's output.    # noqa: E501

        :param output_parameters: The output_parameters of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :type: object
        """

        self._output_parameters = output_parameters

    @property
    def tasks(self):
        """Gets the tasks of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501


        :return: The tasks of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :rtype: list[WorkflowWorkflowTask]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this WorkflowWorkflowDefinitionAllOf.


        :param tasks: The tasks of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :type: list[WorkflowWorkflowTask]
        """

        self._tasks = tasks

    @property
    def ui_rendering_data(self):
        """Gets the ui_rendering_data of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501

        This will hold the data needed for workflow to be rendered in the user interface.    # noqa: E501

        :return: The ui_rendering_data of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :rtype: object
        """
        return self._ui_rendering_data

    @ui_rendering_data.setter
    def ui_rendering_data(self, ui_rendering_data):
        """Sets the ui_rendering_data of this WorkflowWorkflowDefinitionAllOf.

        This will hold the data needed for workflow to be rendered in the user interface.    # noqa: E501

        :param ui_rendering_data: The ui_rendering_data of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :type: object
        """

        self._ui_rendering_data = ui_rendering_data

    @property
    def validation_information(self):
        """Gets the validation_information of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501


        :return: The validation_information of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :rtype: WorkflowValidationInformation
        """
        return self._validation_information

    @validation_information.setter
    def validation_information(self, validation_information):
        """Sets the validation_information of this WorkflowWorkflowDefinitionAllOf.


        :param validation_information: The validation_information of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :type: WorkflowValidationInformation
        """

        self._validation_information = validation_information

    @property
    def version(self):
        """Gets the version of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501

        The version of the workflow to support multiple versions.     # noqa: E501

        :return: The version of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this WorkflowWorkflowDefinitionAllOf.

        The version of the workflow to support multiple versions.     # noqa: E501

        :param version: The version of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def catalog(self):
        """Gets the catalog of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501


        :return: The catalog of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :rtype: WorkflowCatalog
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        """Sets the catalog of this WorkflowWorkflowDefinitionAllOf.


        :param catalog: The catalog of this WorkflowWorkflowDefinitionAllOf.  # noqa: E501
        :type: WorkflowCatalog
        """

        self._catalog = catalog

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
        if not isinstance(other, WorkflowWorkflowDefinitionAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WorkflowWorkflowDefinitionAllOf):
            return True

        return self.to_dict() != other.to_dict()
