# Get All Members of the Repository
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-collaborators](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-collaborators)
Category: Member
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/collaborators`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_collaborators`
- Tags: `Member`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
| page | query | false | integer | Current page number: defaults to 1 |
| per_page | query | false | integer | The number of items per page, with a maximum of 100. The default is 20. |
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
    "properties": {
      "access_level": {
        "type": "null"
      },
      "avatar": {
        "type": "null"
      },
      "avatar_url": {
        "type": "null"
      },
      "committer_system_from": {
        "type": "null"
      },
      "email": {
        "type": "null"
      },
      "expires_at": {
        "type": "null"
      },
      "iam_id": {
        "type": "null"
      },
      "id": {
        "type": "string"
      },
      "is_current_source_member": {
        "type": "null"
      },
      "join_way": {
        "type": "null"
      },
      "last_owner": {
        "type": "null"
      },
      "last_source_owner": {
        "type": "null"
      },
      "limited": {
        "type": "null"
      },
      "member_roles": {
        "type": "null"
      },
      "name": {
        "type": "string"
      },
      "name_cn": {
        "type": "null"
      },
      "nick_name": {
        "type": "null"
      },
      "permissions": {
        "properties": {
          "admin": {
            "type": "integer"
          },
          "pull": {
            "type": "null"
          },
          "push": {
            "type": "null"
          }
        },
        "type": "object"
      },
      "source_name": {
        "type": "null"
      },
      "state": {
        "type": "null"
      },
      "type": {
        "type": "string"
      },
      "username": {
        "type": "string"
      },
      "web_url": {
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": {
      "access_level": null,
      "avatar": null,
      "avatar_url": null,
      "committer_system_from": null,
      "email": null,
      "expires_at": null,
      "iam_id": null,
      "id": "708",
      "is_current_source_member": null,
      "join_way": null,
      "last_owner": null,
      "last_source_owner": null,
      "limited": null,
      "member_roles": null,
      "name": "Lzm_0916",
      "name_cn": null,
      "nick_name": null,
      "permissions": {
        "admin": true,
        "pull": null,
        "push": null
      },
      "source_name": null,
      "state": null,
      "type": "ProjectMember",
      "username": "Lzm_0916",
      "web_url": "https://test.gitcode.net/Lzm_0916"
    }
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_collaborators",
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
      "description": "Current page number: defaults to 1",
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
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/collaborators",
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
    "name": "Get All Members of the Repository",
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
        "collaborators"
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
            "content": "Current page number: defaults to 1",
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
              "value": {
                "access_level": null,
                "avatar": null,
                "avatar_url": null,
                "committer_system_from": null,
                "email": null,
                "expires_at": null,
                "iam_id": null,
                "id": "708",
                "is_current_source_member": null,
                "join_way": null,
                "last_owner": null,
                "last_source_owner": null,
                "limited": null,
                "member_roles": null,
                "name": "Lzm_0916",
                "name_cn": null,
                "nick_name": null,
                "permissions": {
                  "admin": true,
                  "pull": null,
                  "push": null
                },
                "source_name": null,
                "state": null,
                "type": "ProjectMember",
                "username": "Lzm_0916",
                "web_url": "https://test.gitcode.net/Lzm_0916"
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "access_level": {
                  "type": "null"
                },
                "avatar": {
                  "type": "null"
                },
                "avatar_url": {
                  "type": "null"
                },
                "committer_system_from": {
                  "type": "null"
                },
                "email": {
                  "type": "null"
                },
                "expires_at": {
                  "type": "null"
                },
                "iam_id": {
                  "type": "null"
                },
                "id": {
                  "type": "string"
                },
                "is_current_source_member": {
                  "type": "null"
                },
                "join_way": {
                  "type": "null"
                },
                "last_owner": {
                  "type": "null"
                },
                "last_source_owner": {
                  "type": "null"
                },
                "limited": {
                  "type": "null"
                },
                "member_roles": {
                  "type": "null"
                },
                "name": {
                  "type": "string"
                },
                "name_cn": {
                  "type": "null"
                },
                "nick_name": {
                  "type": "null"
                },
                "permissions": {
                  "properties": {
                    "admin": {
                      "type": "integer"
                    },
                    "pull": {
                      "type": "null"
                    },
                    "push": {
                      "type": "null"
                    }
                  },
                  "type": "object"
                },
                "source_name": {
                  "type": "null"
                },
                "state": {
                  "type": "null"
                },
                "type": {
                  "type": "string"
                },
                "username": {
                  "type": "string"
                },
                "web_url": {
                  "type": "string"
                }
              },
              "type": "object"
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
    "Member"
  ]
}
```
