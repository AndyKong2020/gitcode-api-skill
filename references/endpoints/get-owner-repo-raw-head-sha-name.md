# Get File Content
Source: [https://docs.gitcode.com/en/docs/apis/get-owner-repo-raw-head-sha-name](https://docs.gitcode.com/en/docs/apis/get-owner-repo-raw-head-sha-name)
Category: Pull Requests
- Method: `GET`
- Path: `/{owner}/{repo}/raw/{head_sha}/{name}`
- Operation ID: `get_{owner}_{repo}_raw_{head_sha}_{name}`
- Tags: `Pull Requests`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string |  |
| repo | path | true | string |  |
| head_sha | path | true | string |  |
| name | path | true | string |  |
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
  "properties": {},
  "type": "object"
}
```
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": {}
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
  "operationId": "get_{owner}_{repo}_raw_{head_sha}_{name}",
  "parameters": [
    {
      "description": "",
      "example": "",
      "in": "path",
      "name": "owner",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "",
      "example": "",
      "in": "path",
      "name": "repo",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "",
      "example": "",
      "in": "path",
      "name": "head_sha",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "",
      "example": "",
      "in": "path",
      "name": "name",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/{owner}/{repo}/raw/{head_sha}/{name}",
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
    "name": "Get File Content",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        ":owner",
        ":repo",
        "raw",
        ":head_sha",
        ":name"
      ],
      "query": [],
      "variable": [
        {
          "description": {
            "content": "(Required) ",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "owner",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) ",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "repo",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) ",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "head_sha",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) ",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "name",
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
              "value": {}
            }
          },
          "schema": {
            "properties": {},
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
      "url": "https://raw.gitcode.com"
    }
  ],
  "tags": [
    "Pull Requests"
  ]
}
```
