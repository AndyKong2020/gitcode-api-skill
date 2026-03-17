# Create Personal Project Repository
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-user-repos](https://docs.gitcode.com/en/docs/apis/post-api-v-5-user-repos)
Category: Users
- Method: `POST`
- Path: `/api/v5/user/repos`
- Operation ID: `post_api_v5_user_repos`
- Tags: `Users`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "auto_init": {
      "description": "When the value is true, the repository will be initialized with a README. Default: not initialized (false).",
      "type": "boolean"
    },
    "can_comment": {
      "description": "Allows users to comment on the repository. Default: Allowed (true)",
      "type": "boolean"
    },
    "default_branch": {
      "description": "Default branch name when initializing the project. Default: main",
      "type": "string"
    },
    "description": {
      "description": "Repository description",
      "type": "string"
    },
    "gitignore_template": {
      "description": "Git Ignore Template",
      "type": "string"
    },
    "has_issues": {
      "description": "Allow issues to be raised. Default: Allowed (true)",
      "type": "boolean"
    },
    "has_wiki": {
      "description": "Provide Wiki or not. Default: Provide (true)",
      "type": "boolean"
    },
    "import_url": {
      "description": "The git address of the imported project, import_url and project_template parameters can only be passed one.",
      "type": "string"
    },
    "license_template": {
      "description": "License template",
      "type": "string"
    },
    "name": {
      "description": "Repository name",
      "type": "string"
    },
    "path": {
      "description": "Repository path",
      "type": "string"
    },
    "private": {
      "description": "IsPrivate",
      "type": "boolean"
    },
    "project_template": {
      "description": "The path, import_url, and project_template parameters of the template project can only accept one value.",
      "type": "string"
    },
    "repository_type": {
      "description": "Repository type. code: code repository, model: model repository, dataset: dataset repository, space: space, default: code",
      "type": "string"
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
    "description": {
      "type": "string"
    },
    "full_name": {
      "type": "string"
    },
    "human_name": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    },
    "namespace": {
      "properties": {
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
          "type": "integer"
        },
        "path": {
          "type": "string"
        },
        "visibility_level": {
          "type": "integer"
        }
      },
      "type": "object"
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
  "description": "wunian-prj",
  "full_name": "dengmengmian/wunian-prj",
  "human_name": "dengmengmian / wunian-prj",
  "id": 4106383,
  "name": "wunian-prj",
  "namespace": {
    "develop_mode": "normal",
    "enable_file_control": false,
    "full_name": "dengmengmian",
    "full_path": "dengmengmian",
    "id": 199940,
    "kind": "user",
    "name": "dengmengmian",
    "owner_id": 268,
    "path": "dengmengmian",
    "visibility_level": 20
  },
  "path": "wunian-prj",
  "private": true,
  "public": false,
  "url": "https://api.gitcode.com/api/v5/user/repos",
  "visibility": "private"
}
```
## JSON Request Example
```json
{
  "auto_init": true,
  "can_comment": true,
  "default_branch": "string",
  "description": "string",
  "gitignore_template": "string",
  "has_issues": true,
  "has_wiki": true,
  "import_url": "string",
  "license_template": "string",
  "name": "string",
  "path": "string",
  "private": true,
  "project_template": "string",
  "repository_type": "string"
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
    "auto_init": true,
    "can_comment": true,
    "default_branch": "string",
    "description": "string",
    "gitignore_template": "string",
    "has_issues": true,
    "has_wiki": true,
    "import_url": "string",
    "license_template": "string",
    "name": "string",
    "path": "string",
    "private": true,
    "project_template": "string",
    "repository_type": "string"
  },
  "method": "post",
  "operationId": "post_api_v5_user_repos",
  "parameters": [
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
  "path": "/api/v5/user/repos",
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
    "method": "POST",
    "name": "Create Personal Project Repository",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "user",
        "repos"
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
      "variable": []
    }
  },
  "requestBody": {
    "content": {
      "application/json": {
        "example": "",
        "schema": {
          "properties": {
            "auto_init": {
              "description": "When the value is true, the repository will be initialized with a README. Default: not initialized (false).",
              "type": "boolean"
            },
            "can_comment": {
              "description": "Allows users to comment on the repository. Default: Allowed (true)",
              "type": "boolean"
            },
            "default_branch": {
              "description": "Default branch name when initializing the project. Default: main",
              "type": "string"
            },
            "description": {
              "description": "Repository description",
              "type": "string"
            },
            "gitignore_template": {
              "description": "Git Ignore Template",
              "type": "string"
            },
            "has_issues": {
              "description": "Allow issues to be raised. Default: Allowed (true)",
              "type": "boolean"
            },
            "has_wiki": {
              "description": "Provide Wiki or not. Default: Provide (true)",
              "type": "boolean"
            },
            "import_url": {
              "description": "The git address of the imported project, import_url and project_template parameters can only be passed one.",
              "type": "string"
            },
            "license_template": {
              "description": "License template",
              "type": "string"
            },
            "name": {
              "description": "Repository name",
              "type": "string"
            },
            "path": {
              "description": "Repository path",
              "type": "string"
            },
            "private": {
              "description": "IsPrivate",
              "type": "boolean"
            },
            "project_template": {
              "description": "The path, import_url, and project_template parameters of the template project can only accept one value.",
              "type": "string"
            },
            "repository_type": {
              "description": "Repository type. code: code repository, model: model repository, dataset: dataset repository, space: space, default: code",
              "type": "string"
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
            "description": "wunian-prj",
            "full_name": "dengmengmian/wunian-prj",
            "human_name": "dengmengmian / wunian-prj",
            "id": 4106383,
            "name": "wunian-prj",
            "namespace": {
              "develop_mode": "normal",
              "enable_file_control": false,
              "full_name": "dengmengmian",
              "full_path": "dengmengmian",
              "id": 199940,
              "kind": "user",
              "name": "dengmengmian",
              "owner_id": 268,
              "path": "dengmengmian",
              "visibility_level": 20
            },
            "path": "wunian-prj",
            "private": true,
            "public": false,
            "url": "https://api.gitcode.com/api/v5/user/repos",
            "visibility": "private"
          },
          "schema": {
            "properties": {
              "description": {
                "type": "string"
              },
              "full_name": {
                "type": "string"
              },
              "human_name": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "name": {
                "type": "string"
              },
              "namespace": {
                "properties": {
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
                    "type": "integer"
                  },
                  "path": {
                    "type": "string"
                  },
                  "visibility_level": {
                    "type": "integer"
                  }
                },
                "type": "object"
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
    "Users"
  ]
}
```
