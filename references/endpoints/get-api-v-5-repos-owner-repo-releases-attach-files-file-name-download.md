# Download the release attachment from the repository.
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-releases-attach-files-file-name-download](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-releases-attach-files-file-name-download)
Category: Release
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/releases/{tag}/attach_files/{file_name}/download`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_releases_attach_files_{file_name}_download`
- Tags: `Release`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| tag | path | true | string | Label name |
| file_name | path | true | string | Attachment Name |
| access_token | query | true | string | User authorization code |
## Request Body
No request body.
## Responses
### `200`
Headers:
```json
{}
```
#### `*/*`
Schema:
```json
{
  "properties": {},
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_releases_attach_files_{file_name}_download",
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
      "description": "Label name",
      "example": "",
      "in": "path",
      "name": "tag",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Attachment Name",
      "example": "",
      "in": "path",
      "name": "file_name",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "User authorization code",
      "example": "",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/releases/{tag}/attach_files/{file_name}/download",
  "postman": {
    "description": {
      "content": "",
      "type": "text/plain"
    },
    "header": [
      {
        "key": "Accept",
        "value": "*/*"
      }
    ],
    "method": "GET",
    "name": "Download the release attachment from the repository.",
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
        "attach_files",
        ":file_name",
        "download"
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
            "content": "(Required) Label name",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "tag",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) Attachment Name",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "file_name",
          "type": "any",
          "value": ""
        }
      ]
    }
  },
  "responses": {
    "200": {
      "content": {
        "*/*": {
          "schema": {
            "properties": {},
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
  "tags": [
    "Release"
  ]
}
```
