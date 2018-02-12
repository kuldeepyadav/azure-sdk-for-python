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


class Classification(Model):
    """The classification details of the text.

    :param category1: The category1 score details of the text. <a
     href="https://aka.ms/textClassifyCategories">Click here</a> for more
     details on category classification.
    :type category1:
     ~azure.cognitiveservices.vision.contentmoderator.models.ClassificationCategory1
    :param category2: The category2 score details of the text. <a
     href="https://aka.ms/textClassifyCategories">Click here</a> for more
     details on category classification.
    :type category2:
     ~azure.cognitiveservices.vision.contentmoderator.models.ClassificationCategory2
    :param category3: The category3 score details of the text. <a
     href="https://aka.ms/textClassifyCategories">Click here</a> for more
     details on category classification.
    :type category3:
     ~azure.cognitiveservices.vision.contentmoderator.models.ClassificationCategory3
    :param review_recommended: The review recommended flag.
    :type review_recommended: bool
    """

    _attribute_map = {
        'category1': {'key': 'Category1', 'type': 'ClassificationCategory1'},
        'category2': {'key': 'Category2', 'type': 'ClassificationCategory2'},
        'category3': {'key': 'Category3', 'type': 'ClassificationCategory3'},
        'review_recommended': {'key': 'ReviewRecommended', 'type': 'bool'},
    }

    def __init__(self, category1=None, category2=None, category3=None, review_recommended=None):
        super(Classification, self).__init__()
        self.category1 = category1
        self.category2 = category2
        self.category3 = category3
        self.review_recommended = review_recommended
