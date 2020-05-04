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


class ComptageReponseEtatEtat(object):
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
        'tel': 'str',
        'nb_sms': 'str',
        'nb_caractere': 'str'
    }

    attribute_map = {
        'tel': 'tel',
        'nb_sms': 'nb_sms',
        'nb_caractere': 'nb_caractere'
    }

    def __init__(self, tel=None, nb_sms=None, nb_caractere=None):  # noqa: E501
        """ComptageReponseEtatEtat - a model defined in Swagger"""  # noqa: E501

        self._tel = None
        self._nb_sms = None
        self._nb_caractere = None
        self.discriminator = None

        if tel is not None:
            self.tel = tel
        if nb_sms is not None:
            self.nb_sms = nb_sms
        if nb_caractere is not None:
            self.nb_caractere = nb_caractere

    @property
    def tel(self):
        """Gets the tel of this ComptageReponseEtatEtat.  # noqa: E501

        numéro de téléphone  # noqa: E501

        :return: The tel of this ComptageReponseEtatEtat.  # noqa: E501
        :rtype: str
        """
        return self._tel

    @tel.setter
    def tel(self, tel):
        """Sets the tel of this ComptageReponseEtatEtat.

        numéro de téléphone  # noqa: E501

        :param tel: The tel of this ComptageReponseEtatEtat.  # noqa: E501
        :type: str
        """

        self._tel = tel

    @property
    def nb_sms(self):
        """Gets the nb_sms of this ComptageReponseEtatEtat.  # noqa: E501

        nombre de sms nécessaires  # noqa: E501

        :return: The nb_sms of this ComptageReponseEtatEtat.  # noqa: E501
        :rtype: str
        """
        return self._nb_sms

    @nb_sms.setter
    def nb_sms(self, nb_sms):
        """Sets the nb_sms of this ComptageReponseEtatEtat.

        nombre de sms nécessaires  # noqa: E501

        :param nb_sms: The nb_sms of this ComptageReponseEtatEtat.  # noqa: E501
        :type: str
        """

        self._nb_sms = nb_sms

    @property
    def nb_caractere(self):
        """Gets the nb_caractere of this ComptageReponseEtatEtat.  # noqa: E501

        nombre de caractères  # noqa: E501

        :return: The nb_caractere of this ComptageReponseEtatEtat.  # noqa: E501
        :rtype: str
        """
        return self._nb_caractere

    @nb_caractere.setter
    def nb_caractere(self, nb_caractere):
        """Sets the nb_caractere of this ComptageReponseEtatEtat.

        nombre de caractères  # noqa: E501

        :param nb_caractere: The nb_caractere of this ComptageReponseEtatEtat.  # noqa: E501
        :type: str
        """

        self._nb_caractere = nb_caractere

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
        if not isinstance(other, ComptageReponseEtatEtat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
