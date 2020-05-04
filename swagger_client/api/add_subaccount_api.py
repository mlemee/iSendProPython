# coding: utf-8

"""
    API iSendPro

    [1] Liste des fonctionnalités : - envoi de SMS à un ou plusieurs destinataires, - lookup HLR, - récupération des récapitulatifs de campagne, - gestion des répertoires, - ajout en liste noire. - comptage du nombre de caractères des SMS  [2] Pour utiliser cette API vous devez: - Créer un compte iSendPro sur https://isendpro.com/ - Créditer votre compte      - Remarque: obtention d'un crédit de test possible sous conditions - Noter votre clé de compte (keyid)   - Elle vous sera indispensable à l'utilisation de l'API   - Vous pouvez la trouver dans le rubrique mon \"compte\", sous-rubrique \"mon API\" - Configurer le contrôle IP   - Le contrôle IP est configurable dans le rubrique mon \"compte\", sous-rubrique \"mon API\"   - Il s'agit d'un système de liste blanche, vous devez entrer les IP utilisées pour appeler l'API   - Vous pouvez également désactiver totalement le contrôle IP   # noqa: E501

    OpenAPI spec version: 1.1.1
    Contact: support@isendpro.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AddSubaccountApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def subaccount_add(self, addsubaccountrequest, **kwargs):  # noqa: E501
        """Ajoute un sous compte  # noqa: E501

        Ajoute un sous compte  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.subaccount_add(addsubaccountrequest, async=True)
        >>> result = thread.get()

        :param async bool
        :param SubaccountAddRequest addsubaccountrequest: add sub account request (required)
        :return: SubaccountAddResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.subaccount_add_with_http_info(addsubaccountrequest, **kwargs)  # noqa: E501
        else:
            (data) = self.subaccount_add_with_http_info(addsubaccountrequest, **kwargs)  # noqa: E501
            return data

    def subaccount_add_with_http_info(self, addsubaccountrequest, **kwargs):  # noqa: E501
        """Ajoute un sous compte  # noqa: E501

        Ajoute un sous compte  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.subaccount_add_with_http_info(addsubaccountrequest, async=True)
        >>> result = thread.get()

        :param async bool
        :param SubaccountAddRequest addsubaccountrequest: add sub account request (required)
        :return: SubaccountAddResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['addsubaccountrequest']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subaccount_add" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'addsubaccountrequest' is set
        if ('addsubaccountrequest' not in params or
                params['addsubaccountrequest'] is None):
            raise ValueError("Missing the required parameter `addsubaccountrequest` when calling `subaccount_add`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'addsubaccountrequest' in params:
            body_params = params['addsubaccountrequest']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/subaccount', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SubaccountAddResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
