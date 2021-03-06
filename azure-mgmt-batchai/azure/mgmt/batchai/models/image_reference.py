# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ImageReference(Model):
    """The image reference.

    :param publisher: Publisher of the image.
    :type publisher: str
    :param offer: Offer of the image.
    :type offer: str
    :param sku: SKU of the image.
    :type sku: str
    :param version: Version of the image.
    :type version: str
    """

    _validation = {
        'publisher': {'required': True},
        'offer': {'required': True},
        'sku': {'required': True},
    }

    _attribute_map = {
        'publisher': {'key': 'publisher', 'type': 'str'},
        'offer': {'key': 'offer', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, publisher, offer, sku, version=None):
        self.publisher = publisher
        self.offer = offer
        self.sku = sku
        self.version = version
