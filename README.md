# docspring
DocSpring is a service that helps you fill out and sign PDF templates.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.3.2
- Build package: com.docspring.codegen.DocSpringPythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import docspring 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import docspring
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import docspring
from docspring.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: api_token_basic
configuration = docspring.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = docspring.PDFApi(docspring.ApiClient(configuration))
template_id = 'tpl_000000000000000002' # str | 
add_fields_data = docspring.AddFieldsData() # AddFieldsData | 

try:
    # Add new fields to a Template
    api_response = api_instance.add_fields_to_template(template_id, add_fields_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->add_fields_to_template: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.docspring.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PDFApi* | [**add_fields_to_template**](docs/PDFApi.md#add_fields_to_template) | **PUT** /templates/{template_id}/add_fields | Add new fields to a Template
*PDFApi* | [**batch_generate_pdf_v1**](docs/PDFApi.md#batch_generate_pdf_v1) | **POST** /templates/{template_id}/submissions/batch | Generates multiple PDFs
*PDFApi* | [**batch_generate_pdfs**](docs/PDFApi.md#batch_generate_pdfs) | **POST** /submissions/batches | Generates multiple PDFs
*PDFApi* | [**combine_pdfs**](docs/PDFApi.md#combine_pdfs) | **POST** /combined_submissions?v&#x3D;2 | Merge submission PDFs, template PDFs, or custom files
*PDFApi* | [**combine_submissions**](docs/PDFApi.md#combine_submissions) | **POST** /combined_submissions | Merge generated PDFs together
*PDFApi* | [**copy_template**](docs/PDFApi.md#copy_template) | **POST** /templates/{template_id}/copy | Copy a Template
*PDFApi* | [**create_custom_file_from_upload**](docs/PDFApi.md#create_custom_file_from_upload) | **POST** /custom_files | Create a new custom file from a cached presign upload
*PDFApi* | [**create_data_request_token**](docs/PDFApi.md#create_data_request_token) | **POST** /data_requests/{data_request_id}/tokens | Creates a new data request token for form authentication
*PDFApi* | [**create_folder**](docs/PDFApi.md#create_folder) | **POST** /folders/ | Create a folder
*PDFApi* | [**create_html_template**](docs/PDFApi.md#create_html_template) | **POST** /templates?desc&#x3D;html | Create a new HTML template
*PDFApi* | [**create_pdf_template**](docs/PDFApi.md#create_pdf_template) | **POST** /templates | Create a new PDF template with a form POST file upload
*PDFApi* | [**create_pdf_template_from_upload**](docs/PDFApi.md#create_pdf_template_from_upload) | **POST** /templates?desc&#x3D;cached_upload | Create a new PDF template from a cached presign upload
*PDFApi* | [**delete_folder**](docs/PDFApi.md#delete_folder) | **DELETE** /folders/{folder_id} | Delete a folder
*PDFApi* | [**expire_combined_submission**](docs/PDFApi.md#expire_combined_submission) | **DELETE** /combined_submissions/{combined_submission_id} | Expire a combined submission
*PDFApi* | [**expire_submission**](docs/PDFApi.md#expire_submission) | **DELETE** /submissions/{submission_id} | Expire a PDF submission
*PDFApi* | [**generate_pdf**](docs/PDFApi.md#generate_pdf) | **POST** /templates/{template_id}/submissions | Generates a new PDF
*PDFApi* | [**get_combined_submission**](docs/PDFApi.md#get_combined_submission) | **GET** /combined_submissions/{combined_submission_id} | Check the status of a combined submission (merged PDFs)
*PDFApi* | [**get_data_request**](docs/PDFApi.md#get_data_request) | **GET** /data_requests/{data_request_id} | Look up a submission data request
*PDFApi* | [**get_full_template**](docs/PDFApi.md#get_full_template) | **GET** /templates/{template_id}?full&#x3D;true | Fetch the full template attributes
*PDFApi* | [**get_presign_url**](docs/PDFApi.md#get_presign_url) | **GET** /uploads/presign | Get a presigned URL so that you can upload a file to our AWS S3 bucket
*PDFApi* | [**get_submission**](docs/PDFApi.md#get_submission) | **GET** /submissions/{submission_id} | Check the status of a PDF
*PDFApi* | [**get_submission_batch**](docs/PDFApi.md#get_submission_batch) | **GET** /submissions/batches/{submission_batch_id} | Check the status of a submission batch job
*PDFApi* | [**get_template**](docs/PDFApi.md#get_template) | **GET** /templates/{template_id} | Check the status of an uploaded template
*PDFApi* | [**get_template_schema**](docs/PDFApi.md#get_template_schema) | **GET** /templates/{template_id}/schema | Fetch the JSON schema for a template
*PDFApi* | [**list_folders**](docs/PDFApi.md#list_folders) | **GET** /folders/ | Get a list of all folders
*PDFApi* | [**list_submissions**](docs/PDFApi.md#list_submissions) | **GET** /submissions | List all submissions
*PDFApi* | [**list_submissions_0**](docs/PDFApi.md#list_submissions_0) | **GET** /templates/{template_id}/submissions | List all submissions for a given template
*PDFApi* | [**list_templates**](docs/PDFApi.md#list_templates) | **GET** /templates | Get a list of all templates
*PDFApi* | [**move_folder_to_folder**](docs/PDFApi.md#move_folder_to_folder) | **POST** /folders/{folder_id}/move | Move a folder
*PDFApi* | [**move_template_to_folder**](docs/PDFApi.md#move_template_to_folder) | **POST** /templates/{template_id}/move | Move Template to folder
*PDFApi* | [**rename_folder**](docs/PDFApi.md#rename_folder) | **POST** /folders/{folder_id}/rename | Rename a folder
*PDFApi* | [**test_authentication**](docs/PDFApi.md#test_authentication) | **GET** /authentication | Test Authentication
*PDFApi* | [**update_data_request**](docs/PDFApi.md#update_data_request) | **PUT** /data_requests/{data_request_id} | Update a submission data request
*PDFApi* | [**update_template**](docs/PDFApi.md#update_template) | **PUT** /templates/{template_id} | Update a Template


## Documentation For Models

 - [AddFieldsData](docs/AddFieldsData.md)
 - [AddFieldsTemplateResponse](docs/AddFieldsTemplateResponse.md)
 - [AuthenticationError](docs/AuthenticationError.md)
 - [AuthenticationSuccessResponse](docs/AuthenticationSuccessResponse.md)
 - [CombinePdfsData](docs/CombinePdfsData.md)
 - [CombinedSubmission](docs/CombinedSubmission.md)
 - [CombinedSubmissionAction](docs/CombinedSubmissionAction.md)
 - [CombinedSubmissionData](docs/CombinedSubmissionData.md)
 - [CopyTemplateData](docs/CopyTemplateData.md)
 - [CreateCombinedSubmissionResponse](docs/CreateCombinedSubmissionResponse.md)
 - [CreateCustomFileData](docs/CreateCustomFileData.md)
 - [CreateCustomFileResponse](docs/CreateCustomFileResponse.md)
 - [CreateFolderData](docs/CreateFolderData.md)
 - [CreateHtmlTemplateData](docs/CreateHtmlTemplateData.md)
 - [CreateSubmissionBatchResponse](docs/CreateSubmissionBatchResponse.md)
 - [CreateSubmissionBatchSubmissionsResponse](docs/CreateSubmissionBatchSubmissionsResponse.md)
 - [CreateSubmissionDataRequestData](docs/CreateSubmissionDataRequestData.md)
 - [CreateSubmissionDataRequestTokenResponse](docs/CreateSubmissionDataRequestTokenResponse.md)
 - [CreateSubmissionDataRequestTokenResponseToken](docs/CreateSubmissionDataRequestTokenResponseToken.md)
 - [CreateSubmissionResponse](docs/CreateSubmissionResponse.md)
 - [CreateTemplateFromUploadData](docs/CreateTemplateFromUploadData.md)
 - [CustomFile](docs/CustomFile.md)
 - [Error](docs/Error.md)
 - [Folder](docs/Folder.md)
 - [FoldersFolder](docs/FoldersFolder.md)
 - [HtmlTemplateData](docs/HtmlTemplateData.md)
 - [InvalidRequest](docs/InvalidRequest.md)
 - [ListSubmissionsResponse](docs/ListSubmissionsResponse.md)
 - [MoveFolderData](docs/MoveFolderData.md)
 - [MoveTemplateData](docs/MoveTemplateData.md)
 - [PendingTemplate](docs/PendingTemplate.md)
 - [RenameFolderData](docs/RenameFolderData.md)
 - [Submission](docs/Submission.md)
 - [SubmissionAction](docs/SubmissionAction.md)
 - [SubmissionBatch](docs/SubmissionBatch.md)
 - [SubmissionBatchData](docs/SubmissionBatchData.md)
 - [SubmissionData](docs/SubmissionData.md)
 - [SubmissionDataBatchRequest](docs/SubmissionDataBatchRequest.md)
 - [SubmissionDataRequest](docs/SubmissionDataRequest.md)
 - [Template](docs/Template.md)
 - [Template1](docs/Template1.md)
 - [Template1Defaults](docs/Template1Defaults.md)
 - [TemplateData](docs/TemplateData.md)
 - [TemplatestemplateIdaddFieldsFields](docs/TemplatestemplateIdaddFieldsFields.md)
 - [UpdateDataRequestResponse](docs/UpdateDataRequestResponse.md)
 - [UpdateSubmissionDataRequestData](docs/UpdateSubmissionDataRequestData.md)
 - [UpdateTemplateData](docs/UpdateTemplateData.md)
 - [UpdateTemplateResponse](docs/UpdateTemplateResponse.md)
 - [UploadTemplateData](docs/UploadTemplateData.md)
 - [UploadTemplateDataDocument](docs/UploadTemplateDataDocument.md)
 - [UploadTemplateDataDocumentMetadata](docs/UploadTemplateDataDocumentMetadata.md)


## Documentation For Authorization


## api_token_basic

- **Type**: HTTP basic authentication


## Author




