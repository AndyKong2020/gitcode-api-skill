# List Repositories Watched By User
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-user-username-subscriptions](https://docs.gitcode.com/en/docs/apis/get-api-v-5-user-username-subscriptions)
Category: Users
- Method: `GET`
- Path: `/api/v5/users/{username}/subscriptions`
- Operation ID: `get_api_v5_user_{username}_subscriptions`
- Tags: `Users`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| username | path | true | string |  |
| access_token | query | false | string | User authorization code |
| sort | query | false | string | created/last_push Sort by repository creation time (created) or last push time (updated), default: creation time |
| direction | query | false | string | sort direction, default: desc |
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
      "created_at": {
        "title": "creation time",
        "type": "string"
      },
      "default_branch": {
        "title": "Default branch",
        "type": "string"
      },
      "description": {
        "title": "Repository description",
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
        "title": "Enterprise Information of the Repository",
        "type": "object"
      },
      "fork": {
        "title": "Whether to fork the repository",
        "type": "integer"
      },
      "forks_count": {
        "title": "fork count",
        "type": "integer"
      },
      "full_name": {
        "title": "full repository path",
        "type": "string"
      },
      "has_issue": {
        "type": "integer"
      },
      "has_issues": {
        "title": "Whether to enable issue feature",
        "type": "integer"
      },
      "homepage": {
        "title": "Repository homepage",
        "type": "string"
      },
      "http_url_to_repo": {
        "title": "Library HTTP Git URL",
        "type": "string"
      },
      "human_name": {
        "title": "Full warehouse name",
        "type": "string"
      },
      "id": {
        "title": "Repository ID",
        "type": "integer"
      },
      "internal": {
        "title": "internal open source",
        "type": "integer"
      },
      "issue_template_source": {
        "title": "Issue template source project: Use repository issue templates as the template; enterprise: Use corporate work items as the template",
        "type": "string"
      },
      "members": {
        "items": {
          "type": "string"
        },
        "title": "member",
        "type": "array"
      },
      "name": {
        "title": "Repository name",
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
        "title": "Repository namespace information",
        "type": "object"
      },
      "open_issues_count": {
        "title": "The number of open issues",
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
        "title": "Repository owner information",
        "type": "object"
      },
      "parent": {
        "properties": {
          "full_name": {
            "type": "string"
          },
          "human_name": {
            "type": "string"
          }
        },
        "title": "parent repository",
        "type": "object"
      },
      "parentfull_name": {
        "title": "Parent repository name",
        "type": "string"
      },
      "path": {
        "title": "Repository path",
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
        "title": "Operation permission",
        "type": "object"
      },
      "private": {
        "title": "private repository flag",
        "type": "integer"
      },
      "project_creator": {
        "title": "Repository creator",
        "type": "string"
      },
      "public": {
        "title": "IsRepositoryPublic",
        "type": "integer"
      },
      "pushed_at": {
        "title": "The most recent code push time",
        "type": "string"
      },
      "relation": {
        "title": "current user's role in relation to the repository",
        "type": "string"
      },
      "ssh_url_to_repo": {
        "title": "repository ssh git address",
        "type": "string"
      },
      "stargazers_count": {
        "title": "star count",
        "type": "integer"
      },
      "status": {
        "title": "warehouse status",
        "type": "string"
      },
      "updated_at": {
        "title": "Update time",
        "type": "string"
      },
      "url": {
        "title": "Repository details access URL",
        "type": "string"
      },
      "watchers_count": {
        "title": "watch count",
        "type": "integer"
      },
      "web_url": {
        "title": "Repository web access URL",
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
      "created_at": "2024-12-11T17:41:14.536+08:00",
      "default_branch": "main",
      "description": "Trump",
      "enterprise": {
        "html_url": "https://gitcode.com/xiaogang",
        "id": 137117,
        "path": "xiaogang",
        "type": "user"
      },
      "fork": true,
      "forks_count": 0,
      "full_name": "xiaogang/private-new2",
      "has_issue": false,
      "has_issues": false,
      "homepage": "https://gitcode.com/xiaogang/private-new2",
      "http_url_to_repo": "https://gitcode.com/xiaogang/private-new2.git",
      "human_name": "xiaogang / private-new2",
      "id": 777621,
      "internal": false,
      "issue_template_source": "project",
      "members": [
        "xiaogang"
      ],
      "name": "private-new2",
      "namespace": {
        "html_url": "https://gitcode.com/xiaogang",
        "id": 137117,
        "name": "xiaogang",
        "path": "xiaogang",
        "type": "user"
      },
      "open_issues_count": 0,
      "owner": {
        "id": "496",
        "login": "xiaogang",
        "name": "Xiao Gang",
        "type": "User"
      },
      "parent": {
        "full_name": "xiaogang_test/private-new",
        "human_name": "xiaogang_test / private-new"
      },
      "parentfull_name": "xiaogang_test/private-new",
      "path": "private-new2",
      "permission": {
        "admin": true,
        "pull": true,
        "push": true
      },
      "private": false,
      "project_creator": "xiaogang",
      "public": true,
      "pushed_at": "2024-12-20T19:14:34.979+08:00",
      "relation": "master",
      "ssh_url_to_repo": "ssh://git@gitcode.com:2222/xiaogang/private-new2.git",
      "stargazers_count": 1,
      "status": "start",
      "updated_at": "2024-12-11T17:41:14.536+08:00",
      "url": "https://api.gitcode.com/api/v5/repos/xiaogang/private-new2",
      "watchers_count": 0,
      "web_url": "https://gitcode.com/xiaogang/private-new2"
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
  "operationId": "get_api_v5_user_{username}_subscriptions",
  "parameters": [
    {
      "description": "",
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
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "created/last_push Sort by repository creation time (created) or last push time (updated), default: creation time",
      "in": "query",
      "name": "sort",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "sort direction, default: desc",
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
  "path": "/api/v5/users/{username}/subscriptions",
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
    "name": "List Repositories Watched By User",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "users",
        ":username",
        "subscriptions"
      ],
      "query": [
        {
          "description": {
            "content": "User authorization code",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "access_token",
          "value": ""
        },
        {
          "description": {
            "content": "created/last_push Sort by repository creation time (created) or last push time (updated), default: creation time",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sort",
          "value": ""
        },
        {
          "description": {
            "content": "sort direction, default: desc",
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
            "content": "(Required) ",
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
                "created_at": "2024-12-11T17:41:14.536+08:00",
                "default_branch": "main",
                "description": "Trump",
                "enterprise": {
                  "html_url": "https://gitcode.com/xiaogang",
                  "id": 137117,
                  "path": "xiaogang",
                  "type": "user"
                },
                "fork": true,
                "forks_count": 0,
                "full_name": "xiaogang/private-new2",
                "has_issue": false,
                "has_issues": false,
                "homepage": "https://gitcode.com/xiaogang/private-new2",
                "http_url_to_repo": "https://gitcode.com/xiaogang/private-new2.git",
                "human_name": "xiaogang / private-new2",
                "id": 777621,
                "internal": false,
                "issue_template_source": "project",
                "members": [
                  "xiaogang"
                ],
                "name": "private-new2",
                "namespace": {
                  "html_url": "https://gitcode.com/xiaogang",
                  "id": 137117,
                  "name": "xiaogang",
                  "path": "xiaogang",
                  "type": "user"
                },
                "open_issues_count": 0,
                "owner": {
                  "id": "496",
                  "login": "xiaogang",
                  "name": "Xiao Gang",
                  "type": "User"
                },
                "parent": {
                  "full_name": "xiaogang_test/private-new",
                  "human_name": "xiaogang_test / private-new"
                },
                "parentfull_name": "xiaogang_test/private-new",
                "path": "private-new2",
                "permission": {
                  "admin": true,
                  "pull": true,
                  "push": true
                },
                "private": false,
                "project_creator": "xiaogang",
                "public": true,
                "pushed_at": "2024-12-20T19:14:34.979+08:00",
                "relation": "master",
                "ssh_url_to_repo": "ssh://git@gitcode.com:2222/xiaogang/private-new2.git",
                "stargazers_count": 1,
                "status": "start",
                "updated_at": "2024-12-11T17:41:14.536+08:00",
                "url": "https://api.gitcode.com/api/v5/repos/xiaogang/private-new2",
                "watchers_count": 0,
                "web_url": "https://gitcode.com/xiaogang/private-new2"
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "created_at": {
                  "title": "creation time",
                  "type": "string"
                },
                "default_branch": {
                  "title": "Default branch",
                  "type": "string"
                },
                "description": {
                  "title": "Repository description",
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
                  "title": "Enterprise Information of the Repository",
                  "type": "object"
                },
                "fork": {
                  "title": "Whether to fork the repository",
                  "type": "integer"
                },
                "forks_count": {
                  "title": "fork count",
                  "type": "integer"
                },
                "full_name": {
                  "title": "full repository path",
                  "type": "string"
                },
                "has_issue": {
                  "type": "integer"
                },
                "has_issues": {
                  "title": "Whether to enable issue feature",
                  "type": "integer"
                },
                "homepage": {
                  "title": "Repository homepage",
                  "type": "string"
                },
                "http_url_to_repo": {
                  "title": "Library HTTP Git URL",
                  "type": "string"
                },
                "human_name": {
                  "title": "Full warehouse name",
                  "type": "string"
                },
                "id": {
                  "title": "Repository ID",
                  "type": "integer"
                },
                "internal": {
                  "title": "internal open source",
                  "type": "integer"
                },
                "issue_template_source": {
                  "title": "Issue template source project: Use repository issue templates as the template; enterprise: Use corporate work items as the template",
                  "type": "string"
                },
                "members": {
                  "items": {
                    "type": "string"
                  },
                  "title": "member",
                  "type": "array"
                },
                "name": {
                  "title": "Repository name",
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
                  "title": "Repository namespace information",
                  "type": "object"
                },
                "open_issues_count": {
                  "title": "The number of open issues",
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
                  "title": "Repository owner information",
                  "type": "object"
                },
                "parent": {
                  "properties": {
                    "full_name": {
                      "type": "string"
                    },
                    "human_name": {
                      "type": "string"
                    }
                  },
                  "title": "parent repository",
                  "type": "object"
                },
                "parentfull_name": {
                  "title": "Parent repository name",
                  "type": "string"
                },
                "path": {
                  "title": "Repository path",
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
                  "title": "Operation permission",
                  "type": "object"
                },
                "private": {
                  "title": "private repository flag",
                  "type": "integer"
                },
                "project_creator": {
                  "title": "Repository creator",
                  "type": "string"
                },
                "public": {
                  "title": "IsRepositoryPublic",
                  "type": "integer"
                },
                "pushed_at": {
                  "title": "The most recent code push time",
                  "type": "string"
                },
                "relation": {
                  "title": "current user's role in relation to the repository",
                  "type": "string"
                },
                "ssh_url_to_repo": {
                  "title": "repository ssh git address",
                  "type": "string"
                },
                "stargazers_count": {
                  "title": "star count",
                  "type": "integer"
                },
                "status": {
                  "title": "warehouse status",
                  "type": "string"
                },
                "updated_at": {
                  "title": "Update time",
                  "type": "string"
                },
                "url": {
                  "title": "Repository details access URL",
                  "type": "string"
                },
                "watchers_count": {
                  "title": "watch count",
                  "type": "integer"
                },
                "web_url": {
                  "title": "Repository web access URL",
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
