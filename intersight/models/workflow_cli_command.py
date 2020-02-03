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


class WorkflowCliCommand(object):
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
        'body': 'str',
        'content_type': 'str',
        'name': 'str',
        'outcomes': 'object',
        'response_spec': 'ContentGrammar',
        'skip_on_condition': 'str',
        'timeout': 'int',
        'command': 'str',
        'end_prompt': 'str',
        'expect_prompts': 'list[WorkflowExpectPrompt]',
        'skip_status_check': 'bool',
        'terminal_end': 'bool',
        'terminal_start': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'body': 'Body',
        'content_type': 'ContentType',
        'name': 'Name',
        'outcomes': 'Outcomes',
        'response_spec': 'ResponseSpec',
        'skip_on_condition': 'SkipOnCondition',
        'timeout': 'Timeout',
        'command': 'Command',
        'end_prompt': 'EndPrompt',
        'expect_prompts': 'ExpectPrompts',
        'skip_status_check': 'SkipStatusCheck',
        'terminal_end': 'TerminalEnd',
        'terminal_start': 'TerminalStart',
        'type': 'Type'
    }

    def __init__(self, object_type=None, body=None, content_type='json', name=None, outcomes=None, response_spec=None, skip_on_condition=None, timeout=None, command=None, end_prompt=None, expect_prompts=None, skip_status_check=None, terminal_end=None, terminal_start=None, type='NonInteractive'):
        """
        WorkflowCliCommand - a model defined in Swagger
        """

        self._object_type = None
        self._body = None
        self._content_type = None
        self._name = None
        self._outcomes = None
        self._response_spec = None
        self._skip_on_condition = None
        self._timeout = None
        self._command = None
        self._end_prompt = None
        self._expect_prompts = None
        self._skip_status_check = None
        self._terminal_end = None
        self._terminal_start = None
        self._type = None

        if object_type is not None:
          self.object_type = object_type
        if body is not None:
          self.body = body
        if content_type is not None:
          self.content_type = content_type
        if name is not None:
          self.name = name
        if outcomes is not None:
          self.outcomes = outcomes
        if response_spec is not None:
          self.response_spec = response_spec
        if skip_on_condition is not None:
          self.skip_on_condition = skip_on_condition
        if timeout is not None:
          self.timeout = timeout
        if command is not None:
          self.command = command
        if end_prompt is not None:
          self.end_prompt = end_prompt
        if expect_prompts is not None:
          self.expect_prompts = expect_prompts
        if skip_status_check is not None:
          self.skip_status_check = skip_status_check
        if terminal_end is not None:
          self.terminal_end = terminal_end
        if terminal_start is not None:
          self.terminal_start = terminal_start
        if type is not None:
          self.type = type

    @property
    def object_type(self):
        """
        Gets the object_type of this WorkflowCliCommand.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this WorkflowCliCommand.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this WorkflowCliCommand.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this WorkflowCliCommand.
        :type: str
        """

        self._object_type = object_type

    @property
    def body(self):
        """
        Gets the body of this WorkflowCliCommand.
        The optional request body that is sent as part of this API request.  The request body can contain a golang template that can be populated with task input parameters and previous API output parameters.   

        :return: The body of this WorkflowCliCommand.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this WorkflowCliCommand.
        The optional request body that is sent as part of this API request.  The request body can contain a golang template that can be populated with task input parameters and previous API output parameters.   

        :param body: The body of this WorkflowCliCommand.
        :type: str
        """

        self._body = body

    @property
    def content_type(self):
        """
        Gets the content_type of this WorkflowCliCommand.
        Intersight Orchestrator, with the support of response parser specification, can extract the values from API responses and map them to task output parameters. The value extraction is supported for response content types XML and JSON.  The type of the content that gets passed as payload and response in this API.   

        :return: The content_type of this WorkflowCliCommand.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this WorkflowCliCommand.
        Intersight Orchestrator, with the support of response parser specification, can extract the values from API responses and map them to task output parameters. The value extraction is supported for response content types XML and JSON.  The type of the content that gets passed as payload and response in this API.   

        :param content_type: The content_type of this WorkflowCliCommand.
        :type: str
        """
        allowed_values = ["json", "xml", "text"]
        if content_type not in allowed_values:
            raise ValueError(
                "Invalid value for `content_type` ({0}), must be one of {1}"
                .format(content_type, allowed_values)
            )

        self._content_type = content_type

    @property
    def name(self):
        """
        Gets the name of this WorkflowCliCommand.
        A reference name for this API request within the batch API request.  This name shall be used to map the API output parameters to subsequent API input parameters within a batch API task.   

        :return: The name of this WorkflowCliCommand.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WorkflowCliCommand.
        A reference name for this API request within the batch API request.  This name shall be used to map the API output parameters to subsequent API input parameters within a batch API task.   

        :param name: The name of this WorkflowCliCommand.
        :type: str
        """

        self._name = name

    @property
    def outcomes(self):
        """
        Gets the outcomes of this WorkflowCliCommand.
        All the possible outcomes of this API are captured here. Outcomes property is a collection property of type workflow.Outcome objects.  The outcomes can be mapped to the message to be shown. The outcomes are evaluated in the order they are given. At the end of the outcomes list, an catchall success/fail outcome can be added with condition as 'true'.  This is an optional property and if not specified the task will be marked as success.   

        :return: The outcomes of this WorkflowCliCommand.
        :rtype: object
        """
        return self._outcomes

    @outcomes.setter
    def outcomes(self, outcomes):
        """
        Sets the outcomes of this WorkflowCliCommand.
        All the possible outcomes of this API are captured here. Outcomes property is a collection property of type workflow.Outcome objects.  The outcomes can be mapped to the message to be shown. The outcomes are evaluated in the order they are given. At the end of the outcomes list, an catchall success/fail outcome can be added with condition as 'true'.  This is an optional property and if not specified the task will be marked as success.   

        :param outcomes: The outcomes of this WorkflowCliCommand.
        :type: object
        """

        self._outcomes = outcomes

    @property
    def response_spec(self):
        """
        Gets the response_spec of this WorkflowCliCommand.
        The optional grammar specification for parsing the response to extract the required values.  The specification should have extraction specification specified for all the API output parameters.   

        :return: The response_spec of this WorkflowCliCommand.
        :rtype: ContentGrammar
        """
        return self._response_spec

    @response_spec.setter
    def response_spec(self, response_spec):
        """
        Sets the response_spec of this WorkflowCliCommand.
        The optional grammar specification for parsing the response to extract the required values.  The specification should have extraction specification specified for all the API output parameters.   

        :param response_spec: The response_spec of this WorkflowCliCommand.
        :type: ContentGrammar
        """

        self._response_spec = response_spec

    @property
    def skip_on_condition(self):
        """
        Gets the skip_on_condition of this WorkflowCliCommand.
        The skip expression, if provided, allows the batch API executor to skip the api execution when the given expression evaluates to true.  The expression is given as such a golang template that has to be evaluated to a final content true/false. The expression is an optional and in case not provided, the API will always be executed.   

        :return: The skip_on_condition of this WorkflowCliCommand.
        :rtype: str
        """
        return self._skip_on_condition

    @skip_on_condition.setter
    def skip_on_condition(self, skip_on_condition):
        """
        Sets the skip_on_condition of this WorkflowCliCommand.
        The skip expression, if provided, allows the batch API executor to skip the api execution when the given expression evaluates to true.  The expression is given as such a golang template that has to be evaluated to a final content true/false. The expression is an optional and in case not provided, the API will always be executed.   

        :param skip_on_condition: The skip_on_condition of this WorkflowCliCommand.
        :type: str
        """

        self._skip_on_condition = skip_on_condition

    @property
    def timeout(self):
        """
        Gets the timeout of this WorkflowCliCommand.
        The duration in seconds by which the API response is expected from the API target.  If the end point does not respond for the API request within this timeout duration, the task will be marked as failed.    

        :return: The timeout of this WorkflowCliCommand.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """
        Sets the timeout of this WorkflowCliCommand.
        The duration in seconds by which the API response is expected from the API target.  If the end point does not respond for the API request within this timeout duration, the task will be marked as failed.    

        :param timeout: The timeout of this WorkflowCliCommand.
        :type: int
        """

        self._timeout = timeout

    @property
    def command(self):
        """
        Gets the command of this WorkflowCliCommand.
        The command to run on the device connector.   

        :return: The command of this WorkflowCliCommand.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """
        Sets the command of this WorkflowCliCommand.
        The command to run on the device connector.   

        :param command: The command of this WorkflowCliCommand.
        :type: str
        """

        self._command = command

    @property
    def end_prompt(self):
        """
        Gets the end_prompt of this WorkflowCliCommand.
        The regex string that identifies the end of the command response.   

        :return: The end_prompt of this WorkflowCliCommand.
        :rtype: str
        """
        return self._end_prompt

    @end_prompt.setter
    def end_prompt(self, end_prompt):
        """
        Sets the end_prompt of this WorkflowCliCommand.
        The regex string that identifies the end of the command response.   

        :param end_prompt: The end_prompt of this WorkflowCliCommand.
        :type: str
        """

        self._end_prompt = end_prompt

    @property
    def expect_prompts(self):
        """
        Gets the expect_prompts of this WorkflowCliCommand.
        Cli prompts required as part of interactive command execution. For e.g. login credentials will be part of prompts which are provided as list of expect prompt regex and corresponding answer string.   

        :return: The expect_prompts of this WorkflowCliCommand.
        :rtype: list[WorkflowExpectPrompt]
        """
        return self._expect_prompts

    @expect_prompts.setter
    def expect_prompts(self, expect_prompts):
        """
        Sets the expect_prompts of this WorkflowCliCommand.
        Cli prompts required as part of interactive command execution. For e.g. login credentials will be part of prompts which are provided as list of expect prompt regex and corresponding answer string.   

        :param expect_prompts: The expect_prompts of this WorkflowCliCommand.
        :type: list[WorkflowExpectPrompt]
        """

        self._expect_prompts = expect_prompts

    @property
    def skip_status_check(self):
        """
        Gets the skip_status_check of this WorkflowCliCommand.
        Skips the execution status check of the terminal command. One use case for this is while exiting the terminal session from esxi host.   

        :return: The skip_status_check of this WorkflowCliCommand.
        :rtype: bool
        """
        return self._skip_status_check

    @skip_status_check.setter
    def skip_status_check(self, skip_status_check):
        """
        Sets the skip_status_check of this WorkflowCliCommand.
        Skips the execution status check of the terminal command. One use case for this is while exiting the terminal session from esxi host.   

        :param skip_status_check: The skip_status_check of this WorkflowCliCommand.
        :type: bool
        """

        self._skip_status_check = skip_status_check

    @property
    def terminal_end(self):
        """
        Gets the terminal_end of this WorkflowCliCommand.
        If this flag is set, it marks the end of the terminal session where the previous commands were executed.   

        :return: The terminal_end of this WorkflowCliCommand.
        :rtype: bool
        """
        return self._terminal_end

    @terminal_end.setter
    def terminal_end(self, terminal_end):
        """
        Sets the terminal_end of this WorkflowCliCommand.
        If this flag is set, it marks the end of the terminal session where the previous commands were executed.   

        :param terminal_end: The terminal_end of this WorkflowCliCommand.
        :type: bool
        """

        self._terminal_end = terminal_end

    @property
    def terminal_start(self):
        """
        Gets the terminal_start of this WorkflowCliCommand.
        If this flag is set, the execution of this command initiates a terminal session in which the subsequent CLI commands are executed until a command with terminalEnd flag is encountered or the end of the batch.   

        :return: The terminal_start of this WorkflowCliCommand.
        :rtype: bool
        """
        return self._terminal_start

    @terminal_start.setter
    def terminal_start(self, terminal_start):
        """
        Sets the terminal_start of this WorkflowCliCommand.
        If this flag is set, the execution of this command initiates a terminal session in which the subsequent CLI commands are executed until a command with terminalEnd flag is encountered or the end of the batch.   

        :param terminal_start: The terminal_start of this WorkflowCliCommand.
        :type: bool
        """

        self._terminal_start = terminal_start

    @property
    def type(self):
        """
        Gets the type of this WorkflowCliCommand.
        The type of the command - can be interactive or non-interactive.    

        :return: The type of this WorkflowCliCommand.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this WorkflowCliCommand.
        The type of the command - can be interactive or non-interactive.    

        :param type: The type of this WorkflowCliCommand.
        :type: str
        """
        allowed_values = ["NonInteractive", "Interactive"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, WorkflowCliCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
