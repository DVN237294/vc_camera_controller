# coding: utf-8

"""
    vc_webapi

    Web API for the Virtual Classroom project  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: 237294@via.dk
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class UserSignupModel(object):
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
        'full_name': 'str',
        'user_name': 'str',
        'password': 'str',
        'email': 'str'
    }

    attribute_map = {
        'full_name': 'fullName',
        'user_name': 'userName',
        'password': 'password',
        'email': 'email'
    }

    def __init__(self, full_name=None, user_name=None, password=None, email=None):  # noqa: E501
        """UserSignupModel - a model defined in OpenAPI"""  # noqa: E501

        self._full_name = None
        self._user_name = None
        self._password = None
        self._email = None
        self.discriminator = None

        self.full_name = full_name
        self.user_name = user_name
        self.password = password
        self.email = email

    @property
    def full_name(self):
        """Gets the full_name of this UserSignupModel.  # noqa: E501


        :return: The full_name of this UserSignupModel.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this UserSignupModel.


        :param full_name: The full_name of this UserSignupModel.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def user_name(self):
        """Gets the user_name of this UserSignupModel.  # noqa: E501


        :return: The user_name of this UserSignupModel.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserSignupModel.


        :param user_name: The user_name of this UserSignupModel.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this UserSignupModel.  # noqa: E501


        :return: The password of this UserSignupModel.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserSignupModel.


        :param password: The password of this UserSignupModel.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def email(self):
        """Gets the email of this UserSignupModel.  # noqa: E501


        :return: The email of this UserSignupModel.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserSignupModel.


        :param email: The email of this UserSignupModel.  # noqa: E501
        :type: str
        """

        self._email = email

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserSignupModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
