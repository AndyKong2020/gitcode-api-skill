# Update Pull Request Information
Source: [https://docs.gitcode.com/en/docs/apis/patch-api-v-5-repos-owner-repo-pulls-number](https://docs.gitcode.com/en/docs/apis/patch-api-v-5-repos-owner-repo-pulls-number)
Category: Pull Requests
- Method: `PATCH`
- Path: `/api/v5/repos/{owner}/{repo}/pulls/{number}`
- Operation ID: `patch_api_v5_repos_{owner}_{repo}_pulls_{number}`
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
    "body": {
      "description": "Optional. Content of the Pull Request",
      "type": "string"
    },
    "close_related_issue": {
      "description": "Optional, whether to close associated Issues after merging, default is set according to the repository configuration",
      "type": "boolean"
    },
    "draft": {
      "description": "Whether to set as draft",
      "type": "boolean"
    },
    "labels": {
      "description": "A comma-separated list of labels, where the name must be between 2-20 characters long and cannot contain special characters. For example: bug,performance",
      "type": "string"
    },
    "milestone_number": {
      "description": "Optional. Milestone sequence number (id)",
      "type": "integer"
    },
    "state": {
      "description": "Optional. Pull Request status",
      "type": "string"
    },
    "title": {
      "description": "Optional. Pull Request title",
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
    "body": {
      "type": "string"
    },
    "created_at": {
      "type": "string"
    },
    "state": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "updated_at": {
      "type": "string"
    }
  },
  "type": "object"
}
```
Example:
```json
{
  "body": "new: Added file test_b3 \n2223333444444",
  "created_at": "2024-03-28T22:23:29.999+08:00",
  "state": "opened",
  "title": "test_b3->dev",
  "updated_at": "2024-04-14T21:06:52.499+08:00"
}
```
## JSON Request Example
```json
{
  "body": "string",
  "close_related_issue": true,
  "draft": true,
  "labels": "string",
  "milestone_number": 0,
  "state": "string",
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
    "body": "string",
    "close_related_issue": true,
    "draft": true,
    "labels": "string",
    "milestone_number": 0,
    "state": "string",
    "title": "string"
  },
  "method": "patch",
  "operationId": "patch_api_v5_repos_{owner}_{repo}_pulls_{number}",
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
  "path": "/api/v5/repos/{owner}/{repo}/pulls/{number}",
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
    "method": "PATCH",
    "name": "Update Pull Request Information",
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
        ":number"
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
            "body": {
              "description": "Optional. Content of the Pull Request",
              "type": "string"
            },
            "close_related_issue": {
              "description": "Optional, whether to close associated Issues after merging, default is set according to the repository configuration",
              "type": "boolean"
            },
            "draft": {
              "description": "Whether to set as draft",
              "type": "boolean"
            },
            "labels": {
              "description": "A comma-separated list of labels, where the name must be between 2-20 characters long and cannot contain special characters. For example: bug,performance",
              "type": "string"
            },
            "milestone_number": {
              "description": "Optional. Milestone sequence number (id)",
              "type": "integer"
            },
            "state": {
              "description": "Optional. Pull Request status",
              "type": "string"
            },
            "title": {
              "description": "Optional. Pull Request title",
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
            "body": "new: Added file test_b3 \n2223333444444",
            "created_at": "2024-03-28T22:23:29.999+08:00",
            "state": "opened",
            "title": "test_b3->dev",
            "updated_at": "2024-04-14T21:06:52.499+08:00"
          },
          "schema": {
            "properties": {
              "body": {
                "type": "string"
              },
              "created_at": {
                "type": "string"
              },
              "state": {
                "type": "string"
              },
              "title": {
                "type": "string"
              },
              "updated_at": {
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
