# Get Repository Directory Tree
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-git-trees-sha](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-git-trees-sha)
Category: Repositories
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/git/trees/{sha}`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_git_trees_{sha}`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| sha | path | true | string | It can be a branch name (e.g., master), a Commit, or a directory Tree SHA. |
| access_token | query | true | string | User authorization code |
| page | query | false | integer | The current page number |
| per_page | query | false | integer | The number of items per page, with a maximum of 100. The default is 20. |
| recursive | query | false | integer | Assign 1 to recursively retrieve the directory |
| file_path | query | false | string | File tree path |
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
    "tree": {
      "items": {
        "properties": {
          "md5": {
            "type": "string"
          },
          "mode": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "path": {
            "type": "string"
          },
          "sha": {
            "type": "string"
          },
          "type": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    }
  },
  "type": "object"
}
```
Example:
```json
{
  "tree": [
    {
      "md5": "a7e86136543b019d72468ceebf71fb8e",
      "mode": "040000",
      "name": "b",
      "path": "a/b",
      "sha": "5259c4b24f015ffdc3663e81837a730c2a108e1f",
      "type": "tree"
    }
  ]
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_git_trees_{sha}",
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
      "description": "It can be a branch name (e.g., master), a Commit, or a directory Tree SHA.",
      "example": "",
      "in": "path",
      "name": "sha",
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
      "description": "The current page number",
      "in": "query",
      "name": "page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "The number of items per page, with a maximum of 100. The default is 20.",
      "in": "query",
      "name": "per_page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "Assign 1 to recursively retrieve the directory",
      "in": "query",
      "name": "recursive",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "File tree path",
      "in": "query",
      "name": "file_path",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/git/trees/{sha}",
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
    "name": "Get Repository Directory Tree",
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
        "git",
        "trees",
        ":sha"
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
            "content": "The current page number",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "page",
          "value": ""
        },
        {
          "description": {
            "content": "The number of items per page, with a maximum of 100. The default is 20.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "per_page",
          "value": ""
        },
        {
          "description": {
            "content": "Assign 1 to recursively retrieve the directory",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "recursive",
          "value": ""
        },
        {
          "description": {
            "content": "File tree path",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "file_path",
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
            "content": "(Required) It can be a branch name (e.g., master), a Commit, or a directory Tree SHA.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sha",
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
            "tree": [
              {
                "md5": "a7e86136543b019d72468ceebf71fb8e",
                "mode": "040000",
                "name": "b",
                "path": "a/b",
                "sha": "5259c4b24f015ffdc3663e81837a730c2a108e1f",
                "type": "tree"
              }
            ]
          },
          "schema": {
            "properties": {
              "tree": {
                "items": {
                  "properties": {
                    "md5": {
                      "type": "string"
                    },
                    "mode": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "path": {
                      "type": "string"
                    },
                    "sha": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
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
    "Repositories"
  ]
}
```
