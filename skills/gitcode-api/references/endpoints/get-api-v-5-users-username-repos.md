# Get a User's Public Repositories
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-users-username-repos](https://docs.gitcode.com/en/docs/apis/get-api-v-5-users-username-repos)
Category: Users
- Method: `GET`
- Path: `/api/v5/users/{username}/repos`
- Operation ID: `get_api_v5_users_{username}_repos`
- Tags: `Users`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| username | path | true | string | username (alias: login) |
| access_token | query | true | string | User authorization code |
| type | query | false | string | User-created repository (owner), personal repository (personal), member of a repository (member), all (all). Default: all (all). |
| sort | query | false | string | Sort by: created, updated, pushed, full_name. Default: full_name |
| direction | query | false | string | If the sort parameter is full_name, use ascending (asc). Otherwise, use descending (desc). |
| page | query | false | integer | The current page number |
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
      "gitee": {
        "properties": {
          "fork": {
            "type": "integer"
          },
          "star": {
            "type": "integer"
          },
          "watch": {
            "type": "integer"
          }
        },
        "type": "object"
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
      "issue_template_source": {
        "type": "string"
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
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": {
      "assignee": [
        {
          "avatar_url": "https://cdn-img.gitcode.com/ec/fb/430ecf07b9ee91bbbbf341d92a36783d06e69086f82ce8cf5a6406f79f1c9cf4.png",
          "html_url": "https://gitcode.com/dengmengmian",
          "id": "268",
          "login": "dengmengmian",
          "name": "Mavan",
          "type": "User"
        }
      ],
      "assignees_number": 1,
      "assigner": {
        "id": "268",
        "login": "dengmengmian",
        "name": "Mavan",
        "type": "User"
      },
      "default_branch": "master",
      "description": "manifest",
      "enterprise": {
        "html_url": "https://gitcode.com/dengmengmian",
        "id": 199940,
        "path": "dengmengmian",
        "type": "user"
      },
      "fork": false,
      "forks_count": 0,
      "full_name": "dengmengmian/manifest",
      "gitee": {
        "fork": 15,
        "star": 10,
        "watch": 1
      },
      "has_issue": false,
      "homepage": "https://gitcode.com/dengmengmian/manifest",
      "http_url_to_repo": "https://gitcode.com/dengmengmian/manifest.git",
      "human_name": "dengmengmian / manifest",
      "id": 2734882,
      "internal": false,
      "issue_template_source": "project",
      "members": [
        "dengmengmian"
      ],
      "name": "manifest",
      "namespace": {
        "html_url": "https://gitcode.com/dengmengmian",
        "id": 199940,
        "name": "dengmengmian",
        "path": "dengmengmian",
        "type": "user"
      },
      "open_issues_count": 0,
      "owner": {
        "id": "268",
        "login": "dengmengmian",
        "name": "Mavan",
        "type": "User"
      },
      "path": "manifest",
      "permission": {
        "admin": true,
        "pull": true,
        "push": true
      },
      "private": false,
      "project_labels": [],
      "public": true,
      "relation": "master",
      "ssh_url_to_repo": "git@gitcode.com:dengmengmian/manifest.git",
      "stargazers_count": 0,
      "status": "start",
      "url": "https://api.gitcode.com/api/v5/repos/dengmengmian/manifest",
      "watched": false,
      "watchers_count": 0,
      "web_url": "https://gitcode.com/dengmengmian/manifest"
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
  "operationId": "get_api_v5_users_{username}_repos",
  "parameters": [
    {
      "description": "username (alias: login)",
      "example": "",
      "in": "path",
      "name": "username",
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
      "description": "User-created repository (owner), personal repository (personal), member of a repository (member), all (all). Default: all (all).",
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
    }
  ],
  "path": "/api/v5/users/{username}/repos",
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
    "name": "Get a User's Public Repositories",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "users",
        ":username",
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
            "content": "User-created repository (owner), personal repository (personal), member of a repository (member), all (all). Default: all (all).",
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
        }
      ],
      "variable": [
        {
          "description": {
            "content": "(Required) username (alias: login)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "username",
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
                "assignee": [
                  {
                    "avatar_url": "https://cdn-img.gitcode.com/ec/fb/430ecf07b9ee91bbbbf341d92a36783d06e69086f82ce8cf5a6406f79f1c9cf4.png",
                    "html_url": "https://gitcode.com/dengmengmian",
                    "id": "268",
                    "login": "dengmengmian",
                    "name": "Mavan",
                    "type": "User"
                  }
                ],
                "assignees_number": 1,
                "assigner": {
                  "id": "268",
                  "login": "dengmengmian",
                  "name": "Mavan",
                  "type": "User"
                },
                "default_branch": "master",
                "description": "manifest",
                "enterprise": {
                  "html_url": "https://gitcode.com/dengmengmian",
                  "id": 199940,
                  "path": "dengmengmian",
                  "type": "user"
                },
                "fork": false,
                "forks_count": 0,
                "full_name": "dengmengmian/manifest",
                "gitee": {
                  "fork": 15,
                  "star": 10,
                  "watch": 1
                },
                "has_issue": false,
                "homepage": "https://gitcode.com/dengmengmian/manifest",
                "http_url_to_repo": "https://gitcode.com/dengmengmian/manifest.git",
                "human_name": "dengmengmian / manifest",
                "id": 2734882,
                "internal": false,
                "issue_template_source": "project",
                "members": [
                  "dengmengmian"
                ],
                "name": "manifest",
                "namespace": {
                  "html_url": "https://gitcode.com/dengmengmian",
                  "id": 199940,
                  "name": "dengmengmian",
                  "path": "dengmengmian",
                  "type": "user"
                },
                "open_issues_count": 0,
                "owner": {
                  "id": "268",
                  "login": "dengmengmian",
                  "name": "Mavan",
                  "type": "User"
                },
                "path": "manifest",
                "permission": {
                  "admin": true,
                  "pull": true,
                  "push": true
                },
                "private": false,
                "project_labels": [],
                "public": true,
                "relation": "master",
                "ssh_url_to_repo": "git@gitcode.com:dengmengmian/manifest.git",
                "stargazers_count": 0,
                "status": "start",
                "url": "https://api.gitcode.com/api/v5/repos/dengmengmian/manifest",
                "watched": false,
                "watchers_count": 0,
                "web_url": "https://gitcode.com/dengmengmian/manifest"
              }
            }
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
                "gitee": {
                  "properties": {
                    "fork": {
                      "type": "integer"
                    },
                    "star": {
                      "type": "integer"
                    },
                    "watch": {
                      "type": "integer"
                    }
                  },
                  "type": "object"
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
                "issue_template_source": {
                  "type": "string"
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
