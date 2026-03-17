# Update a Task Label in a Repository
Source: [https://docs.gitcode.com/en/docs/apis/patch-api-v-5-repos-owner-repo-labels-original-name](https://docs.gitcode.com/en/docs/apis/patch-api-v-5-repos-owner-repo-labels-original-name)
Category: Labels
- Method: `PATCH`
- Path: `/api/v5/repos/{owner}/{repo}/labels/{original_name}`
- Operation ID: `patch_api_v5_repos_{owner}_{repo}_labels_{original_name}`
- Tags: `Labels`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| original_name | path | true | string | Original label name |
| access_token | query | true | string | User authorization code |
| name | query | false | string | Label New Name |
| color | query | false | string | Label New Color |
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
  "properties": {
    "color": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    }
  },
  "type": "object"
}
```
Example:
```json
{
  "color": "#ED4014",
  "id": 12738100,
  "name": "list"
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
  "method": "patch",
  "operationId": "patch_api_v5_repos_{owner}_{repo}_labels_{original_name}",
  "parameters": [
    {
      "description": "Repository space address (address path of the enterprise, organization, or individual)",
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
      "description": "Original label name",
      "example": "",
      "in": "path",
      "name": "original_name",
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
      "description": "Label New Name",
      "in": "query",
      "name": "name",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Label New Color",
      "in": "query",
      "name": "color",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/labels/{original_name}",
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
    "method": "PATCH",
    "name": "Update a Task Label in a Repository",
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
        "labels",
        ":original_name"
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
            "content": "Label New Name",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "name",
          "value": ""
        },
        {
          "description": {
            "content": "Label New Color",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "color",
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
            "content": "(Required) Original label name",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "original_name",
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
          "example": {
            "color": "#ED4014",
            "id": 12738100,
            "name": "list"
          },
          "schema": {
            "properties": {
              "color": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "name": {
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
    "Labels"
  ]
}
```
