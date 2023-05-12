from http.client import HTTPResponse
import boto3
from django.conf import settings
from django.shortcuts import render
import requests, uuid, json

# Create your views here.
def helloWorld(HttpRequest):
    return HTTPResponse("Hello World!")

#S3 concult bucket images
def s3_images(request):
    s3 = boto3.client('s3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME)
    objects = s3.list_objects(Bucket=settings.AWS_STORAGE_BUCKET_NAME)

    image_urls = []
    for obj in objects['Contents']:
        if obj['Key'].endswith('.jpg') or obj['Key'].endswith('.png'):
            image_url = s3.generate_presigned_url(
                ClientMethod='get_object',
                Params={
                    'Bucket': settings.AWS_STORAGE_BUCKET_NAME,
                    'Key': obj['Key']
                },
                ExpiresIn=3600  # Link expiration time in seconds
            )
            image_urls.append(image_url)

    return render(request, 'image_list.html', {'image_urls': image_urls})

def index(request):
    return render(request, 'index.html')


def AzureTranslate(request):

    # Add your key and endpoint
    key = settings.AZURE_TRANSLATE_KEY
    endpoint = settings.AZURE_TRANLATE_ENDPOINT
    uno, language, dos, textresponse = "", "", "", ""
    texts= []
    idiomas = {
        'en': 'Inglés',
        'fr': 'Francés',
        'ar': 'Árabe'
    }


    if request.method == "POST":
        data = request.POST
        uno = data['uno']
        idioma = data['idioma']

        # location, also known as region.
        # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
        location = settings.AZURE_TRANSLATE_LOCATION
        path = '/translate'
        constructed_url = endpoint + path
        headers = {
            'Ocp-Apim-Subscription-Key': key,
            # location required if you're using a multi-service or regional (not global) resource.
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

        params = {
            'api-version': '3.0',
            'from': 'es',
            'to': [idioma]
        }
        body = [{
            'text': uno
        }]

        requestssss = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = requestssss.json()

        for translation in response[0]['translations']: 
            texts.append(translation['text'])

        dos = texts[0]
        textresponse = "La traducción de " + uno
        language = idiomas.get(idioma)


    return render(request, 'azure_translate.html', context={'uno': uno, 'dos': dos, 'textresponse': textresponse, 'language': language})



