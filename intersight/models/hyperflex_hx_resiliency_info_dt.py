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


class HyperflexHxResiliencyInfoDt(object):
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
        'data_replication_factor': 'str',
        'hdd_failures_tolerable': 'int',
        'messages': 'list[str]',
        'node_failures_tolerable': 'int',
        'policy_compliance': 'str',
        'resiliency_state': 'str',
        'ssd_failures_tolerable': 'int'
    }

    attribute_map = {
        'data_replication_factor': 'DataReplicationFactor',
        'hdd_failures_tolerable': 'HddFailuresTolerable',
        'messages': 'Messages',
        'node_failures_tolerable': 'NodeFailuresTolerable',
        'policy_compliance': 'PolicyCompliance',
        'resiliency_state': 'ResiliencyState',
        'ssd_failures_tolerable': 'SsdFailuresTolerable'
    }

    def __init__(self, data_replication_factor='ONE_COPY', hdd_failures_tolerable=None, messages=None, node_failures_tolerable=None, policy_compliance='UNKNOWN', resiliency_state='UNKNOWN', ssd_failures_tolerable=None):
        """
        HyperflexHxResiliencyInfoDt - a model defined in Swagger
        """

        self._data_replication_factor = None
        self._hdd_failures_tolerable = None
        self._messages = None
        self._node_failures_tolerable = None
        self._policy_compliance = None
        self._resiliency_state = None
        self._ssd_failures_tolerable = None

        if data_replication_factor is not None:
          self.data_replication_factor = data_replication_factor
        if hdd_failures_tolerable is not None:
          self.hdd_failures_tolerable = hdd_failures_tolerable
        if messages is not None:
          self.messages = messages
        if node_failures_tolerable is not None:
          self.node_failures_tolerable = node_failures_tolerable
        if policy_compliance is not None:
          self.policy_compliance = policy_compliance
        if resiliency_state is not None:
          self.resiliency_state = resiliency_state
        if ssd_failures_tolerable is not None:
          self.ssd_failures_tolerable = ssd_failures_tolerable

    @property
    def data_replication_factor(self):
        """
        Gets the data_replication_factor of this HyperflexHxResiliencyInfoDt.

        :return: The data_replication_factor of this HyperflexHxResiliencyInfoDt.
        :rtype: str
        """
        return self._data_replication_factor

    @data_replication_factor.setter
    def data_replication_factor(self, data_replication_factor):
        """
        Sets the data_replication_factor of this HyperflexHxResiliencyInfoDt.

        :param data_replication_factor: The data_replication_factor of this HyperflexHxResiliencyInfoDt.
        :type: str
        """
        allowed_values = ["ONE_COPY", "TWO_COPIES", "THREE_COPIES", "FOUR_COPIES", "SIX_COPIES"]
        if data_replication_factor not in allowed_values:
            raise ValueError(
                "Invalid value for `data_replication_factor` ({0}), must be one of {1}"
                .format(data_replication_factor, allowed_values)
            )

        self._data_replication_factor = data_replication_factor

    @property
    def hdd_failures_tolerable(self):
        """
        Gets the hdd_failures_tolerable of this HyperflexHxResiliencyInfoDt.

        :return: The hdd_failures_tolerable of this HyperflexHxResiliencyInfoDt.
        :rtype: int
        """
        return self._hdd_failures_tolerable

    @hdd_failures_tolerable.setter
    def hdd_failures_tolerable(self, hdd_failures_tolerable):
        """
        Sets the hdd_failures_tolerable of this HyperflexHxResiliencyInfoDt.

        :param hdd_failures_tolerable: The hdd_failures_tolerable of this HyperflexHxResiliencyInfoDt.
        :type: int
        """

        self._hdd_failures_tolerable = hdd_failures_tolerable

    @property
    def messages(self):
        """
        Gets the messages of this HyperflexHxResiliencyInfoDt.

        :return: The messages of this HyperflexHxResiliencyInfoDt.
        :rtype: list[str]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """
        Sets the messages of this HyperflexHxResiliencyInfoDt.

        :param messages: The messages of this HyperflexHxResiliencyInfoDt.
        :type: list[str]
        """

        self._messages = messages

    @property
    def node_failures_tolerable(self):
        """
        Gets the node_failures_tolerable of this HyperflexHxResiliencyInfoDt.

        :return: The node_failures_tolerable of this HyperflexHxResiliencyInfoDt.
        :rtype: int
        """
        return self._node_failures_tolerable

    @node_failures_tolerable.setter
    def node_failures_tolerable(self, node_failures_tolerable):
        """
        Sets the node_failures_tolerable of this HyperflexHxResiliencyInfoDt.

        :param node_failures_tolerable: The node_failures_tolerable of this HyperflexHxResiliencyInfoDt.
        :type: int
        """

        self._node_failures_tolerable = node_failures_tolerable

    @property
    def policy_compliance(self):
        """
        Gets the policy_compliance of this HyperflexHxResiliencyInfoDt.

        :return: The policy_compliance of this HyperflexHxResiliencyInfoDt.
        :rtype: str
        """
        return self._policy_compliance

    @policy_compliance.setter
    def policy_compliance(self, policy_compliance):
        """
        Sets the policy_compliance of this HyperflexHxResiliencyInfoDt.

        :param policy_compliance: The policy_compliance of this HyperflexHxResiliencyInfoDt.
        :type: str
        """
        allowed_values = ["UNKNOWN", "COMPLIANT", "NON_COMPLIANT"]
        if policy_compliance not in allowed_values:
            raise ValueError(
                "Invalid value for `policy_compliance` ({0}), must be one of {1}"
                .format(policy_compliance, allowed_values)
            )

        self._policy_compliance = policy_compliance

    @property
    def resiliency_state(self):
        """
        Gets the resiliency_state of this HyperflexHxResiliencyInfoDt.

        :return: The resiliency_state of this HyperflexHxResiliencyInfoDt.
        :rtype: str
        """
        return self._resiliency_state

    @resiliency_state.setter
    def resiliency_state(self, resiliency_state):
        """
        Sets the resiliency_state of this HyperflexHxResiliencyInfoDt.

        :param resiliency_state: The resiliency_state of this HyperflexHxResiliencyInfoDt.
        :type: str
        """
        allowed_values = ["UNKNOWN", "HEALTHY", "WARNING", "OFFLINE"]
        if resiliency_state not in allowed_values:
            raise ValueError(
                "Invalid value for `resiliency_state` ({0}), must be one of {1}"
                .format(resiliency_state, allowed_values)
            )

        self._resiliency_state = resiliency_state

    @property
    def ssd_failures_tolerable(self):
        """
        Gets the ssd_failures_tolerable of this HyperflexHxResiliencyInfoDt.

        :return: The ssd_failures_tolerable of this HyperflexHxResiliencyInfoDt.
        :rtype: int
        """
        return self._ssd_failures_tolerable

    @ssd_failures_tolerable.setter
    def ssd_failures_tolerable(self, ssd_failures_tolerable):
        """
        Sets the ssd_failures_tolerable of this HyperflexHxResiliencyInfoDt.

        :param ssd_failures_tolerable: The ssd_failures_tolerable of this HyperflexHxResiliencyInfoDt.
        :type: int
        """

        self._ssd_failures_tolerable = ssd_failures_tolerable

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
        if not isinstance(other, HyperflexHxResiliencyInfoDt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
