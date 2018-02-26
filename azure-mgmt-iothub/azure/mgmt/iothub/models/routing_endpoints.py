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


class RoutingEndpoints(Model):
    """The properties related to the custom endpoints to which your IoT hub routes
    messages based on the routing rules. A maximum of 10 custom endpoints are
    allowed across all endpoint types for paid hubs and only 1 custom endpoint
    is allowed across all endpoint types for free hubs.

    :param service_bus_queues: The list of Service Bus queue endpoints that
     IoT hub routes the messages to, based on the routing rules.
    :type service_bus_queues:
     list[~azure.mgmt.iothub.models.RoutingServiceBusQueueEndpointProperties]
    :param service_bus_topics: The list of Service Bus topic endpoints that
     the IoT hub routes the messages to, based on the routing rules.
    :type service_bus_topics:
     list[~azure.mgmt.iothub.models.RoutingServiceBusTopicEndpointProperties]
    :param event_hubs: The list of Event Hubs endpoints that IoT hub routes
     messages to, based on the routing rules. This list does not include the
     built-in Event Hubs endpoint.
    :type event_hubs:
     list[~azure.mgmt.iothub.models.RoutingEventHubProperties]
    :param storage_containers: The list of storage container endpoints that
     IoT hub routes messages to, based on the routing rules.
    :type storage_containers:
     list[~azure.mgmt.iothub.models.RoutingStorageContainerProperties]
    """

    _attribute_map = {
        'service_bus_queues': {'key': 'serviceBusQueues', 'type': '[RoutingServiceBusQueueEndpointProperties]'},
        'service_bus_topics': {'key': 'serviceBusTopics', 'type': '[RoutingServiceBusTopicEndpointProperties]'},
        'event_hubs': {'key': 'eventHubs', 'type': '[RoutingEventHubProperties]'},
        'storage_containers': {'key': 'storageContainers', 'type': '[RoutingStorageContainerProperties]'},
    }

    def __init__(self, service_bus_queues=None, service_bus_topics=None, event_hubs=None, storage_containers=None):
        super(RoutingEndpoints, self).__init__()
        self.service_bus_queues = service_bus_queues
        self.service_bus_topics = service_bus_topics
        self.event_hubs = event_hubs
        self.storage_containers = storage_containers
