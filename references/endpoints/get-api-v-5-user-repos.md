# List All Repositories For Authorized Users
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-user-repos](https://docs.gitcode.com/en/docs/apis/get-api-v-5-user-repos)
Category: Users
- Method: `GET`
- Path: `/api/v5/user/repos`
- Operation ID: `get_api_v5_user_repos`
- Tags: `Users`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| access_token | query | true | string | User authorization code |
| visibility | query | false | string | public, private, or all; default: all |
| affiliation | query | false | string | owner (repository owner), collaborator (authorized user as a member of the repository), organization_member (authorized user as a member of the organization that owns the repository and has access to the repository), enterprise_member (authorized user as a member of the enterprise that owns the repository and has access to the repository), admin (all authorized users including all repositories in managed organizations and all repositories in managed enterprises). These can be combined with commas. For example: owner, organization_member or owner, collaborator, organization_member. |
| type | query | false | string | Filter user repositories: created(owner), personal, member, public, private. Cannot be used with the affiliation parameter, otherwise a 422 error will occur. Should be used with the visibility parameter, which has higher priority. |
| sort | query | false | string | Sort by: created, updated, pushed, full_name. Default: full_name |
| direction | query | false | string | If the sort parameter is full_name, use ascending (asc). Otherwise, use descending (desc). |
| q | query | false | string | Search keyword |
| page | query | false | integer | The current page number |
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
      "assignee": {
        "items": {
          "properties": {
            "avatar_url": {
              "type": "string"
            },
            "html_url": {
              "type": "string"
            },
            "id": {
              "type": "string"
            },
            "login": {
              "type": "string"
            },
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            }
          },
          "type": "object"
        },
        "type": "array"
      },
      "assignees_number": {
        "type": "integer"
      },
      "assigner": {
        "properties": {
          "id": {
            "type": "string"
          },
          "login": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "type": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "default_branch": {
        "type": "string"
      },
      "description": {
        "type": "string"
      },
      "enterprise": {
        "properties": {
          "html_url": {
            "type": "string"
          },
          "id": {
            "type": "integer"
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
      "fork": {
        "type": "integer"
      },
      "forks_count": {
        "type": "integer"
      },
      "full_name": {
        "type": "string"
      },
      "has_issue": {
        "type": "integer"
      },
      "homepage": {
        "type": "string"
      },
      "http_url_to_repo": {
        "type": "string"
      },
      "human_name": {
        "type": "string"
      },
      "id": {
        "type": "integer"
      },
      "internal": {
        "type": "integer"
      },
      "members": {
        "items": {
          "type": "string"
        },
        "type": "array"
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
      "owner": {
        "properties": {
          "id": {
            "type": "string"
          },
          "login": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "type": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "path": {
        "type": "string"
      },
      "permission": {
        "properties": {
          "admin": {
            "type": "integer"
          },
          "pull": {
            "type": "integer"
          },
          "push": {
            "type": "integer"
          }
        },
        "type": "object"
      },
      "private": {
        "type": "integer"
      },
      "project_labels": {
        "items": {
          "properties": {},
          "type": "object"
        },
        "type": "array"
      },
      "public": {
        "type": "integer"
      },
      "relation": {
        "type": "string"
      },
      "repo_type": {
        "type": "string"
      },
      "ssh_url_to_repo": {
        "type": "string"
      },
      "stargazers_count": {
        "type": "integer"
      },
      "status": {
        "type": "string"
      },
      "url": {
        "type": "string"
      },
      "watched": {
        "type": "integer"
      },
      "watchers_count": {
        "type": "integer"
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
Example:
```json
{
  "assignee": [
    {
      "avatar_url": "https://cdn-img.gitcode.com/bd/ca/0115343247b338d0c53589a145501e84a58464272f2fb09b372cc3d2311b2b39.png?time=1722525295285",
      "html_url": "https://gitcode.com/aron1",
      "id": "332008",
      "login": "aron1",
      "name": "yanfan",
      "type": "User"
    }
  ],
  "assignees_number": 1,
  "assigner": {
    "id": "444601",
    "login": "yanfan",
    "name": "abcabcabc",
    "type": "User"
  },
  "default_branch": "main",
  "description": "",
  "enterprise": {
    "html_url": "https://gitcode.com/tiandi",
    "id": 1420034,
    "path": "tiandi",
    "type": "enterprise"
  },
  "fork": false,
  "forks_count": 0,
  "full_name": "tiandi/test_yf_repo",
  "has_issue": false,
  "homepage": "https://gitcode.com/tiandi/test_yf_repo",
  "http_url_to_repo": "https://gitcode.com/tiandi/test_yf_repo.git",
  "human_name": "Hongmen / test_yf_repo",
  "id": 4028329,
  "internal": false,
  "members": [
    "aron1"
  ],
  "name": "test_yf_repo",
  "namespace": {
    "html_url": "https://gitcode.com/tiandi",
    "id": 1420034,
    "name": "Red Gang",
    "path": "tiandi",
    "type": "enterprise"
  },
  "open_issues_count": 0,
  "owner": {
    "id": "444601",
    "login": "yanfan",
    "name": "abcabcabc",
    "type": "User"
  },
  "path": "test_yf_repo",
  "permission": {
    "admin": true,
    "pull": true,
    "push": true
  },
  "private": true,
  "project_labels": [],
  "public": false,
  "relation": "master",
  "ssh_url_to_repo": "git@gitcode.com:tiandi/test_yf_repo.git",
  "stargazers_count": 0,
  "status": "start",
  "url": "https://api.gitcode.com/api/v5/repos/tiandi/test_yf_repo",
  "watched": false,
  "watchers_count": 0,
  "web_url": "https://gitcode.com/tiandi/test_yf_repo"
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
  "operationId": "get_api_v5_user_repos",
  "parameters": [
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
      "description": "public, private, or all; default: all",
      "in": "query",
      "name": "visibility",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "owner (repository owner), collaborator (authorized user as a member of the repository), organization_member (authorized user as a member of the organization that owns the repository and has access to the repository), enterprise_member (authorized user as a member of the enterprise that owns the repository and has access to the repository), admin (all authorized users including all repositories in managed organizations and all repositories in managed enterprises). These can be combined with commas. For example: owner, organization_member or owner, collaborator, organization_member.",
      "in": "query",
      "name": "affiliation",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Filter user repositories: created(owner), personal, member, public, private. Cannot be used with the affiliation parameter, otherwise a 422 error will occur. Should be used with the visibility parameter, which has higher priority.",
      "in": "query",
      "name": "type",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Sort by: created, updated, pushed, full_name. Default: full_name",
      "in": "query",
      "name": "sort",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "If the sort parameter is full_name, use ascending (asc). Otherwise, use descending (desc).",
      "in": "query",
      "name": "direction",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Search keyword",
      "in": "query",
      "name": "q",
      "required": false,
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
      "description": "Filter repository type, which can be code: code repository, model: model repository, dataset: dataset repository, space: space, all: all repository types. Default: code",
      "in": "query",
      "name": "repo_type",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/user/repos",
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
    "name": "List All Repositories For Authorized Users",
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
        },
        {
          "description": {
            "content": "public, private, or all; default: all",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "visibility",
          "value": ""
        },
        {
          "description": {
            "content": "owner (repository owner), collaborator (authorized user as a member of the repository), organization_member (authorized user as a member of the organization that owns the repository and has access to the repository), enterprise_member (authorized user as a member of the enterprise that owns the repository and has access to the repository), admin (all authorized users including all repositories in managed organizations and all repositories in managed enterprises). These can be combined with commas. For example: owner, organization_member or owner, collaborator, organization_member.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "affiliation",
          "value": ""
        },
        {
          "description": {
            "content": "Filter user repositories: created(owner), personal, member, public, private. Cannot be used with the affiliation parameter, otherwise a 422 error will occur. Should be used with the visibility parameter, which has higher priority.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "type",
          "value": ""
        },
        {
          "description": {
            "content": "Sort by: created, updated, pushed, full_name. Default: full_name",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sort",
          "value": ""
        },
        {
          "description": {
            "content": "If the sort parameter is full_name, use ascending (asc). Otherwise, use descending (desc).",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "direction",
          "value": ""
        },
        {
          "description": {
            "content": "Search keyword",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "q",
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
            "content": "Filter repository type, which can be code: code repository, model: model repository, dataset: dataset repository, space: space, all: all repository types. Default: code",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "repo_type",
          "value": ""
        }
      ],
      "variable": []
    }
  },
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "example": {
            "assignee": [
              {
                "avatar_url": "https://cdn-img.gitcode.com/bd/ca/0115343247b338d0c53589a145501e84a58464272f2fb09b372cc3d2311b2b39.png?time=1722525295285",
                "html_url": "https://gitcode.com/aron1",
                "id": "332008",
                "login": "aron1",
                "name": "yanfan",
                "type": "User"
              }
            ],
            "assignees_number": 1,
            "assigner": {
              "id": "444601",
              "login": "yanfan",
              "name": "abcabcabc",
              "type": "User"
            },
            "default_branch": "main",
            "description": "",
            "enterprise": {
              "html_url": "https://gitcode.com/tiandi",
              "id": 1420034,
              "path": "tiandi",
              "type": "enterprise"
            },
            "fork": false,
            "forks_count": 0,
            "full_name": "tiandi/test_yf_repo",
            "has_issue": false,
            "homepage": "https://gitcode.com/tiandi/test_yf_repo",
            "http_url_to_repo": "https://gitcode.com/tiandi/test_yf_repo.git",
            "human_name": "Hongmen / test_yf_repo",
            "id": 4028329,
            "internal": false,
            "members": [
              "aron1"
            ],
            "name": "test_yf_repo",
            "namespace": {
              "html_url": "https://gitcode.com/tiandi",
              "id": 1420034,
              "name": "Red Gang",
              "path": "tiandi",
              "type": "enterprise"
            },
            "open_issues_count": 0,
            "owner": {
              "id": "444601",
              "login": "yanfan",
              "name": "abcabcabc",
              "type": "User"
            },
            "path": "test_yf_repo",
            "permission": {
              "admin": true,
              "pull": true,
              "push": true
            },
            "private": true,
            "project_labels": [],
            "public": false,
            "relation": "master",
            "ssh_url_to_repo": "git@gitcode.com:tiandi/test_yf_repo.git",
            "stargazers_count": 0,
            "status": "start",
            "url": "https://api.gitcode.com/api/v5/repos/tiandi/test_yf_repo",
            "watched": false,
            "watchers_count": 0,
            "web_url": "https://gitcode.com/tiandi/test_yf_repo"
          },
          "schema": {
            "items": {
              "properties": {
                "assignee": {
                  "items": {
                    "properties": {
                      "avatar_url": {
                        "type": "string"
                      },
                      "html_url": {
                        "type": "string"
                      },
                      "id": {
                        "type": "string"
                      },
                      "login": {
                        "type": "string"
                      },
                      "name": {
                        "type": "string"
                      },
                      "type": {
                        "type": "string"
                      }
                    },
                    "type": "object"
                  },
                  "type": "array"
                },
                "assignees_number": {
                  "type": "integer"
                },
                "assigner": {
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "login": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "default_branch": {
                  "type": "string"
                },
                "description": {
                  "type": "string"
                },
                "enterprise": {
                  "properties": {
                    "html_url": {
                      "type": "string"
                    },
                    "id": {
                      "type": "integer"
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
                "fork": {
                  "type": "integer"
                },
                "forks_count": {
                  "type": "integer"
                },
                "full_name": {
                  "type": "string"
                },
                "has_issue": {
                  "type": "integer"
                },
                "homepage": {
                  "type": "string"
                },
                "http_url_to_repo": {
                  "type": "string"
                },
                "human_name": {
                  "type": "string"
                },
                "id": {
                  "type": "integer"
                },
                "internal": {
                  "type": "integer"
                },
                "members": {
                  "items": {
                    "type": "string"
                  },
                  "type": "array"
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
                "owner": {
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "login": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "path": {
                  "type": "string"
                },
                "permission": {
                  "properties": {
                    "admin": {
                      "type": "integer"
                    },
                    "pull": {
                      "type": "integer"
                    },
                    "push": {
                      "type": "integer"
                    }
                  },
                  "type": "object"
                },
                "private": {
                  "type": "integer"
                },
                "project_labels": {
                  "items": {
                    "properties": {},
                    "type": "object"
                  },
                  "type": "array"
                },
                "public": {
                  "type": "integer"
                },
                "relation": {
                  "type": "string"
                },
                "repo_type": {
                  "type": "string"
                },
                "ssh_url_to_repo": {
                  "type": "string"
                },
                "stargazers_count": {
                  "type": "integer"
                },
                "status": {
                  "type": "string"
                },
                "url": {
                  "type": "string"
                },
                "watched": {
                  "type": "integer"
                },
                "watchers_count": {
                  "type": "integer"
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
    "Users"
  ]
}
```
