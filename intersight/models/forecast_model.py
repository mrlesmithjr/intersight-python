# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1461
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ForecastModel(object):
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
        'accuracy': 'float',
        'model_data': 'list[float]',
        'model_type': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'accuracy': 'Accuracy',
        'model_data': 'ModelData',
        'model_type': 'ModelType'
    }

    def __init__(self, object_type=None, accuracy=None, model_data=None, model_type='Linear'):
        """
        ForecastModel - a model defined in Swagger
        """

        self._object_type = None
        self._accuracy = None
        self._model_data = None
        self._model_type = None

        if object_type is not None:
          self.object_type = object_type
        if accuracy is not None:
          self.accuracy = accuracy
        if model_data is not None:
          self.model_data = model_data
        if model_type is not None:
          self.model_type = model_type

    @property
    def object_type(self):
        """
        Gets the object_type of this ForecastModel.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :return: The object_type of this ForecastModel.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this ForecastModel.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :param object_type: The object_type of this ForecastModel.
        :type: str
        """

        self._object_type = object_type

    @property
    def accuracy(self):
        """
        Gets the accuracy of this ForecastModel.
        The standard error of the estimate is a measure of the accuracy of predictions from predective modeling.

        :return: The accuracy of this ForecastModel.
        :rtype: float
        """
        return self._accuracy

    @accuracy.setter
    def accuracy(self, accuracy):
        """
        Sets the accuracy of this ForecastModel.
        The standard error of the estimate is a measure of the accuracy of predictions from predective modeling.

        :param accuracy: The accuracy of this ForecastModel.
        :type: float
        """

        self._accuracy = accuracy

    @property
    def model_data(self):
        """
        Gets the model_data of this ForecastModel.
        The collection of model data returned by running a predictive modeling. Data can range from slope, coefficient and more depending on the type of model used.

        :return: The model_data of this ForecastModel.
        :rtype: list[float]
        """
        return self._model_data

    @model_data.setter
    def model_data(self, model_data):
        """
        Sets the model_data of this ForecastModel.
        The collection of model data returned by running a predictive modeling. Data can range from slope, coefficient and more depending on the type of model used.

        :param model_data: The model_data of this ForecastModel.
        :type: list[float]
        """

        self._model_data = model_data

    @property
    def model_type(self):
        """
        Gets the model_type of this ForecastModel.
        Model type indicating type of predictive model used for computing forecast.

        :return: The model_type of this ForecastModel.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this ForecastModel.
        Model type indicating type of predictive model used for computing forecast.

        :param model_type: The model_type of this ForecastModel.
        :type: str
        """
        allowed_values = ["Linear"]
        if model_type not in allowed_values:
            raise ValueError(
                "Invalid value for `model_type` ({0}), must be one of {1}"
                .format(model_type, allowed_values)
            )

        self._model_type = model_type

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
        if not isinstance(other, ForecastModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
