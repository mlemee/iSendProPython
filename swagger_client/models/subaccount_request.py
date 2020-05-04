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


class SubaccountRequest(object):
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
        'keyid': 'str',
        'sub_account_edit': 'str',
        'sub_account_key_id': 'str',
        'sub_account_add_credit': 'str',
        'sub_account_restriction_stop': 'str',
        'sub_account_restriction_time': 'str',
        'sub_account_price': 'str',
        'sub_account_country_code': 'str'
    }

    attribute_map = {
        'keyid': 'keyid',
        'sub_account_edit': 'subAccountEdit',
        'sub_account_key_id': 'subAccountKeyId',
        'sub_account_add_credit': 'subAccountAddCredit',
        'sub_account_restriction_stop': 'subAccountRestrictionStop',
        'sub_account_restriction_time': 'subAccountRestrictionTime',
        'sub_account_price': 'subAccountPrice',
        'sub_account_country_code': 'subAccountCountryCode'
    }

    def __init__(self, keyid='', sub_account_edit='setPrice', sub_account_key_id=None, sub_account_add_credit=None, sub_account_restriction_stop=None, sub_account_restriction_time=None, sub_account_price=None, sub_account_country_code=None):  # noqa: E501
        """SubaccountRequest - a model defined in Swagger"""  # noqa: E501

        self._keyid = None
        self._sub_account_edit = None
        self._sub_account_key_id = None
        self._sub_account_add_credit = None
        self._sub_account_restriction_stop = None
        self._sub_account_restriction_time = None
        self._sub_account_price = None
        self._sub_account_country_code = None
        self.discriminator = None

        self.keyid = keyid
        self.sub_account_edit = sub_account_edit
        if sub_account_key_id is not None:
            self.sub_account_key_id = sub_account_key_id
        if sub_account_add_credit is not None:
            self.sub_account_add_credit = sub_account_add_credit
        if sub_account_restriction_stop is not None:
            self.sub_account_restriction_stop = sub_account_restriction_stop
        if sub_account_restriction_time is not None:
            self.sub_account_restriction_time = sub_account_restriction_time
        if sub_account_price is not None:
            self.sub_account_price = sub_account_price
        if sub_account_country_code is not None:
            self.sub_account_country_code = sub_account_country_code

    @property
    def keyid(self):
        """Gets the keyid of this SubaccountRequest.  # noqa: E501

        Clé API  # noqa: E501

        :return: The keyid of this SubaccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._keyid

    @keyid.setter
    def keyid(self, keyid):
        """Sets the keyid of this SubaccountRequest.

        Clé API  # noqa: E501

        :param keyid: The keyid of this SubaccountRequest.  # noqa: E501
        :type: str
        """
        if keyid is None:
            raise ValueError("Invalid value for `keyid`, must not be `None`")  # noqa: E501

        self._keyid = keyid

    @property
    def sub_account_edit(self):
        """Gets the sub_account_edit of this SubaccountRequest.  # noqa: E501

        action à réaliser soit setPrice pour définir un prix ou addCredit pour ajouter du credit ou setRestriction modifier la restriction stop /  # noqa: E501

        :return: The sub_account_edit of this SubaccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._sub_account_edit

    @sub_account_edit.setter
    def sub_account_edit(self, sub_account_edit):
        """Sets the sub_account_edit of this SubaccountRequest.

        action à réaliser soit setPrice pour définir un prix ou addCredit pour ajouter du credit ou setRestriction modifier la restriction stop /  # noqa: E501

        :param sub_account_edit: The sub_account_edit of this SubaccountRequest.  # noqa: E501
        :type: str
        """
        if sub_account_edit is None:
            raise ValueError("Invalid value for `sub_account_edit`, must not be `None`")  # noqa: E501
        allowed_values = ["setPrice", "addCredit", "setRestriction"]  # noqa: E501
        if sub_account_edit not in allowed_values:
            raise ValueError(
                "Invalid value for `sub_account_edit` ({0}), must be one of {1}"  # noqa: E501
                .format(sub_account_edit, allowed_values)
            )

        self._sub_account_edit = sub_account_edit

    @property
    def sub_account_key_id(self):
        """Gets the sub_account_key_id of this SubaccountRequest.  # noqa: E501

        keyid du sous-compte  # noqa: E501

        :return: The sub_account_key_id of this SubaccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._sub_account_key_id

    @sub_account_key_id.setter
    def sub_account_key_id(self, sub_account_key_id):
        """Sets the sub_account_key_id of this SubaccountRequest.

        keyid du sous-compte  # noqa: E501

        :param sub_account_key_id: The sub_account_key_id of this SubaccountRequest.  # noqa: E501
        :type: str
        """

        self._sub_account_key_id = sub_account_key_id

    @property
    def sub_account_add_credit(self):
        """Gets the sub_account_add_credit of this SubaccountRequest.  # noqa: E501

        montant du crédit à ajouter  # noqa: E501

        :return: The sub_account_add_credit of this SubaccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._sub_account_add_credit

    @sub_account_add_credit.setter
    def sub_account_add_credit(self, sub_account_add_credit):
        """Sets the sub_account_add_credit of this SubaccountRequest.

        montant du crédit à ajouter  # noqa: E501

        :param sub_account_add_credit: The sub_account_add_credit of this SubaccountRequest.  # noqa: E501
        :type: str
        """

        self._sub_account_add_credit = sub_account_add_credit

    @property
    def sub_account_restriction_stop(self):
        """Gets the sub_account_restriction_stop of this SubaccountRequest.  # noqa: E501


        :return: The sub_account_restriction_stop of this SubaccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._sub_account_restriction_stop

    @sub_account_restriction_stop.setter
    def sub_account_restriction_stop(self, sub_account_restriction_stop):
        """Sets the sub_account_restriction_stop of this SubaccountRequest.


        :param sub_account_restriction_stop: The sub_account_restriction_stop of this SubaccountRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["0", "1"]  # noqa: E501
        if sub_account_restriction_stop not in allowed_values:
            raise ValueError(
                "Invalid value for `sub_account_restriction_stop` ({0}), must be one of {1}"  # noqa: E501
                .format(sub_account_restriction_stop, allowed_values)
            )

        self._sub_account_restriction_stop = sub_account_restriction_stop

    @property
    def sub_account_restriction_time(self):
        """Gets the sub_account_restriction_time of this SubaccountRequest.  # noqa: E501


        :return: The sub_account_restriction_time of this SubaccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._sub_account_restriction_time

    @sub_account_restriction_time.setter
    def sub_account_restriction_time(self, sub_account_restriction_time):
        """Sets the sub_account_restriction_time of this SubaccountRequest.


        :param sub_account_restriction_time: The sub_account_restriction_time of this SubaccountRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["0", "1"]  # noqa: E501
        if sub_account_restriction_time not in allowed_values:
            raise ValueError(
                "Invalid value for `sub_account_restriction_time` ({0}), must be one of {1}"  # noqa: E501
                .format(sub_account_restriction_time, allowed_values)
            )

        self._sub_account_restriction_time = sub_account_restriction_time

    @property
    def sub_account_price(self):
        """Gets the sub_account_price of this SubaccountRequest.  # noqa: E501


        :return: The sub_account_price of this SubaccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._sub_account_price

    @sub_account_price.setter
    def sub_account_price(self, sub_account_price):
        """Sets the sub_account_price of this SubaccountRequest.


        :param sub_account_price: The sub_account_price of this SubaccountRequest.  # noqa: E501
        :type: str
        """

        self._sub_account_price = sub_account_price

    @property
    def sub_account_country_code(self):
        """Gets the sub_account_country_code of this SubaccountRequest.  # noqa: E501


        :return: The sub_account_country_code of this SubaccountRequest.  # noqa: E501
        :rtype: str
        """
        return self._sub_account_country_code

    @sub_account_country_code.setter
    def sub_account_country_code(self, sub_account_country_code):
        """Sets the sub_account_country_code of this SubaccountRequest.


        :param sub_account_country_code: The sub_account_country_code of this SubaccountRequest.  # noqa: E501
        :type: str
        """

        self._sub_account_country_code = sub_account_country_code

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
        if not isinstance(other, SubaccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other