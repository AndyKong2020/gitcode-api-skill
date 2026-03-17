# Update Warehouse Settings
Source: [https://docs.gitcode.com/en/docs/apis/patch-api-v-5-repos-owner-repo](https://docs.gitcode.com/en/docs/apis/patch-api-v-5-repos-owner-repo)
Category: Repositories
- Method: `PATCH`
- Path: `/api/v5/repos/{owner}/{repo}`
- Operation ID: `patch_api_v5_repos_{owner}_{repo}`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "default_branch": {
      "description": "Default branch",
      "type": "string"
    },
    "description": {
      "description": "Repository description",
      "type": "string"
    },
    "homepage": {
      "description": "Project Address (e.g. https://gitcode.com)",
      "type": "string"
    },
    "lfs_enabled": {
      "description": "Whether to enable LFS",
      "type": "boolean"
    },
    "name": {
      "description": "Repository name",
      "type": "string"
    },
    "path": {
      "description": "Update repository path",
      "type": "string"
    },
    "private": {
      "description": "Repository is public or private. (true/false)",
      "type": "boolean"
    },
    "tags": {
      "description": "Project Tags",
      "items": {
        "type": "string"
      },
      "type": "array"
    }
  },
  "required": [
    "name"
  ],
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
    "creator": {
      "type": "null"
    },
    "description": {
      "type": "string"
    },
    "empty_repo": {
      "type": "null"
    },
    "forked_from_project": {
      "type": "null"
    },
    "full_name": {
      "type": "string"
    },
    "homepage": {
      "type": "string"
    },
    "human_name": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    },
    "item_type": {
      "type": "null"
    },
    "main_repository_language": {
      "type": "null"
    },
    "name": {
      "type": "string"
    },
    "namespace": {
      "properties": {
        "cell": {
          "type": "string"
        },
        "develop_mode": {
          "type": "string"
        },
        "enable_file_control": {
          "type": "integer"
        },
        "full_name": {
          "type": "string"
        },
        "full_path": {
          "type": "string"
        },
        "id": {
          "type": "integer"
        },
        "kind": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "owner_id": {
          "type": "null"
        },
        "parent_id": {
          "type": "null"
        },
        "path": {
          "type": "string"
        },
        "region": {
          "type": "null"
        },
        "visibility_level": {
          "type": "integer"
        }
      },
      "type": "object"
    },
    "owner": {
      "type": "null"
    },
    "path": {
      "type": "string"
    },
    "private": {
      "type": "integer"
    },
    "public": {
      "type": "integer"
    },
    "starred": {
      "type": "null"
    },
    "url": {
      "type": "string"
    },
    "visibility": {
      "type": "string"
    }
  },
  "type": "object"
}
```
Example:
```json
{
  "creator": null,
  "description": "description",
  "empty_repo": null,
  "forked_from_project": null,
  "full_name": "daming_1/test_create_project_2",
  "homepage": "http://www.baidi.com",
  "human_name": "daming/test_create_project_2",
  "id": 34171993,
  "item_type": null,
  "main_repository_language": null,
  "name": "test_create_project_2",
  "namespace": {
    "cell": "default",
    "develop_mode": "normal",
    "enable_file_control": false,
    "full_name": "group1111",
    "full_path": "group11111",
    "id": 74962,
    "kind": "group",
    "name": "group1111",
    "owner_id": null,
    "parent_id": null,
    "path": "group11111",
    "region": null,
    "visibility_level": 20
  },
  "owner": null,
  "path": "test_create_project_2",
  "private": false,
  "public": true,
  "starred": null,
  "url": "https://gitcode.com/api/v5/repos/daming_1/test_create_project_2",
  "visibility": "public"
}
```
## JSON Request Example
```json
{
  "default_branch": "string",
  "description": "string",
  "homepage": "string",
  "lfs_enabled": true,
  "name": "string",
  "path": "string",
  "private": true,
  "tags": [
    "string"
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
  "jsonRequestBodyExample": {
    "default_branch": "string",
    "description": "string",
    "homepage": "string",
    "lfs_enabled": true,
    "name": "string",
    "path": "string",
    "private": true,
    "tags": [
      "string"
    ]
  },
  "method": "patch",
  "operationId": "patch_api_v5_repos_{owner}_{repo}",
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
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}",
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
    "name": "Update Warehouse Settings",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "repos",
        ":owner",
        ":repo"
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
            "default_branch": {
              "description": "Default branch",
              "type": "string"
            },
            "description": {
              "description": "Repository description",
              "type": "string"
            },
            "homepage": {
              "description": "Project Address (e.g. https://gitcode.com)",
              "type": "string"
            },
            "lfs_enabled": {
              "description": "Whether to enable LFS",
              "type": "boolean"
            },
            "name": {
              "description": "Repository name",
              "type": "string"
            },
            "path": {
              "description": "Update repository path",
              "type": "string"
            },
            "private": {
              "description": "Repository is public or private. (true/false)",
              "type": "boolean"
            },
            "tags": {
              "description": "Project Tags",
              "items": {
                "type": "string"
              },
              "type": "array"
            }
          },
          "required": [
            "name"
          ],
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
            "creator": null,
            "description": "description",
            "empty_repo": null,
            "forked_from_project": null,
            "full_name": "daming_1/test_create_project_2",
            "homepage": "http://www.baidi.com",
            "human_name": "daming/test_create_project_2",
            "id": 34171993,
            "item_type": null,
            "main_repository_language": null,
            "name": "test_create_project_2",
            "namespace": {
              "cell": "default",
              "develop_mode": "normal",
              "enable_file_control": false,
              "full_name": "group1111",
              "full_path": "group11111",
              "id": 74962,
              "kind": "group",
              "name": "group1111",
              "owner_id": null,
              "parent_id": null,
              "path": "group11111",
              "region": null,
              "visibility_level": 20
            },
            "owner": null,
            "path": "test_create_project_2",
            "private": false,
            "public": true,
            "starred": null,
            "url": "https://gitcode.com/api/v5/repos/daming_1/test_create_project_2",
            "visibility": "public"
          },
          "schema": {
            "properties": {
              "creator": {
                "type": "null"
              },
              "description": {
                "type": "string"
              },
              "empty_repo": {
                "type": "null"
              },
              "forked_from_project": {
                "type": "null"
              },
              "full_name": {
                "type": "string"
              },
              "homepage": {
                "type": "string"
              },
              "human_name": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "item_type": {
                "type": "null"
              },
              "main_repository_language": {
                "type": "null"
              },
              "name": {
                "type": "string"
              },
              "namespace": {
                "properties": {
                  "cell": {
                    "type": "string"
                  },
                  "develop_mode": {
                    "type": "string"
                  },
                  "enable_file_control": {
                    "type": "integer"
                  },
                  "full_name": {
                    "type": "string"
                  },
                  "full_path": {
                    "type": "string"
                  },
                  "id": {
                    "type": "integer"
                  },
                  "kind": {
                    "type": "string"
                  },
                  "name": {
                    "type": "string"
                  },
                  "owner_id": {
                    "type": "null"
                  },
                  "parent_id": {
                    "type": "null"
                  },
                  "path": {
                    "type": "string"
                  },
                  "region": {
                    "type": "null"
                  },
                  "visibility_level": {
                    "type": "integer"
                  }
                },
                "type": "object"
              },
              "owner": {
                "type": "null"
              },
              "path": {
                "type": "string"
              },
              "private": {
                "type": "integer"
              },
              "public": {
                "type": "integer"
              },
              "starred": {
                "type": "null"
              },
              "url": {
                "type": "string"
              },
              "visibility": {
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
    "Repositories"
  ]
}
```
