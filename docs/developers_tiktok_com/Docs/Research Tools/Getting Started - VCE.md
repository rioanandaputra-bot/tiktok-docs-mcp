Docs
# Getting Started
This guide shows you how to access and use the Virtual Compute Environment (VCE), a secure space that allows you to query and analyze public data.
# How does the Virtual Compute Environment work?
The VCE allows you to access and analyze TikTok's public data in two stages. These stages are meant to protect user privacy and help organize your data analysis.
- **Test Stage**: Query the data using TikTok's query software development kit (SDK). The VCE will return random sample data based on your query, limited to 5,000 records per day. The data here is limited to data of users who have at least 25,000 followers.
- **Execution Stage**: Submit a script to execute against all public data. TikTok provides a powerful search capability that allows data to be paginated in increments of up to 100,000 records. TikTok will review the results file to make sure the output is **aggregated**.
- **NOTE**: Please ensure that the scripts submitted are looking to get aggregated outputs. Scripts that request individual data will be rejected.
- Examples of Acceptable Outputs:
- Descriptive statistics (for example, mean, standard deviation, skewness)
- Inferential statistics (for example, Z-scores, regression coefficients)
- Topic model results or word clouds
Note: TikTok only reviews the results to ensure that there is no identifiable individual information extracted out of the platform. All aggregated results will be shared as a downloadable link to the approved primary researcher's email.
# View your client registration
[[Once your application is approved, a research client will be generated for your project. You can view your approved research projects on your **Research projects](https://developers.tiktok.com/research/)** page](https://developers.tiktok.com/research/). Select a project from the list to view the research client details.
The provided **Client key** and **Client secret** are required to access the VCE. The client key and secret are hidden by default but can be displayed by clicking the **Display** button (eye icon).
Note: The client secret is a credential used to authenticate your connection to TikTok's Research Tools. Do not share this with anyone!
# Log in to the Virtual Compute Environment
[First, go to the Virtual Compute Environment login page](https://research.tiktok.com/virtual-compute-environment/hub/).
Then, sign in using your **Client key** as the **Username** and your **Client secret** as the **Password**.
# Use the Virtual Compute Environment
## Test Stage: Query TikTok's public data
In the Test Stage, you will submit a query to access random sample public data about videos, comments, and users. You can retrieve up to 5000 records per day from creators who have at least 25,000 followers.
Note: If you want to analyze all public user data, you must submit a script to the VCE, as explained later in this guide.
### Install query SDK
After logging into the VCE, click the **New Launcher** [**+**] button. Then open a new notebook, choosing the **Python 3 (ipykernel)** option.
Copy and paste the following code into the terminal, then run the code to install the query SDK from TikTok.
```
!pip install \
-U --index-url https://us-west2-python.pkg.dev/research-platform-prod/jupyterlab-extensions-prod/simple/ \
pyrqs
```
### Set query parameters
You must structure your query according to the following guidelines. Use the query structure example code below as a framework for formatting your query.
#### Data category
Indicate what `category` of data you want to query. The available data categories are described in the respective reference pages:
- [Query Profiles](https://developers.tiktok.com/doc/vce-query-profiles/)
- [Query Videos](https://developers.tiktok.com/doc/vce-query-videos/)
- [Query Video Comments](https://developers.tiktok.com/doc/vce-query-video-comments/)
#### Condition groups
Create your query `condition_groups` using the listed field names, operations, and boolean operators.
**Field names**
The following are the `field_name` values:
- `create_time`
- `display_name`
- `region_code`
- `id`
- `video_description`
- `hashtag_name`
- `music_id`
- `like_count`
- `comment_count`
- `share_count`
- `view_count`
- `effect_ids`
- `hashtag_names`
- `playlist_id`
- `voice_to_text`
- `duration_type`
- `video_length`
**Operations**
The following are the `operation` values:
- `IN`: Tests if an expression matches any value in a list of values
- `EQ`: Tests if an expression matches the specified value
- `GT`: Tests if an expression is strictly greater than the specified value
- `GTE`: Tests if an expression is greater than or equal to the specified value
- `LT`: Tests if an expression is strictly less than the specified value
- `LTE`: Tests if an expression is less than or equal to the specified value
- `LIKE`: Available for video_description, returns the rows if it contains a specified value
- `CONTAINS`: Available for `effect_ids` and `hashtag_names`, returns the rows if they contain the specified `effect_ids` or `hashtag_names`
**Boolean operators**
Conditions are grouped by the following boolean operators:
- `AND`: Displays a record if all the conditions separated by `AND` are `TRUE`
- `OR`: Displays a record if any of the conditions separated by `OR` is `TRUE`
- `NOT`: Displays a record if all the conditions separated by `NOT` are `FALSE`
#### Fields, limit, and client
Specify the `fields` to be returned in the query results, and a `limit` indicating the maximum number of records to return. Create a `client`, such as RQSClient, to interact with the query service.
### Query structure example
Below is a complete sample command that can be executed in the VCE. This example defines a data variable and prints the data received by the query to display it on the VCE.
**Example code**
```
from pyrqs import rqs

category = 'video'
condition_groups = [
    {
        "operator": "and",
        "conditions": [
            {
                "field": "like_count",
                "operator": "gte",
                "field_values": ["10"]
            }
        ]
    }
]
fields = 'username,video_description,create_time,id'
limit = 10
client = rqs.RQSClient()
data = client.query(
            category=category, condition_groups=condition_groups, fields=fields, limit=limit)
print(data)
```
The data from this sample code should be displayed on the VCE, as below.
## Execution Stage: Submit script to analyze data
After you have queried the data and understood the metadata structure, you can run a script to analyze all TikTok's public data. Please make sure that the output of your script at this stage does not contain individual-level data.
To submit a script to the VCE, do the following:
- Click the shield icon on the right sidebar.
- Select your script file in the right sidebar, then click the upload button.
- When prompted to submit a job to Data Clean Room, click the **Ok** button.
- Once submitted, your script will run in a trusted execution environment to analyze and prepare the results file.
- TikTok will review the results to verify that results are aggregated and do not contain individual data.
- After the results are verified, TikTok will send an email to the primary researcher to download the approved results file.
Was this document helpful?