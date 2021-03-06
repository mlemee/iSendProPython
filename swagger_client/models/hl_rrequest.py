# coding: utf-8

"""
    API iSendPro

    [1] Liste des fonctionnalités : - envoi de SMS à un ou plusieurs destinataires, - lookup HLR, - récupération des récapitulatifs de campagne, - gestion des répertoires, - ajout en liste noire. - comptage du nombre de caractères des SMS  [2] Pour utiliser cette API vous devez: - Créer un compte iSendPro sur https://isendpro.com/ - Créditer votre compte      - Remarque: obtention d'un crédit de test possible sous conditions - Noter votre clé de compte (keyid)   - Elle vous sera indispensable à l'utilisation de l'API   - Vous pouvez la trouver dans le rubrique mon \"compte\", sous-rubrique \"mon API\" - Configurer le contrôle IP   - Le contrôle IP est configurable dans le rubrique mon \"compte\", sous-rubrique \"mon API\"   - Il s'agit d'un système de liste blanche, vous devez entrer les IP utilisées pour appeler l'API   - Vous pouvez également désactiver totalement le contrôle IP   # noqa: E501

    OpenAPI spec version: 1.1.1
    Contact: support@isendpro.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class HLRrequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'get_hlr': 'str',
        'num': 'list[str]',
        'keyid': 'str'
    }

    attribute_map = {
        'get_hlr': 'getHLR',
        'num': 'num',
        'keyid': 'keyid'
    }

    def __init__(self, get_hlr='1', num=None, keyid=''):  # noqa: E501
        """HLRrequest - a model defined in Swagger"""  # noqa: E501

        self._get_hlr = None
        self._num = None
        self._keyid = None
        self.discriminator = None

        self.get_hlr = get_hlr
        self.num = num
        self.keyid = keyid

    @property
    def get_hlr(self):
        """Gets the get_hlr of this HLRrequest.  # noqa: E501

        Doit valoir \"1\"  # noqa: E501

        :return: The get_hlr of this HLRrequest.  # noqa: E501
        :rtype: str
        """
        return self._get_hlr

    @get_hlr.setter
    def get_hlr(self, get_hlr):
        """Sets the get_hlr of this HLRrequest.

        Doit valoir \"1\"  # noqa: E501

        :param get_hlr: The get_hlr of this HLRrequest.  # noqa: E501
        :type: str
        """
        if get_hlr is None:
            raise ValueError("Invalid value for `get_hlr`, must not be `None`")  # noqa: E501
        allowed_values = ["1"]  # noqa: E501
        if get_hlr not in allowed_values:
            raise ValueError(
                "Invalid value for `get_hlr` ({0}), must be one of {1}"  # noqa: E501
                .format(get_hlr, allowed_values)
            )

        self._get_hlr = get_hlr

    @property
    def num(self):
        """Gets the num of this HLRrequest.  # noqa: E501

        liste de numéros de téléphone  # noqa: E501

        :return: The num of this HLRrequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this HLRrequest.

        liste de numéros de téléphone  # noqa: E501

        :param num: The num of this HLRrequest.  # noqa: E501
        :type: list[str]
        """
        if num is None:
            raise ValueError("Invalid value for `num`, must not be `None`")  # noqa: E501

        self._num = num

    @property
    def keyid(self):
        """Gets the keyid of this HLRrequest.  # noqa: E501

        Clé API  # noqa: E501

        :return: The keyid of this HLRrequest.  # noqa: E501
        :rtype: str
        """
        return self._keyid

    @keyid.setter
    def keyid(self, keyid):
        """Sets the keyid of this HLRrequest.

        Clé API  # noqa: E501

        :param keyid: The keyid of this HLRrequest.  # noqa: E501
        :type: str
        """
        if keyid is None:
            raise ValueError("Invalid value for `keyid`, must not be `None`")  # noqa: E501

        self._keyid = keyid

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, HLRrequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
