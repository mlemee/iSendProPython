# SMSRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyid** | **str** | Clé API | [default to '']
**gmt_zone** | **str** | Fuseau horaire de la date d&#39;envoi | [optional] 
**date_envoi** | **str** | Paramètre optionnel, date d&#39;envoi au format YYYY-MM-DD hh:mm | [optional] 
**sms** | **list[str]** |  | 
**num** | **list[str]** |  | 
**repertoire_id** | **str** | Id du repertoire | [optional] 
**emetteur** | **str** | L&#39;emetteur doit être une chaîne alphanumérique comprise entre 4 et 11 caractères. Les caractères acceptés sont les chiffres entre 0 et 9, les lettres entre A et Z et l’espace. Il ne peut pas comporter uniquement des chiffres. Pour la modification de l’émetteur et dans le cadre de campagnes commerciales, les opérateurs imposent contractuellement d’ajouter en fin de message le texte suivant : STOP XXXXX De ce fait, le message envoyé ne pourra excéder une longueur de 148 caractères au lieu des 160 caractères, le « STOP » étant rajouté automatiquement. | [optional] 
**tracker** | **list[str]** |  | [optional] 
**smslong** | **str** | Le SMS long permet de dépasser la limite de 160 caractères en envoyant un message constitué de plusieurs SMS. Il est possible d’envoyer jusqu’à 6 SMS concaténés pour une longueur totale maximale de 918 caractères par message. Pour des raisons technique, la limite par SMS concaténé étant de 153 caractères. En cas de modification de l’émetteur, il faut considérer l’ajout automatique de 12 caractères du « STOP SMS ». Pour envoyer un smslong, il faut ajouter le paramètre smslong aux appels. La valeur de SMS doit être le nombre maximum de sms concaténé autorisé.   Pour ne pas avoir ce message d’erreur et obtenir un calcul dynamique du nombre de SMS alors il faut renseigner smslong &#x3D; \&quot;999\&quot;  | [optional] 
**nostop** | **str** | Si le message n’est pas à but commercial, vous pouvez faire une demande pour retirer l’obligation du STOP. Une fois votre demande validée par nos services, vous pourrez supprimer la mention STOP SMS en ajoutant nostop &#x3D; \&quot;1\&quot; | [optional] 
**num_azur** | **str** |  | [optional] 
**ucs2** | **str** | Il est également possible d’envoyer des SMS en alphabet non latin (russe, chinois, arabe, etc) sur les numéros hors France métropolitaine. Pour ce faire, la requête devrait être encodée au format UTF-8 et contenir l’argument ucs2 &#x3D; \&quot;1\&quot; Du fait de contraintes techniques, 1 SMS unique ne pourra pas dépasser 70 caractères (au lieu des 160 usuels) et dans le cas de SMS long, chaque sms ne pourra dépasser 67 caractères. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


