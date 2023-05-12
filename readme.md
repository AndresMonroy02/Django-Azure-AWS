# Django-Azure-AWS

## Installation

1. Clone this repository.

2. Navigate to the project directory.

3. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate # for Linux/Mac
venv\Scripts\activate # for Windows

4. Install the required packages:

pip install -r requirements.txt

## Usage

1. Activate your virtual environment:

source venv/bin/activate # for Linux/Mac
venv\Scripts\activate # for Windows

2. Run the development server:

python manage.py runserver

3. Open your web browser and go to http://localhost:8000/

## Note

- Make sure to add a `.env` file in the project root directory and add your environment variables there.

AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY_ID_HERE
AWS_SECRET_ACCESS_KEY=YOUR_SECRET_ACCESS_KEY_HERE
AWS_STORAGE_BUCKET_NAME=YOUR_STORAGE_BUCKET_NAME_HERE
AWS_S3_REGION_NAME=YOUR_S3_REGION_NAME_HERE
AZURE_TRANSLATE_KEY=YOUR_AZURE_TRANSLATE_KEY_HERE
AZURE_TRANSLATE_LOCATION=YOUR_AZURE_TRANSLATE_LOCATION_HERE
AZURE_TRANSLATE_ENDPOINT=YOUR_AZURE_TRANSLATE_ENDPOINT_HERE

Replace YOUR_ACCESS_KEY_ID_HERE, YOUR_SECRET_ACCESS_KEY_HERE, YOUR_STORAGE_BUCKET_NAME_HERE, YOUR_S3_REGION_NAME_HERE, YOUR_AZURE_TRANSLATE_KEY_HERE, YOUR_AZURE_TRANSLATE_LOCATION_HERE, and YOUR_AZURE_TRANSLATE_ENDPOINT_HERE with the actual values of your environment variables.

Make sure to save the file and add it to your .gitignore file so that the values are not uploaded to your repository.
