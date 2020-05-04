# coding: utf-8

"""
    API iSendPro

    [1] Liste des fonctionnalités : - envoi de SMS à un ou plusieurs destinataires, - lookup HLR, - récupération des récapitulatifs de campagne, - gestion des répertoires, - ajout en liste noire. - comptage du nombre de caractères des SMS  [2] Pour utiliser cette API vous devez: - Créer un compte iSendPro sur https://isendpro.com/ - Créditer votre compte      - Remarque: obtention d'un crédit de test possible sous conditions - Noter votre clé de compte (keyid)   - Elle vous sera indispensable à l'utilisation de l'API   - Vous pouvez la trouver dans le rubrique mon \"compte\", sous-rubrique \"mon API\" - Configurer le contrôle IP   - Le contrôle IP est configurable dans le rubrique mon \"compte\", sous-rubrique \"mon API\"   - Il s'agit d'un système de liste blanche, vous devez entrer les IP utilisées pour appeler l'API   - Vous pouvez également désactiver totalement le contrôle IP   # noqa: E501

    OpenAPI spec version: 1.1.1
    Contact: support@isendpro.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.hlr_reponse_etat import HLRReponseEtat  # noqa: E501
from swagger_client.rest import ApiException


class TestHLRReponseEtat(unittest.TestCase):
    """HLRReponseEtat unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHLRReponseEtat(self):
        """Test HLRReponseEtat"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.hlr_reponse_etat.HLRReponseEtat()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
