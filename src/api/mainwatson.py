import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, CategoriesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2018-03-16',
    iam_apikey='GA88EsoDG-juC0DgrlQdYDMLocVlyb--IDi2METuRdOz',
    url='https://gateway-syd.watsonplatform.net/natural-language-understanding/api'
)

response = natural_language_understanding.analyze(
    url='www.ibm.com',
    features=Features(categories=CategoriesOptions())).get_result()

print(json.dumps(response, indent=2))
