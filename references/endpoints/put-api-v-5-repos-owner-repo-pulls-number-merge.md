# Merge Pull Request
Source: [https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-pulls-number-merge](https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-pulls-number-merge)
Category: Pull Requests
- Method: `PUT`
- Path: `/api/v5/repos/{owner}/{repo}/pulls/{number}/merge`
- Operation ID: `put_api_v5_repos_{owner}_{repo}_pulls_{number}_merge`
- Tags: `Pull Requests`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| number | path | true | integer | The ordinal number of the PR in this repository, i.e., which PR it is. |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "description": {
      "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation! Optional. Merge description",
      "type": "string"
    },
    "merge_method": {
      "description": "Optional. Method to merge the PR, which can be merge (merge all commits), squash (flatten branch merge), or rebase (rebase and merge). The default is merge.",
      "type": "string"
    },
    "title": {
      "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation! Optional. Merge titles",
      "type": "string"
    }
  },
  "type": "object"
}
```
Example:
```json
""
```
## Responses
### `200`
Successful Response
Headers:
```json
{}
```
#### `application/json`
Schema:
```json
{
  "properties": {
    "merged": {
      "type": "integer"
    },
    "message": {
      "type": "string"
    },
    "sha": {
      "type": "string"
    }
  },
  "type": "object"
}
```
Example:
```json
{
  "merged": true,
  "message": "Pull Request has been successfully merged",
  "sha": "c20ac9624d2811a9313af29769dcf581b60c3044"
}
```
## JSON Request Example
```json
{
  "description": "string",
  "merge_method": "string",
  "title": "string"
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
  "jsonRequestBodyExample": {
    "description": "string",
    "merge_method": "string",
    "title": "string"
  },
  "method": "put",
  "operationId": "put_api_v5_repos_{owner}_{repo}_pulls_{number}_merge",
  "parameters": [
    {
      "description": "Repository space address (organization or individual's address path)",
      "example": "",
      "in": "path",
      "name": "owner",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Repository path (path)",
      "example": "",
      "in": "path",
      "name": "repo",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "The ordinal number of the PR in this repository, i.e., which PR it is.",
      "example": 0,
      "in": "path",
      "name": "number",
      "required": true,
      "schema": {
        "type": "integer"
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
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/pulls/{number}/merge",
  "postman": {
    "body": {
      "mode": "raw",
      "options": {
        "raw": {
          "language": "json"
        }
      },
      "raw": ""
    },
    "description": {
      "content": "",
      "type": "text/plain"
    },
    "header": [
      {
        "key": "Content-Type",
        "value": "application/json"
      },
      {
        "key": "Accept",
        "value": "application/json"
      }
    ],
    "method": "PUT",
    "name": "Merge Pull Request",
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
        "pulls",
        ":number",
        "merge"
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
        }
      ],
      "variable": [
        {
          "description": {
            "content": "(Required) Repository space address (organization or individual's address path)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "owner",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) Repository path (path)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "repo",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) The ordinal number of the PR in this repository, i.e., which PR it is.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "number",
          "type": "any",
          "value": ""
        }
      ]
    }
  },
  "requestBody": {
    "content": {
      "application/json": {
        "example": "",
        "schema": {
          "properties": {
            "description": {
              "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation! Optional. Merge description",
              "type": "string"
            },
            "merge_method": {
              "description": "Optional. Method to merge the PR, which can be merge (merge all commits), squash (flatten branch merge), or rebase (rebase and merge). The default is merge.",
              "type": "string"
            },
            "title": {
              "description": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts besides the translation! Optional. Merge titles",
              "type": "string"
            }
          },
          "type": "object"
        }
      }
    }
  },
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "example": {
            "merged": true,
            "message": "Pull Request has been successfully merged",
            "sha": "c20ac9624d2811a9313af29769dcf581b60c3044"
          },
          "schema": {
            "properties": {
              "merged": {
                "type": "integer"
              },
              "message": {
                "type": "string"
              },
              "sha": {
                "type": "string"
              }
            },
            "type": "object"
          }
        }
      },
      "description": "Successful Response",
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
  "tags": [
    "Pull Requests"
  ]
}
```
