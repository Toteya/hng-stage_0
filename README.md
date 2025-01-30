# HNG Stage 0 - Basic Information Public API

This is a simple public API that returns my basic information.
i.e. my **email address**, the **github URL** of this project, and the current **date and time** (UCT).

## Setup

#### Install dependencies:
`pip install -r requirements.txt`

#### Run the web application:
`python3 -m api.v1.app`

#### Access endpoint locally:
`localhost:5000/api/v1/info`


## API

#### Endpoint URL:
`https://hng-stage-0-0kat.onrender.com/api/v1/info`

#### Request / Response Format
- Resquest:

`GET** https://hng-stage-0-0kat.onrender.com/api/v1/info`

- Response (JSON):

```
{
   "current_datetime" : YYYY-MM-DDTHH:MM:SSZ,
   "email" : EMAIL,
   "github_url" : GITHUB_URL
}
```

#### Example Usage:
- Resquest:

`curl -s https://hng-stage-0-0kat.onrender.com/api/v1/info`

- Response:

```
{
   "current_datetime" : "2025-01-30T13:45:14Z",
   "email" : "twkamanja@gmail.com",
   "github_url" : "https://github.com/Toteya/hng-stage_0"
}
```
