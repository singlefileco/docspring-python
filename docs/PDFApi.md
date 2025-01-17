# docspring.PDFApi

All URIs are relative to *https://api.docspring.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_fields_to_template**](PDFApi.md#add_fields_to_template) | **PUT** /templates/{template_id}/add_fields | Add new fields to a Template
[**batch_generate_pdf_v1**](PDFApi.md#batch_generate_pdf_v1) | **POST** /templates/{template_id}/submissions/batch | Generates multiple PDFs
[**batch_generate_pdfs**](PDFApi.md#batch_generate_pdfs) | **POST** /submissions/batches | Generates multiple PDFs
[**combine_pdfs**](PDFApi.md#combine_pdfs) | **POST** /combined_submissions?v&#x3D;2 | Merge submission PDFs, template PDFs, or custom files
[**combine_submissions**](PDFApi.md#combine_submissions) | **POST** /combined_submissions | Merge generated PDFs together
[**copy_template**](PDFApi.md#copy_template) | **POST** /templates/{template_id}/copy | Copy a Template
[**create_custom_file_from_upload**](PDFApi.md#create_custom_file_from_upload) | **POST** /custom_files | Create a new custom file from a cached presign upload
[**create_data_request_token**](PDFApi.md#create_data_request_token) | **POST** /data_requests/{data_request_id}/tokens | Creates a new data request token for form authentication
[**create_folder**](PDFApi.md#create_folder) | **POST** /folders/ | Create a folder
[**create_html_template**](PDFApi.md#create_html_template) | **POST** /templates?desc&#x3D;html | Create a new HTML template
[**create_pdf_template**](PDFApi.md#create_pdf_template) | **POST** /templates | Create a new PDF template with a form POST file upload
[**create_pdf_template_from_upload**](PDFApi.md#create_pdf_template_from_upload) | **POST** /templates?desc&#x3D;cached_upload | Create a new PDF template from a cached presign upload
[**delete_folder**](PDFApi.md#delete_folder) | **DELETE** /folders/{folder_id} | Delete a folder
[**expire_combined_submission**](PDFApi.md#expire_combined_submission) | **DELETE** /combined_submissions/{combined_submission_id} | Expire a combined submission
[**expire_submission**](PDFApi.md#expire_submission) | **DELETE** /submissions/{submission_id} | Expire a PDF submission
[**generate_pdf**](PDFApi.md#generate_pdf) | **POST** /templates/{template_id}/submissions | Generates a new PDF
[**get_combined_submission**](PDFApi.md#get_combined_submission) | **GET** /combined_submissions/{combined_submission_id} | Check the status of a combined submission (merged PDFs)
[**get_data_request**](PDFApi.md#get_data_request) | **GET** /data_requests/{data_request_id} | Look up a submission data request
[**get_full_template**](PDFApi.md#get_full_template) | **GET** /templates/{template_id}?full&#x3D;true | Fetch the full template attributes
[**get_presign_url**](PDFApi.md#get_presign_url) | **GET** /uploads/presign | Get a presigned URL so that you can upload a file to our AWS S3 bucket
[**get_submission**](PDFApi.md#get_submission) | **GET** /submissions/{submission_id} | Check the status of a PDF
[**get_submission_batch**](PDFApi.md#get_submission_batch) | **GET** /submissions/batches/{submission_batch_id} | Check the status of a submission batch job
[**get_template**](PDFApi.md#get_template) | **GET** /templates/{template_id} | Check the status of an uploaded template
[**get_template_schema**](PDFApi.md#get_template_schema) | **GET** /templates/{template_id}/schema | Fetch the JSON schema for a template
[**list_folders**](PDFApi.md#list_folders) | **GET** /folders/ | Get a list of all folders
[**list_submissions**](PDFApi.md#list_submissions) | **GET** /submissions | List all submissions
[**list_submissions_0**](PDFApi.md#list_submissions_0) | **GET** /templates/{template_id}/submissions | List all submissions for a given template
[**list_templates**](PDFApi.md#list_templates) | **GET** /templates | Get a list of all templates
[**move_folder_to_folder**](PDFApi.md#move_folder_to_folder) | **POST** /folders/{folder_id}/move | Move a folder
[**move_template_to_folder**](PDFApi.md#move_template_to_folder) | **POST** /templates/{template_id}/move | Move Template to folder
[**rename_folder**](PDFApi.md#rename_folder) | **POST** /folders/{folder_id}/rename | Rename a folder
[**test_authentication**](PDFApi.md#test_authentication) | **GET** /authentication | Test Authentication
[**update_data_request**](PDFApi.md#update_data_request) | **PUT** /data_requests/{data_request_id} | Update a submission data request
[**update_template**](PDFApi.md#update_template) | **PUT** /templates/{template_id} | Update a Template


# **add_fields_to_template**
> AddFieldsTemplateResponse add_fields_to_template(template_id, add_fields_data)

Add new fields to a Template

### Example

* Basic Authentication (api_token_basic): 
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **add_fields_data** | [**AddFieldsData**](AddFieldsData.md)|  | 

### Return type

[**AddFieldsTemplateResponse**](AddFieldsTemplateResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_generate_pdf_v1**
> list[CreateSubmissionResponse] batch_generate_pdf_v1(template_id, request_body)

Generates multiple PDFs

### Example

* Basic Authentication (api_token_basic): 
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
template_id = 'tpl_000000000000000001' # str | 
request_body = NULL # list[object] | 

try:
    # Generates multiple PDFs
    api_response = api_instance.batch_generate_pdf_v1(template_id, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->batch_generate_pdf_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **request_body** | [**list[object]**](list.md)|  | 

### Return type

[**list[CreateSubmissionResponse]**](CreateSubmissionResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_generate_pdfs**
> CreateSubmissionBatchResponse batch_generate_pdfs(submission_batch_data)

Generates multiple PDFs

### Example

* Basic Authentication (api_token_basic): 
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
submission_batch_data = docspring.SubmissionBatchData() # SubmissionBatchData | 

try:
    # Generates multiple PDFs
    api_response = api_instance.batch_generate_pdfs(submission_batch_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->batch_generate_pdfs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_batch_data** | [**SubmissionBatchData**](SubmissionBatchData.md)|  | 

### Return type

[**CreateSubmissionBatchResponse**](CreateSubmissionBatchResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **combine_pdfs**
> CreateCombinedSubmissionResponse combine_pdfs(combine_pdfs_data)

Merge submission PDFs, template PDFs, or custom files

### Example

* Basic Authentication (api_token_basic): 
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
combine_pdfs_data = docspring.CombinePdfsData() # CombinePdfsData | 

try:
    # Merge submission PDFs, template PDFs, or custom files
    api_response = api_instance.combine_pdfs(combine_pdfs_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->combine_pdfs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **combine_pdfs_data** | [**CombinePdfsData**](CombinePdfsData.md)|  | 

### Return type

[**CreateCombinedSubmissionResponse**](CreateCombinedSubmissionResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **combine_submissions**
> CreateCombinedSubmissionResponse combine_submissions(combined_submission_data)

Merge generated PDFs together

### Example

* Basic Authentication (api_token_basic): 
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
combined_submission_data = docspring.CombinedSubmissionData() # CombinedSubmissionData | 

try:
    # Merge generated PDFs together
    api_response = api_instance.combine_submissions(combined_submission_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->combine_submissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **combined_submission_data** | [**CombinedSubmissionData**](CombinedSubmissionData.md)|  | 

### Return type

[**CreateCombinedSubmissionResponse**](CreateCombinedSubmissionResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_template**
> Template copy_template(template_id, copy_template_data)

Copy a Template

### Example

* Basic Authentication (api_token_basic): 
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
template_id = 'tpl_000000000000000001' # str | 
copy_template_data = docspring.CopyTemplateData() # CopyTemplateData | 

try:
    # Copy a Template
    api_response = api_instance.copy_template(template_id, copy_template_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->copy_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **copy_template_data** | [**CopyTemplateData**](CopyTemplateData.md)|  | 

### Return type

[**Template**](Template.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_file_from_upload**
> CreateCustomFileResponse create_custom_file_from_upload(create_custom_file_data)

Create a new custom file from a cached presign upload

### Example

* Basic Authentication (api_token_basic): 
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
create_custom_file_data = docspring.CreateCustomFileData() # CreateCustomFileData | 

try:
    # Create a new custom file from a cached presign upload
    api_response = api_instance.create_custom_file_from_upload(create_custom_file_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->create_custom_file_from_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_custom_file_data** | [**CreateCustomFileData**](CreateCustomFileData.md)|  | 

### Return type

[**CreateCustomFileResponse**](CreateCustomFileResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_data_request_token**
> CreateSubmissionDataRequestTokenResponse create_data_request_token(data_request_id)

Creates a new data request token for form authentication

### Example

* Basic Authentication (api_token_basic): 
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
data_request_id = 'drq_000000000000000001' # str | 

try:
    # Creates a new data request token for form authentication
    api_response = api_instance.create_data_request_token(data_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->create_data_request_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_request_id** | **str**|  | 

### Return type

[**CreateSubmissionDataRequestTokenResponse**](CreateSubmissionDataRequestTokenResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> Folder create_folder(create_folder_data)

Create a folder

### Example

* Basic Authentication (api_token_basic): 
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
create_folder_data = docspring.CreateFolderData() # CreateFolderData | 

try:
    # Create a folder
    api_response = api_instance.create_folder(create_folder_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->create_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_folder_data** | [**CreateFolderData**](CreateFolderData.md)|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_html_template**
> PendingTemplate create_html_template(create_html_template_data)

Create a new HTML template

### Example

* Basic Authentication (api_token_basic): 
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
create_html_template_data = docspring.CreateHtmlTemplateData() # CreateHtmlTemplateData | 

try:
    # Create a new HTML template
    api_response = api_instance.create_html_template(create_html_template_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->create_html_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_html_template_data** | [**CreateHtmlTemplateData**](CreateHtmlTemplateData.md)|  | 

### Return type

[**PendingTemplate**](PendingTemplate.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pdf_template**
> PendingTemplate create_pdf_template(template_document, template_name, template_parent_folder_id=template_parent_folder_id)

Create a new PDF template with a form POST file upload

### Example

* Basic Authentication (api_token_basic): 
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
template_document = '/path/to/file' # file | 
template_name = 'template_name_example' # str | 
template_parent_folder_id = 'template_parent_folder_id_example' # str |  (optional)

try:
    # Create a new PDF template with a form POST file upload
    api_response = api_instance.create_pdf_template(template_document, template_name, template_parent_folder_id=template_parent_folder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->create_pdf_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_document** | **file**|  | 
 **template_name** | **str**|  | 
 **template_parent_folder_id** | **str**|  | [optional] 

### Return type

[**PendingTemplate**](PendingTemplate.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pdf_template_from_upload**
> PendingTemplate create_pdf_template_from_upload(create_template_from_upload_data)

Create a new PDF template from a cached presign upload

### Example

* Basic Authentication (api_token_basic): 
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
create_template_from_upload_data = docspring.CreateTemplateFromUploadData() # CreateTemplateFromUploadData | 

try:
    # Create a new PDF template from a cached presign upload
    api_response = api_instance.create_pdf_template_from_upload(create_template_from_upload_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->create_pdf_template_from_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_template_from_upload_data** | [**CreateTemplateFromUploadData**](CreateTemplateFromUploadData.md)|  | 

### Return type

[**PendingTemplate**](PendingTemplate.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> Folder delete_folder(folder_id)

Delete a folder

### Example

* Basic Authentication (api_token_basic): 
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
folder_id = 'fld_000000000000000001' # str | 

try:
    # Delete a folder
    api_response = api_instance.delete_folder(folder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->delete_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **expire_combined_submission**
> CombinedSubmission expire_combined_submission(combined_submission_id)

Expire a combined submission

### Example

* Basic Authentication (api_token_basic): 
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
combined_submission_id = 'com_000000000000000001' # str | 

try:
    # Expire a combined submission
    api_response = api_instance.expire_combined_submission(combined_submission_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->expire_combined_submission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **combined_submission_id** | **str**|  | 

### Return type

[**CombinedSubmission**](CombinedSubmission.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **expire_submission**
> Submission expire_submission(submission_id)

Expire a PDF submission

### Example

* Basic Authentication (api_token_basic): 
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
submission_id = 'sub_000000000000000001' # str | 

try:
    # Expire a PDF submission
    api_response = api_instance.expire_submission(submission_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->expire_submission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **str**|  | 

### Return type

[**Submission**](Submission.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_pdf**
> CreateSubmissionResponse generate_pdf(template_id, submission_data)

Generates a new PDF

### Example

* Basic Authentication (api_token_basic): 
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
template_id = 'tpl_000000000000000001' # str | 
submission_data = docspring.SubmissionData() # SubmissionData | 

try:
    # Generates a new PDF
    api_response = api_instance.generate_pdf(template_id, submission_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->generate_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **submission_data** | [**SubmissionData**](SubmissionData.md)|  | 

### Return type

[**CreateSubmissionResponse**](CreateSubmissionResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_combined_submission**
> CombinedSubmission get_combined_submission(combined_submission_id)

Check the status of a combined submission (merged PDFs)

### Example

* Basic Authentication (api_token_basic): 
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
combined_submission_id = 'com_000000000000000001' # str | 

try:
    # Check the status of a combined submission (merged PDFs)
    api_response = api_instance.get_combined_submission(combined_submission_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->get_combined_submission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **combined_submission_id** | **str**|  | 

### Return type

[**CombinedSubmission**](CombinedSubmission.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_request**
> SubmissionDataRequest get_data_request(data_request_id)

Look up a submission data request

### Example

* Basic Authentication (api_token_basic): 
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
data_request_id = 'drq_000000000000000001' # str | 

try:
    # Look up a submission data request
    api_response = api_instance.get_data_request(data_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->get_data_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_request_id** | **str**|  | 

### Return type

[**SubmissionDataRequest**](SubmissionDataRequest.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_full_template**
> Template1 get_full_template(template_id)

Fetch the full template attributes

### Example

* Basic Authentication (api_token_basic): 
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
template_id = 'tpl_000000000000000001' # str | 

try:
    # Fetch the full template attributes
    api_response = api_instance.get_full_template(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->get_full_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

[**Template1**](Template1.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_presign_url**
> dict(str, object) get_presign_url()

Get a presigned URL so that you can upload a file to our AWS S3 bucket

### Example

* Basic Authentication (api_token_basic): 
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

try:
    # Get a presigned URL so that you can upload a file to our AWS S3 bucket
    api_response = api_instance.get_presign_url()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->get_presign_url: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, object)**

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submission**
> Submission get_submission(submission_id, include_data=include_data)

Check the status of a PDF

### Example

* Basic Authentication (api_token_basic): 
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
submission_id = 'sub_000000000000000001' # str | 
include_data = true # bool |  (optional)

try:
    # Check the status of a PDF
    api_response = api_instance.get_submission(submission_id, include_data=include_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->get_submission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **str**|  | 
 **include_data** | **bool**|  | [optional] 

### Return type

[**Submission**](Submission.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submission_batch**
> SubmissionBatch get_submission_batch(submission_batch_id, include_submissions=include_submissions)

Check the status of a submission batch job

### Example

* Basic Authentication (api_token_basic): 
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
submission_batch_id = 'sbb_000000000000000001' # str | 
include_submissions = true # bool |  (optional)

try:
    # Check the status of a submission batch job
    api_response = api_instance.get_submission_batch(submission_batch_id, include_submissions=include_submissions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->get_submission_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_batch_id** | **str**|  | 
 **include_submissions** | **bool**|  | [optional] 

### Return type

[**SubmissionBatch**](SubmissionBatch.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template**
> Template get_template(template_id)

Check the status of an uploaded template

### Example

* Basic Authentication (api_token_basic): 
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
template_id = 'tpl_000000000000000001' # str | 

try:
    # Check the status of an uploaded template
    api_response = api_instance.get_template(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->get_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

[**Template**](Template.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template_schema**
> dict(str, object) get_template_schema(template_id)

Fetch the JSON schema for a template

### Example

* Basic Authentication (api_token_basic): 
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
template_id = 'tpl_000000000000000001' # str | 

try:
    # Fetch the JSON schema for a template
    api_response = api_instance.get_template_schema(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->get_template_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

**dict(str, object)**

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_folders**
> list[Folder] list_folders(parent_folder_id=parent_folder_id)

Get a list of all folders

### Example

* Basic Authentication (api_token_basic): 
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
parent_folder_id = 'fld_000000000000000002' # str | Filter By Folder Id (optional)

try:
    # Get a list of all folders
    api_response = api_instance.list_folders(parent_folder_id=parent_folder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->list_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_folder_id** | **str**| Filter By Folder Id | [optional] 

### Return type

[**list[Folder]**](Folder.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_submissions**
> ListSubmissionsResponse list_submissions(cursor=cursor, limit=limit, created_after=created_after, created_before=created_before, type=type, include_data=include_data)

List all submissions

### Example

* Basic Authentication (api_token_basic): 
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
cursor = 'sub_list_000012' # str |  (optional)
limit = 3 # float |  (optional)
created_after = '2019-01-01T09:00:00-05:00' # str |  (optional)
created_before = '2020-01-01T09:00:00-05:00' # str |  (optional)
type = 'test' # str |  (optional)
include_data = true # bool |  (optional)

try:
    # List all submissions
    api_response = api_instance.list_submissions(cursor=cursor, limit=limit, created_after=created_after, created_before=created_before, type=type, include_data=include_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->list_submissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional] 
 **limit** | **float**|  | [optional] 
 **created_after** | **str**|  | [optional] 
 **created_before** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **include_data** | **bool**|  | [optional] 

### Return type

[**ListSubmissionsResponse**](ListSubmissionsResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_submissions_0**
> ListSubmissionsResponse list_submissions_0(template_id, cursor=cursor, limit=limit, created_after=created_after, created_before=created_before, type=type, include_data=include_data)

List all submissions for a given template

### Example

* Basic Authentication (api_token_basic): 
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
cursor = 'cursor_example' # str |  (optional)
limit = 3.4 # float |  (optional)
created_after = 'created_after_example' # str |  (optional)
created_before = 'created_before_example' # str |  (optional)
type = 'type_example' # str |  (optional)
include_data = true # bool |  (optional)

try:
    # List all submissions for a given template
    api_response = api_instance.list_submissions_0(template_id, cursor=cursor, limit=limit, created_after=created_after, created_before=created_before, type=type, include_data=include_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->list_submissions_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **cursor** | **str**|  | [optional] 
 **limit** | **float**|  | [optional] 
 **created_after** | **str**|  | [optional] 
 **created_before** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **include_data** | **bool**|  | [optional] 

### Return type

[**ListSubmissionsResponse**](ListSubmissionsResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_templates**
> list[Template] list_templates(query=query, parent_folder_id=parent_folder_id, page=page, per_page=per_page)

Get a list of all templates

### Example

* Basic Authentication (api_token_basic): 
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
query = '2' # str | Search By Name (optional)
parent_folder_id = 'fld_000000000000000001' # str | Filter By Folder Id (optional)
page = 2 # int | Default: 1 (optional)
per_page = 1 # int | Default: 50 (optional)

try:
    # Get a list of all templates
    api_response = api_instance.list_templates(query=query, parent_folder_id=parent_folder_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->list_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search By Name | [optional] 
 **parent_folder_id** | **str**| Filter By Folder Id | [optional] 
 **page** | **int**| Default: 1 | [optional] 
 **per_page** | **int**| Default: 50 | [optional] 

### Return type

[**list[Template]**](Template.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_folder_to_folder**
> Folder move_folder_to_folder(folder_id, move_folder_data)

Move a folder

### Example

* Basic Authentication (api_token_basic): 
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
folder_id = 'fld_000000000000000001' # str | 
move_folder_data = docspring.MoveFolderData() # MoveFolderData | 

try:
    # Move a folder
    api_response = api_instance.move_folder_to_folder(folder_id, move_folder_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->move_folder_to_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 
 **move_folder_data** | [**MoveFolderData**](MoveFolderData.md)|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_template_to_folder**
> Template move_template_to_folder(template_id, move_template_data)

Move Template to folder

### Example

* Basic Authentication (api_token_basic): 
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
template_id = 'tpl_000000000000000001' # str | 
move_template_data = docspring.MoveTemplateData() # MoveTemplateData | 

try:
    # Move Template to folder
    api_response = api_instance.move_template_to_folder(template_id, move_template_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->move_template_to_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **move_template_data** | [**MoveTemplateData**](MoveTemplateData.md)|  | 

### Return type

[**Template**](Template.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_folder**
> rename_folder(folder_id, rename_folder_data)

Rename a folder

### Example

* Basic Authentication (api_token_basic): 
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
folder_id = 'fld_000000000000000001' # str | 
rename_folder_data = docspring.RenameFolderData() # RenameFolderData | 

try:
    # Rename a folder
    api_instance.rename_folder(folder_id, rename_folder_data)
except ApiException as e:
    print("Exception when calling PDFApi->rename_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 
 **rename_folder_data** | [**RenameFolderData**](RenameFolderData.md)|  | 

### Return type

void (empty response body)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_authentication**
> AuthenticationSuccessResponse test_authentication()

Test Authentication

### Example

* Basic Authentication (api_token_basic): 
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

try:
    # Test Authentication
    api_response = api_instance.test_authentication()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->test_authentication: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthenticationSuccessResponse**](AuthenticationSuccessResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_request**
> UpdateDataRequestResponse update_data_request(data_request_id, update_submission_data_request_data)

Update a submission data request

### Example

* Basic Authentication (api_token_basic): 
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
data_request_id = 'drq_000000000000000001' # str | 
update_submission_data_request_data = docspring.UpdateSubmissionDataRequestData() # UpdateSubmissionDataRequestData | 

try:
    # Update a submission data request
    api_response = api_instance.update_data_request(data_request_id, update_submission_data_request_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->update_data_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_request_id** | **str**|  | 
 **update_submission_data_request_data** | [**UpdateSubmissionDataRequestData**](UpdateSubmissionDataRequestData.md)|  | 

### Return type

[**UpdateDataRequestResponse**](UpdateDataRequestResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template**
> UpdateTemplateResponse update_template(template_id, update_template_data)

Update a Template

### Example

* Basic Authentication (api_token_basic): 
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
template_id = 'tpl_000000000000000003' # str | 
update_template_data = docspring.UpdateTemplateData() # UpdateTemplateData | 

try:
    # Update a Template
    api_response = api_instance.update_template(template_id, update_template_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDFApi->update_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **update_template_data** | [**UpdateTemplateData**](UpdateTemplateData.md)|  | 

### Return type

[**UpdateTemplateResponse**](UpdateTemplateResponse.md)

### Authorization

[api_token_basic](../README.md#api_token_basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

