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


class ExpressRouteServiceProviderBandwidthsOffered(Model):
    """Contains bandwidths offered in ExpressRouteServiceProvider resources.

    :param offer_name: The OfferName.
    :type offer_name: str
    :param value_in_mbps: The ValueInMbps.
    :type value_in_mbps: int
    """

    _attribute_map = {
        'offer_name': {'key': 'offerName', 'type': 'str'},
        'value_in_mbps': {'key': 'valueInMbps', 'type': 'int'},
    }

    def __init__(self, offer_name=None, value_in_mbps=None):
        super(ExpressRouteServiceProviderBandwidthsOffered, self).__init__()
        self.offer_name = offer_name
        self.value_in_mbps = value_in_mbps
