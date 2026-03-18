# Get the upload address of the Release attachment
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-releases-tag-upload-url](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-releases-tag-upload-url)
Category: Release
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/releases/{tag}/upload_url`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_releases_{tag}_upload_url`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path |
| tag | path | true | string | tag name |
| access_token | query | true | string | User authorization code |
| file_name | query | true | string | File name to be uploaded |
## Request Body
No request body.
## Responses
### `200`
Headers:
```json
{}
```
#### `application/json`
Schema:
```json
{
  "properties": {
    "headers": {
      "description": "The request headers required for uploading.",
      "properties": {
        "Content-Type": {
          "type": "string"
        },
        "x-obs-acl": {
          "type": "string"
        },
        "x-obs-callback": {
          "type": "string"
        },
        "x-obs-meta-project-id": {
          "type": "string"
        }
      },
      "required": [
        "x-obs-meta-project-id",
        "x-obs-acl",
        "x-obs-callback",
        "Content-Type"
      ],
      "type": "object"
    },
    "url": {
      "description": "Please translate the following content professionally into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any content other than the translation!! The address for uploading is sent via a PUT request.",
      "type": "string"
    }
  },
  "required": [
    "url",
    "headers"
  ],
  "type": "object"
}
```
## Raw OpenAPI Operation
```json
{
  "deprecated": false,
  "description": "",
  "info": {
    "description": "",
    "title": "GicodeOpenAPI",
    "version": "1.0.0"
  },
  "method": "get",
  "operationId": "get_api_v5_repos_{owner}_{repo}_releases_{tag}_upload_url",
  "parameters": [
    {
      "description": "Repository space address (address path of the enterprise, organization, or individual)",
      "in": "path",
      "name": "owner",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Repository path",
      "in": "path",
      "name": "repo",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "tag name",
      "in": "path",
      "name": "tag",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "User authorization code",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "File name to be uploaded",
      "in": "query",
      "name": "file_name",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/releases/{tag}/upload_url",
  "postman": {
    "description": {
      "content": "",
      "type": "text/plain"
    },
    "header": [
      {
        "key": "Accept",
        "value": "application/json"
      }
    ],
    "method": "GET",
    "name": "Get the upload address of the Release attachment",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "repos",
        ":owner",
        ":repo",
        "releases",
        ":tag",
        "upload_url"
      ],
      "query": [
        {
          "description": {
            "content": "(Required) User authorization code",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "access_token",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) File name to be uploaded",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "file_name",
          "value": ""
        }
      ],
      "variable": [
        {
          "description": {
            "content": "(Required) Repository space address (address path of the enterprise, organization, or individual)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "owner",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) Repository path",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "repo",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) tag name",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "tag",
          "type": "any",
          "value": ""
        }
      ]
    }
  },
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "schema": {
            "properties": {
              "headers": {
                "description": "The request headers required for uploading.",
                "properties": {
                  "Content-Type": {
                    "type": "string"
                  },
                  "x-obs-acl": {
                    "type": "string"
                  },
                  "x-obs-callback": {
                    "type": "string"
                  },
                  "x-obs-meta-project-id": {
                    "type": "string"
                  }
                },
                "required": [
                  "x-obs-meta-project-id",
                  "x-obs-acl",
                  "x-obs-callback",
                  "Content-Type"
                ],
                "type": "object"
              },
              "url": {
                "description": "Please translate the following content professionally into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any content other than the translation!! The address for uploading is sent via a PUT request.",
                "type": "string"
              }
            },
            "required": [
              "url",
              "headers"
            ],
            "type": "object"
          }
        }
      },
      "description": "",
      "headers": {}
    }
  },
  "security": [],
  "securitySchemes": {},
  "servers": [
    {
      "description": "正式环境",
      "url": "https://api.gitcode.com"
    }
  ],
  "tags": []
}
```
