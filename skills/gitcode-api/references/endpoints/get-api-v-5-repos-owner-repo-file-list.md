# Get File List
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-file-list](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-file-list)
Category: Repositories
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/file_list`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_file_list`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
| ref_name | query | false | string | ref (branch, tag, commit) |
| file_name | query | false | string | The name of the file to be searched for. |
## Request Body
No request body.
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
  "items": {
    "type": "string"
  },
  "type": "array"
}
```
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": "abc/test.rs"
  },
  "2": {
    "summary": "Successful Example",
    "value": "bcd/test.rs"
  }
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_file_list",
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
      "description": "User authorization code",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "ref (branch, tag, commit)",
      "in": "query",
      "name": "ref_name",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "The name of the file to be searched for.",
      "in": "query",
      "name": "file_name",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/file_list",
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
    "name": "Get File List",
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
        "file_list"
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
            "content": "ref (branch, tag, commit)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "ref_name",
          "value": ""
        },
        {
          "description": {
            "content": "The name of the file to be searched for.",
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
        }
      ]
    }
  },
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "examples": {
            "1": {
              "summary": "Successful Example",
              "value": "abc/test.rs"
            },
            "2": {
              "summary": "Successful Example",
              "value": "bcd/test.rs"
            }
          },
          "schema": {
            "items": {
              "type": "string"
            },
            "type": "array"
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
    "Repositories"
  ]
}
```
