# Get Organization Project List
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-orgs-org-repos](https://docs.gitcode.com/en/docs/apis/get-api-v-5-orgs-org-repos)
Category: Organizations
- Method: `GET`
- Path: `/api/v5/orgs/{org}/repos`
- Operation ID: `get_api_v5_orgs_{org}_repos`
- Tags: `Organizations`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| org | path | true | string | Organization's path (path/login) |
| access_token | query | true | string | User authorization code |
| type | query | false | string | Filter the type of public/private repositories, which can be all, public, private. Default: all |
| page | query | false | integer | Current page number: defaults to 1 |
| per_page | query | false | integer | The number of items per page, with a maximum of 100. The default is 20. |
| repo_type | query | false | string | Filter repository type, which can be code: code repository, model: model repository, dataset: dataset repository, space: space, all: all repository types. Default: code |
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
      "created_at": {
        "type": "string"
      },
      "default_branch": {
        "type": "string"
      },
      "description": {
        "type": "string"
      },
      "fork": {
        "type": "integer"
      },
      "forks_count": {
        "type": "integer"
      },
      "full_name": {
        "type": "string"
      },
      "html_url": {
        "type": "string"
      },
      "id": {
        "type": "integer"
      },
      "internal": {
        "type": "integer"
      },
      "license": {
        "type": "null"
      },
      "name": {
        "type": "string"
      },
      "namespace": {
        "properties": {
          "html_url": {
            "type": "string"
          },
          "id": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          },
          "path": {
            "type": "string"
          },
          "type": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "open_issues_count": {
        "type": "integer"
      },
      "path": {
        "type": "string"
      },
      "private": {
        "type": "integer"
      },
      "project_creator": {
        "type": "string"
      },
      "public": {
        "type": "integer"
      },
      "pushed_at": {
        "type": "string"
      },
      "repo_type": {
        "type": "string"
      },
      "stargazers_count": {
        "type": "integer"
      },
      "status": {
        "type": "string"
      },
      "updated_at": {
        "type": "string"
      },
      "watchers_count": {
        "type": "integer"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```
Example:
```json
{
  "created_at": "2023-06-16T10:55:42+08:00",
  "default_branch": "master",
  "description": "",
  "fork": false,
  "forks_count": 4,
  "full_name": "openharmony/.gitee",
  "html_url": "https://gitcode.com/openharmony/.gitee.git",
  "id": 29724198,
  "internal": false,
  "license": null,
  "name": ".gitee",
  "namespace": {
    "html_url": "https://gitcode.com/openharmony",
    "id": 6486504,
    "name": "OpenHarmony",
    "path": "openharmony",
    "type": "group"
  },
  "open_issues_count": 0,
  "path": ".gitee",
  "private": false,
  "project_creator": "landwind",
  "public": true,
  "pushed_at": "2024-02-06T18:25:26+08:00",
  "repo_type": "code",
  "stargazers_count": 0,
  "status": "start",
  "updated_at": "2024-03-29T14:59:46+08:00",
  "watchers_count": 1
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
  "operationId": "get_api_v5_orgs_{org}_repos",
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
    },
    {
      "description": "Filter the type of public/private repositories, which can be all, public, private. Default: all",
      "in": "query",
      "name": "type",
      "required": false,
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
    },
    {
      "description": "Filter repository type, which can be code: code repository, model: model repository, dataset: dataset repository, space: space, all: all repository types. Default: code",
      "in": "query",
      "name": "repo_type",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/orgs/{org}/repos",
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
    "name": "Get Organization Project List",
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
        },
        {
          "description": {
            "content": "Filter the type of public/private repositories, which can be all, public, private. Default: all",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "type",
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
        },
        {
          "description": {
            "content": "Filter repository type, which can be code: code repository, model: model repository, dataset: dataset repository, space: space, all: all repository types. Default: code",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "repo_type",
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
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "example": {
            "created_at": "2023-06-16T10:55:42+08:00",
            "default_branch": "master",
            "description": "",
            "fork": false,
            "forks_count": 4,
            "full_name": "openharmony/.gitee",
            "html_url": "https://gitcode.com/openharmony/.gitee.git",
            "id": 29724198,
            "internal": false,
            "license": null,
            "name": ".gitee",
            "namespace": {
              "html_url": "https://gitcode.com/openharmony",
              "id": 6486504,
              "name": "OpenHarmony",
              "path": "openharmony",
              "type": "group"
            },
            "open_issues_count": 0,
            "path": ".gitee",
            "private": false,
            "project_creator": "landwind",
            "public": true,
            "pushed_at": "2024-02-06T18:25:26+08:00",
            "repo_type": "code",
            "stargazers_count": 0,
            "status": "start",
            "updated_at": "2024-03-29T14:59:46+08:00",
            "watchers_count": 1
          },
          "schema": {
            "items": {
              "properties": {
                "created_at": {
                  "type": "string"
                },
                "default_branch": {
                  "type": "string"
                },
                "description": {
                  "type": "string"
                },
                "fork": {
                  "type": "integer"
                },
                "forks_count": {
                  "type": "integer"
                },
                "full_name": {
                  "type": "string"
                },
                "html_url": {
                  "type": "string"
                },
                "id": {
                  "type": "integer"
                },
                "internal": {
                  "type": "integer"
                },
                "license": {
                  "type": "null"
                },
                "name": {
                  "type": "string"
                },
                "namespace": {
                  "properties": {
                    "html_url": {
                      "type": "string"
                    },
                    "id": {
                      "type": "integer"
                    },
                    "name": {
                      "type": "string"
                    },
                    "path": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "open_issues_count": {
                  "type": "integer"
                },
                "path": {
                  "type": "string"
                },
                "private": {
                  "type": "integer"
                },
                "project_creator": {
                  "type": "string"
                },
                "public": {
                  "type": "integer"
                },
                "pushed_at": {
                  "type": "string"
                },
                "repo_type": {
                  "type": "string"
                },
                "stargazers_count": {
                  "type": "integer"
                },
                "status": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                },
                "watchers_count": {
                  "type": "integer"
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
    "Organizations"
  ]
}
```
