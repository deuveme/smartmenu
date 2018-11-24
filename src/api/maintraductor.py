import json

from watson_developer_cloud import LanguageTranslatorV3

language_translator = LanguageTranslatorV3(
    version='2.4.1',
    iam_apikey='EaotF6vCJtTTWQWigO6a9oi2GVTVycPCNkQxFtqzKAbn',
    url='https://gateway-syd.watsonplatform.net/language-translator/api'
)


translation = language_translator.translate(
    text='Hello',
    model_id='en-es').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))

