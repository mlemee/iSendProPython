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


class REPERTOIREcreaterequest(object):
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
        'repertoire_edit': 'str',
        'repertoire_nom': 'str'
    }

    attribute_map = {
        'keyid': 'keyid',
        'repertoire_edit': 'repertoireEdit',
        'repertoire_nom': 'repertoireNom'
    }

    def __init__(self, keyid='', repertoire_edit='create', repertoire_nom=''):  # noqa: E501
        """REPERTOIREcreaterequest - a model defined in Swagger"""  # noqa: E501

        self._keyid = None
        self._repertoire_edit = None
        self._repertoire_nom = None
        self.discriminator = None

        self.keyid = keyid
        self.repertoire_edit = repertoire_edit
        self.repertoire_nom = repertoire_nom

    @property
    def keyid(self):
        """Gets the keyid of this REPERTOIREcreaterequest.  # noqa: E501

        Clé API  # noqa: E501

        :return: The keyid of this REPERTOIREcreaterequest.  # noqa: E501
        :rtype: str
        """
        return self._keyid

    @keyid.setter
    def keyid(self, keyid):
        """Sets the keyid of this REPERTOIREcreaterequest.

        Clé API  # noqa: E501

        :param keyid: The keyid of this REPERTOIREcreaterequest.  # noqa: E501
        :type: str
        """
        if keyid is None:
            raise ValueError("Invalid value for `keyid`, must not be `None`")  # noqa: E501

        self._keyid = keyid

    @property
    def repertoire_edit(self):
        """Gets the repertoire_edit of this REPERTOIREcreaterequest.  # noqa: E501

        Action à réaliser doit valoir \"create\" ici.  # noqa: E501

        :return: The repertoire_edit of this REPERTOIREcreaterequest.  # noqa: E501
        :rtype: str
        """
        return self._repertoire_edit

    @repertoire_edit.setter
    def repertoire_edit(self, repertoire_edit):
        """Sets the repertoire_edit of this REPERTOIREcreaterequest.

        Action à réaliser doit valoir \"create\" ici.  # noqa: E501

        :param repertoire_edit: The repertoire_edit of this REPERTOIREcreaterequest.  # noqa: E501
        :type: str
        """
        if repertoire_edit is None:
            raise ValueError("Invalid value for `repertoire_edit`, must not be `None`")  # noqa: E501
        allowed_values = ["create"]  # noqa: E501
        if repertoire_edit not in allowed_values:
            raise ValueError(
                "Invalid value for `repertoire_edit` ({0}), must be one of {1}"  # noqa: E501
                .format(repertoire_edit, allowed_values)
            )

        self._repertoire_edit = repertoire_edit

    @property
    def repertoire_nom(self):
        """Gets the repertoire_nom of this REPERTOIREcreaterequest.  # noqa: E501

        Nom du répertoire (libellé) à créer  # noqa: E501

        :return: The repertoire_nom of this REPERTOIREcreaterequest.  # noqa: E501
        :rtype: str
        """
        return self._repertoire_nom

    @repertoire_nom.setter
    def repertoire_nom(self, repertoire_nom):
        """Sets the repertoire_nom of this REPERTOIREcreaterequest.

        Nom du répertoire (libellé) à créer  # noqa: E501

        :param repertoire_nom: The repertoire_nom of this REPERTOIREcreaterequest.  # noqa: E501
        :type: str
        """
        if repertoire_nom is None:
            raise ValueError("Invalid value for `repertoire_nom`, must not be `None`")  # noqa: E501

        self._repertoire_nom = repertoire_nom

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
        if not isinstance(other, REPERTOIREcreaterequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
