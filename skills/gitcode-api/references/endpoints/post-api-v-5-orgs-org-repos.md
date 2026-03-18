# Create Organization Repository
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-orgs-org-repos](https://docs.gitcode.com/en/docs/apis/post-api-v-5-orgs-org-repos)
Category: Organizations
- Method: `POST`
- Path: `/api/v5/orgs/{org}/repos`
- Operation ID: `post_api_v5_orgs_{org}_repos`
- Tags: `Organizations`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| org | path | true | string | Organization's path (path/login) |
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
    "homepage": {
      "description": "home page",
      "type": "string"
    },
    "import_url": {
      "description": "The git address of the imported project, import_url and project_template parameters can only be passed in one.",
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
      "description": "Repository is public or private. Default: Public (false), Note: Mutually exclusive with public, with public taking precedence.",
      "type": "boolean"
    },
    "project_template": {
      "description": "The path, import_url, and project_template parameters for the template project can only be passed in one at a time.",
      "type": "string"
    },
    "public": {
      "description": "Repository open-source type. 0 (private), 1 (external open source), 2 (internal open source). Note: Mutually exclusive with private, takes public as the priority.",
      "type": "integer"
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
  "auto_init": true,
  "can_comment": true,
  "default_branch": "string",
  "description": "string",
  "gitignore_template": "string",
  "has_issues": true,
  "has_wiki": true,
  "homepage": "string",
  "import_url": "string",
  "license_template": "string",
  "name": "string",
  "path": "string",
  "private": true,
  "project_template": "string",
  "public": 0,
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
    "homepage": "string",
    "import_url": "string",
    "license_template": "string",
    "name": "string",
    "path": "string",
    "private": true,
    "project_template": "string",
    "public": 0,
    "repository_type": "string"
  },
  "method": "post",
  "operationId": "post_api_v5_orgs_{org}_repos",
  "parameters": [
    {
      "description": "Organization's path (path/login)",
      "example": "",
      "in": "path",
      "name": "org",
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
  "path": "/api/v5/orgs/{org}/repos",
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
    "name": "Create Organization Repository",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "orgs",
        ":org",
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
      "variable": [
        {
          "description": {
            "content": "(Required) Organization's path (path/login)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "org",
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
            "homepage": {
              "description": "home page",
              "type": "string"
            },
            "import_url": {
              "description": "The git address of the imported project, import_url and project_template parameters can only be passed in one.",
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
              "description": "Repository is public or private. Default: Public (false), Note: Mutually exclusive with public, with public taking precedence.",
              "type": "boolean"
            },
            "project_template": {
              "description": "The path, import_url, and project_template parameters for the template project can only be passed in one at a time.",
              "type": "string"
            },
            "public": {
              "description": "Repository open-source type. 0 (private), 1 (external open source), 2 (internal open source). Note: Mutually exclusive with private, takes public as the priority.",
              "type": "integer"
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
    "Organizations"
  ]
}
```
