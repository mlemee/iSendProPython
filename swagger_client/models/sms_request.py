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


class SMSRequest(object):
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
        'gmt_zone': 'str',
        'date_envoi': 'str',
        'sms': 'list[str]',
        'num': 'list[str]',
        'repertoire_id': 'str',
        'emetteur': 'str',
        'tracker': 'list[str]',
        'smslong': 'str',
        'nostop': 'str',
        'num_azur': 'str',
        'ucs2': 'str'
    }

    attribute_map = {
        'keyid': 'keyid',
        'gmt_zone': 'gmt_zone',
        'date_envoi': 'date_envoi',
        'sms': 'sms',
        'num': 'num',
        'repertoire_id': 'repertoireId',
        'emetteur': 'emetteur',
        'tracker': 'tracker',
        'smslong': 'smslong',
        'nostop': 'nostop',
        'num_azur': 'numAzur',
        'ucs2': 'ucs2'
    }

    def __init__(self, keyid='', gmt_zone=None, date_envoi=None, sms=None, num=None, repertoire_id=None, emetteur=None, tracker=None, smslong=None, nostop=None, num_azur=None, ucs2=None):  # noqa: E501
        """SMSRequest - a model defined in Swagger"""  # noqa: E501

        self._keyid = None
        self._gmt_zone = None
        self._date_envoi = None
        self._sms = None
        self._num = None
        self._repertoire_id = None
        self._emetteur = None
        self._tracker = None
        self._smslong = None
        self._nostop = None
        self._num_azur = None
        self._ucs2 = None
        self.discriminator = None

        self.keyid = keyid
        if gmt_zone is not None:
            self.gmt_zone = gmt_zone
        if date_envoi is not None:
            self.date_envoi = date_envoi
        self.sms = sms
        self.num = num
        if repertoire_id is not None:
            self.repertoire_id = repertoire_id
        if emetteur is not None:
            self.emetteur = emetteur
        if tracker is not None:
            self.tracker = tracker
        if smslong is not None:
            self.smslong = smslong
        if nostop is not None:
            self.nostop = nostop
        if num_azur is not None:
            self.num_azur = num_azur
        if ucs2 is not None:
            self.ucs2 = ucs2

    @property
    def keyid(self):
        """Gets the keyid of this SMSRequest.  # noqa: E501

        Clé API  # noqa: E501

        :return: The keyid of this SMSRequest.  # noqa: E501
        :rtype: str
        """
        return self._keyid

    @keyid.setter
    def keyid(self, keyid):
        """Sets the keyid of this SMSRequest.

        Clé API  # noqa: E501

        :param keyid: The keyid of this SMSRequest.  # noqa: E501
        :type: str
        """
        if keyid is None:
            raise ValueError("Invalid value for `keyid`, must not be `None`")  # noqa: E501

        self._keyid = keyid

    @property
    def gmt_zone(self):
        """Gets the gmt_zone of this SMSRequest.  # noqa: E501

        Fuseau horaire de la date d'envoi  # noqa: E501

        :return: The gmt_zone of this SMSRequest.  # noqa: E501
        :rtype: str
        """
        return self._gmt_zone

    @gmt_zone.setter
    def gmt_zone(self, gmt_zone):
        """Sets the gmt_zone of this SMSRequest.

        Fuseau horaire de la date d'envoi  # noqa: E501

        :param gmt_zone: The gmt_zone of this SMSRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Pacific/Midway", "America/Adak", "Etc/GMT+10", "Pacific/Marquesas", "Pacific/Gambier", "America/Anchorage", "America/Ensenada", "Etc/GMT+8", "America/Los_Angeles", "America/Denver", "America/Chihuahua", "America/Dawson_Creek", "America/Belize", "America/Cancun", "Chile/EasterIsland", "America/Chicago", "America/New_York", "America/Havana", "America/Bogota", "America/Caracas", "America/Santiago", "America/La_Paz", "Atlantic/Stanley", "America/Campo_Grande", "America/Goose_Bay", "America/Glace_Bay", "America/St_Johns", "America/Araguaina", "America/Montevideo", "America/Miquelon", "America/Godthab", "America/Argentina/Buenos_Aires", "America/Sao_Paulo", "America/Noronha", "Atlantic/Cape_Verde", "Atlantic/Azores", "Europe/Belfast", "Europe/Dublin", "Europe/Lisbon", "Europe/London", "Africa/Abidjan", "Europe/Amsterdam", "Europe/Belgrade", "Europe/Brussels", "Africa/Algiers", "Africa/Windhoek", "Asia/Beirut", "Africa/Cairo", "Asia/Gaza", "Africa/Blantyre", "Asia/Jerusalem", "Europe/Minsk", "Asia/Damascus", "Europe/Moscow", "Africa/Addis_Ababa", "Asia/Tehran", "Asia/Dubai", "Asia/Yerevan", "Asia/Kabul", "Asia/Yekaterinburg", "Asia/Tashkent", "Asia/Kolkata", "Asia/Katmandu", "Asia/Dhaka", "Asia/Novosibirsk", "Asia/Rangoon", "Asia/Bangkok", "Asia/Krasnoyarsk", "Asia/Hong_Kong", "Asia/Irkutsk", "Australia/Perth", "Australia/Eucla", "Asia/Tokyo", "Asia/Seoul", "Asia/Yakutsk", "Australia/Adelaide", "Australia/Darwin", "Australia/Brisbane", "Australia/Hobart", "Asia/Vladivostok", "Australia/Lord_Howe", "Etc/GMT-11", "Asia/Magadan", "Pacific/Norfolk", "Asia/Anadyr", "Pacific/Auckland", "Etc/GMT-12", "Pacific/Chatham", "Pacific/Tongatapu", "Pacific/Kiritimati"]  # noqa: E501
        if gmt_zone not in allowed_values:
            raise ValueError(
                "Invalid value for `gmt_zone` ({0}), must be one of {1}"  # noqa: E501
                .format(gmt_zone, allowed_values)
            )

        self._gmt_zone = gmt_zone

    @property
    def date_envoi(self):
        """Gets the date_envoi of this SMSRequest.  # noqa: E501

        Paramètre optionnel, date d'envoi au format YYYY-MM-DD hh:mm  # noqa: E501

        :return: The date_envoi of this SMSRequest.  # noqa: E501
        :rtype: str
        """
        return self._date_envoi

    @date_envoi.setter
    def date_envoi(self, date_envoi):
        """Sets the date_envoi of this SMSRequest.

        Paramètre optionnel, date d'envoi au format YYYY-MM-DD hh:mm  # noqa: E501

        :param date_envoi: The date_envoi of this SMSRequest.  # noqa: E501
        :type: str
        """

        self._date_envoi = date_envoi

    @property
    def sms(self):
        """Gets the sms of this SMSRequest.  # noqa: E501


        :return: The sms of this SMSRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this SMSRequest.


        :param sms: The sms of this SMSRequest.  # noqa: E501
        :type: list[str]
        """
        if sms is None:
            raise ValueError("Invalid value for `sms`, must not be `None`")  # noqa: E501

        self._sms = sms

    @property
    def num(self):
        """Gets the num of this SMSRequest.  # noqa: E501


        :return: The num of this SMSRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._num

    @num.setter
    def num(self, num):
        """Sets the num of this SMSRequest.


        :param num: The num of this SMSRequest.  # noqa: E501
        :type: list[str]
        """
        if num is None:
            raise ValueError("Invalid value for `num`, must not be `None`")  # noqa: E501

        self._num = num

    @property
    def repertoire_id(self):
        """Gets the repertoire_id of this SMSRequest.  # noqa: E501

        Id du repertoire  # noqa: E501

        :return: The repertoire_id of this SMSRequest.  # noqa: E501
        :rtype: str
        """
        return self._repertoire_id

    @repertoire_id.setter
    def repertoire_id(self, repertoire_id):
        """Sets the repertoire_id of this SMSRequest.

        Id du repertoire  # noqa: E501

        :param repertoire_id: The repertoire_id of this SMSRequest.  # noqa: E501
        :type: str
        """

        self._repertoire_id = repertoire_id

    @property
    def emetteur(self):
        """Gets the emetteur of this SMSRequest.  # noqa: E501

        L'emetteur doit être une chaîne alphanumérique comprise entre 4 et 11 caractères. Les caractères acceptés sont les chiffres entre 0 et 9, les lettres entre A et Z et l’espace. Il ne peut pas comporter uniquement des chiffres. Pour la modification de l’émetteur et dans le cadre de campagnes commerciales, les opérateurs imposent contractuellement d’ajouter en fin de message le texte suivant : STOP XXXXX De ce fait, le message envoyé ne pourra excéder une longueur de 148 caractères au lieu des 160 caractères, le « STOP » étant rajouté automatiquement.  # noqa: E501

        :return: The emetteur of this SMSRequest.  # noqa: E501
        :rtype: str
        """
        return self._emetteur

    @emetteur.setter
    def emetteur(self, emetteur):
        """Sets the emetteur of this SMSRequest.

        L'emetteur doit être une chaîne alphanumérique comprise entre 4 et 11 caractères. Les caractères acceptés sont les chiffres entre 0 et 9, les lettres entre A et Z et l’espace. Il ne peut pas comporter uniquement des chiffres. Pour la modification de l’émetteur et dans le cadre de campagnes commerciales, les opérateurs imposent contractuellement d’ajouter en fin de message le texte suivant : STOP XXXXX De ce fait, le message envoyé ne pourra excéder une longueur de 148 caractères au lieu des 160 caractères, le « STOP » étant rajouté automatiquement.  # noqa: E501

        :param emetteur: The emetteur of this SMSRequest.  # noqa: E501
        :type: str
        """

        self._emetteur = emetteur

    @property
    def tracker(self):
        """Gets the tracker of this SMSRequest.  # noqa: E501


        :return: The tracker of this SMSRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._tracker

    @tracker.setter
    def tracker(self, tracker):
        """Sets the tracker of this SMSRequest.


        :param tracker: The tracker of this SMSRequest.  # noqa: E501
        :type: list[str]
        """

        self._tracker = tracker

    @property
    def smslong(self):
        """Gets the smslong of this SMSRequest.  # noqa: E501

        Le SMS long permet de dépasser la limite de 160 caractères en envoyant un message constitué de plusieurs SMS. Il est possible d’envoyer jusqu’à 6 SMS concaténés pour une longueur totale maximale de 918 caractères par message. Pour des raisons technique, la limite par SMS concaténé étant de 153 caractères. En cas de modification de l’émetteur, il faut considérer l’ajout automatique de 12 caractères du « STOP SMS ». Pour envoyer un smslong, il faut ajouter le paramètre smslong aux appels. La valeur de SMS doit être le nombre maximum de sms concaténé autorisé.   Pour ne pas avoir ce message d’erreur et obtenir un calcul dynamique du nombre de SMS alors il faut renseigner smslong = \"999\"   # noqa: E501

        :return: The smslong of this SMSRequest.  # noqa: E501
        :rtype: str
        """
        return self._smslong

    @smslong.setter
    def smslong(self, smslong):
        """Sets the smslong of this SMSRequest.

        Le SMS long permet de dépasser la limite de 160 caractères en envoyant un message constitué de plusieurs SMS. Il est possible d’envoyer jusqu’à 6 SMS concaténés pour une longueur totale maximale de 918 caractères par message. Pour des raisons technique, la limite par SMS concaténé étant de 153 caractères. En cas de modification de l’émetteur, il faut considérer l’ajout automatique de 12 caractères du « STOP SMS ». Pour envoyer un smslong, il faut ajouter le paramètre smslong aux appels. La valeur de SMS doit être le nombre maximum de sms concaténé autorisé.   Pour ne pas avoir ce message d’erreur et obtenir un calcul dynamique du nombre de SMS alors il faut renseigner smslong = \"999\"   # noqa: E501

        :param smslong: The smslong of this SMSRequest.  # noqa: E501
        :type: str
        """

        self._smslong = smslong

    @property
    def nostop(self):
        """Gets the nostop of this SMSRequest.  # noqa: E501

        Si le message n’est pas à but commercial, vous pouvez faire une demande pour retirer l’obligation du STOP. Une fois votre demande validée par nos services, vous pourrez supprimer la mention STOP SMS en ajoutant nostop = \"1\"  # noqa: E501

        :return: The nostop of this SMSRequest.  # noqa: E501
        :rtype: str
        """
        return self._nostop

    @nostop.setter
    def nostop(self, nostop):
        """Sets the nostop of this SMSRequest.

        Si le message n’est pas à but commercial, vous pouvez faire une demande pour retirer l’obligation du STOP. Une fois votre demande validée par nos services, vous pourrez supprimer la mention STOP SMS en ajoutant nostop = \"1\"  # noqa: E501

        :param nostop: The nostop of this SMSRequest.  # noqa: E501
        :type: str
        """

        self._nostop = nostop

    @property
    def num_azur(self):
        """Gets the num_azur of this SMSRequest.  # noqa: E501


        :return: The num_azur of this SMSRequest.  # noqa: E501
        :rtype: str
        """
        return self._num_azur

    @num_azur.setter
    def num_azur(self, num_azur):
        """Sets the num_azur of this SMSRequest.


        :param num_azur: The num_azur of this SMSRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["1"]  # noqa: E501
        if num_azur not in allowed_values:
            raise ValueError(
                "Invalid value for `num_azur` ({0}), must be one of {1}"  # noqa: E501
                .format(num_azur, allowed_values)
            )

        self._num_azur = num_azur

    @property
    def ucs2(self):
        """Gets the ucs2 of this SMSRequest.  # noqa: E501

        Il est également possible d’envoyer des SMS en alphabet non latin (russe, chinois, arabe, etc) sur les numéros hors France métropolitaine. Pour ce faire, la requête devrait être encodée au format UTF-8 et contenir l’argument ucs2 = \"1\" Du fait de contraintes techniques, 1 SMS unique ne pourra pas dépasser 70 caractères (au lieu des 160 usuels) et dans le cas de SMS long, chaque sms ne pourra dépasser 67 caractères.  # noqa: E501

        :return: The ucs2 of this SMSRequest.  # noqa: E501
        :rtype: str
        """
        return self._ucs2

    @ucs2.setter
    def ucs2(self, ucs2):
        """Sets the ucs2 of this SMSRequest.

        Il est également possible d’envoyer des SMS en alphabet non latin (russe, chinois, arabe, etc) sur les numéros hors France métropolitaine. Pour ce faire, la requête devrait être encodée au format UTF-8 et contenir l’argument ucs2 = \"1\" Du fait de contraintes techniques, 1 SMS unique ne pourra pas dépasser 70 caractères (au lieu des 160 usuels) et dans le cas de SMS long, chaque sms ne pourra dépasser 67 caractères.  # noqa: E501

        :param ucs2: The ucs2 of this SMSRequest.  # noqa: E501
        :type: str
        """

        self._ucs2 = ucs2

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
        if not isinstance(other, SMSRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other