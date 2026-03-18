# Get User Personal Dynamics
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-users-username-events](https://docs.gitcode.com/en/docs/apis/get-api-v-5-users-username-events)
Category: Users
- Method: `GET`
- Path: `/api/v5/users/{username}/events`
- Operation ID: `get_api_v5_users_{username}_events`
- Tags: `Users`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| username | path | true | string |  |
| access_token | query | true | string | User authorization code |
| year | query | false | string | Start Year (2024) |
| next | query | false | string | End date |
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
    "events": {
      "properties": {
        "2024-08-27": {
          "items": {
            "properties": {
              "_links": {
                "properties": {
                  "action_type": {
                    "type": "string"
                  },
                  "project": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "action": {
                "type": "integer"
              },
              "action_name": {
                "type": "string"
              },
              "author": {
                "properties": {
                  "avatar_url": {
                    "type": "string"
                  },
                  "email": {
                    "type": "string"
                  },
                  "iam_id": {
                    "type": "string"
                  },
                  "id": {
                    "type": "integer"
                  },
                  "name": {
                    "type": "string"
                  },
                  "name_cn": {
                    "type": "string"
                  },
                  "state": {
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
              "author_id": {
                "type": "integer"
              },
              "author_username": {
                "type": "string"
              },
              "created_at": {
                "type": "string"
              },
              "project": {
                "properties": {
                  "develop_mode": {
                    "type": "string"
                  },
                  "forks_count": {
                    "type": "integer"
                  },
                  "main_repository_language": {
                    "items": {
                      "type": "null"
                    },
                    "type": "array"
                  },
                  "star_count": {
                    "type": "integer"
                  },
                  "stared": {
                    "type": "integer"
                  }
                },
                "type": "object"
              },
              "project_id": {
                "type": "integer"
              },
              "project_name": {
                "type": "string"
              },
              "push_data": {
                "properties": {
                  "action": {
                    "type": "string"
                  },
                  "commit_count": {
                    "type": "integer"
                  },
                  "commit_from": {
                    "type": "string"
                  },
                  "commit_title": {
                    "type": "string"
                  },
                  "commit_to": {
                    "type": "string"
                  },
                  "ref": {
                    "type": "string"
                  },
                  "ref_type": {
                    "type": "string"
                  }
                },
                "type": "object"
              }
            },
            "type": "object"
          },
          "type": "array"
        }
      },
      "type": "object"
    },
    "next": {
      "type": "string"
    }
  },
  "type": "object"
}
```
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": {
      "events": {
        "2024-08-27": [
          {
            "_links": {
              "action_type": "",
              "project": "https://test.gitcode.net/mactribe/midsommarcartoon"
            },
            "action": 5,
            "action_name": "pushed to",
            "author": {
              "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/fa/fe/f32a9fecc53e890afbd48fd098b0f6c5f20f062581400c76c85e5baab3f0d5b2.png",
              "email": "",
              "iam_id": "5c340cab034d455992541f00f9936fb4",
              "id": 704,
              "name": "dengmengmian",
              "name_cn": "dengmengmian",
              "state": "active",
              "username": "dengmengmian",
              "web_url": "https://test.gitcode.net/dengmengmian"
            },
            "author_id": 704,
            "author_username": "dengmengmian",
            "created_at": "2024-08-27T10:34:05.093Z",
            "project": {
              "develop_mode": "normal",
              "forks_count": 0,
              "main_repository_language": [
                null,
                null
              ],
              "star_count": 0,
              "stared": false
            },
            "project_id": 507167,
            "project_name": "mactribe/midsommarcartoon",
            "push_data": {
              "action": "pushed",
              "commit_count": 1,
              "commit_from": "2ce472fec073f77804c3480ccf128219a6172e54",
              "commit_title": "File title",
              "commit_to": "14b742fe434797fb073ba536804011f735f2f430",
              "ref": "main",
              "ref_type": "branch"
            }
          },
          {
            "_links": {
              "action_type": "",
              "project": "https://test.gitcode.net/mactribe/midsommarcartoon"
            },
            "action": 5,
            "action_name": "pushed to",
            "author": {
              "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/fa/fe/f32a9fecc53e890afbd48fd098b0f6c5f20f062581400c76c85e5baab3f0d5b2.png",
              "email": "",
              "iam_id": "5c340cab034d455992541f00f9936fb4",
              "id": 704,
              "name": "dengmengmian",
              "name_cn": "dengmengmian",
              "state": "active",
              "username": "dengmengmian",
              "web_url": "https://test.gitcode.net/dengmengmian"
            },
            "author_id": 704,
            "author_username": "dengmengmian",
            "created_at": "2024-08-27T10:31:17.494Z",
            "project": {
              "develop_mode": "normal",
              "forks_count": 0,
              "main_repository_language": [
                null,
                null
              ],
              "star_count": 0,
              "stared": false
            },
            "project_id": 507167,
            "project_name": "mactribe/midsommarcartoon",
            "push_data": {
              "action": "pushed",
              "commit_count": 1,
              "commit_from": "ee25b0353dae9bf19f5e3e733e651e7870020386",
              "commit_title": "File title",
              "commit_to": "2ce472fec073f77804c3480ccf128219a6172e54",
              "ref": "main",
              "ref_type": "branch"
            }
          }
        ]
      },
      "next": "2024-08-01T10:10:40.370Z"
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
  "operationId": "get_api_v5_users_{username}_events",
  "parameters": [
    {
      "description": "",
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
      "description": "Start Year (2024)",
      "in": "query",
      "name": "year",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "End date",
      "in": "query",
      "name": "next",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/users/{username}/events",
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
    "name": "Get User Personal Dynamics",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "users",
        ":username",
        "events"
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
            "content": "Start Year (2024)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "year",
          "value": ""
        },
        {
          "description": {
            "content": "End date",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "next",
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
                "events": {
                  "2024-08-27": [
                    {
                      "_links": {
                        "action_type": "",
                        "project": "https://test.gitcode.net/mactribe/midsommarcartoon"
                      },
                      "action": 5,
                      "action_name": "pushed to",
                      "author": {
                        "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/fa/fe/f32a9fecc53e890afbd48fd098b0f6c5f20f062581400c76c85e5baab3f0d5b2.png",
                        "email": "",
                        "iam_id": "5c340cab034d455992541f00f9936fb4",
                        "id": 704,
                        "name": "dengmengmian",
                        "name_cn": "dengmengmian",
                        "state": "active",
                        "username": "dengmengmian",
                        "web_url": "https://test.gitcode.net/dengmengmian"
                      },
                      "author_id": 704,
                      "author_username": "dengmengmian",
                      "created_at": "2024-08-27T10:34:05.093Z",
                      "project": {
                        "develop_mode": "normal",
                        "forks_count": 0,
                        "main_repository_language": [
                          null,
                          null
                        ],
                        "star_count": 0,
                        "stared": false
                      },
                      "project_id": 507167,
                      "project_name": "mactribe/midsommarcartoon",
                      "push_data": {
                        "action": "pushed",
                        "commit_count": 1,
                        "commit_from": "2ce472fec073f77804c3480ccf128219a6172e54",
                        "commit_title": "File title",
                        "commit_to": "14b742fe434797fb073ba536804011f735f2f430",
                        "ref": "main",
                        "ref_type": "branch"
                      }
                    },
                    {
                      "_links": {
                        "action_type": "",
                        "project": "https://test.gitcode.net/mactribe/midsommarcartoon"
                      },
                      "action": 5,
                      "action_name": "pushed to",
                      "author": {
                        "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/fa/fe/f32a9fecc53e890afbd48fd098b0f6c5f20f062581400c76c85e5baab3f0d5b2.png",
                        "email": "",
                        "iam_id": "5c340cab034d455992541f00f9936fb4",
                        "id": 704,
                        "name": "dengmengmian",
                        "name_cn": "dengmengmian",
                        "state": "active",
                        "username": "dengmengmian",
                        "web_url": "https://test.gitcode.net/dengmengmian"
                      },
                      "author_id": 704,
                      "author_username": "dengmengmian",
                      "created_at": "2024-08-27T10:31:17.494Z",
                      "project": {
                        "develop_mode": "normal",
                        "forks_count": 0,
                        "main_repository_language": [
                          null,
                          null
                        ],
                        "star_count": 0,
                        "stared": false
                      },
                      "project_id": 507167,
                      "project_name": "mactribe/midsommarcartoon",
                      "push_data": {
                        "action": "pushed",
                        "commit_count": 1,
                        "commit_from": "ee25b0353dae9bf19f5e3e733e651e7870020386",
                        "commit_title": "File title",
                        "commit_to": "2ce472fec073f77804c3480ccf128219a6172e54",
                        "ref": "main",
                        "ref_type": "branch"
                      }
                    }
                  ]
                },
                "next": "2024-08-01T10:10:40.370Z"
              }
            }
          },
          "schema": {
            "properties": {
              "events": {
                "properties": {
                  "2024-08-27": {
                    "items": {
                      "properties": {
                        "_links": {
                          "properties": {
                            "action_type": {
                              "type": "string"
                            },
                            "project": {
                              "type": "string"
                            }
                          },
                          "type": "object"
                        },
                        "action": {
                          "type": "integer"
                        },
                        "action_name": {
                          "type": "string"
                        },
                        "author": {
                          "properties": {
                            "avatar_url": {
                              "type": "string"
                            },
                            "email": {
                              "type": "string"
                            },
                            "iam_id": {
                              "type": "string"
                            },
                            "id": {
                              "type": "integer"
                            },
                            "name": {
                              "type": "string"
                            },
                            "name_cn": {
                              "type": "string"
                            },
                            "state": {
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
                        "author_id": {
                          "type": "integer"
                        },
                        "author_username": {
                          "type": "string"
                        },
                        "created_at": {
                          "type": "string"
                        },
                        "project": {
                          "properties": {
                            "develop_mode": {
                              "type": "string"
                            },
                            "forks_count": {
                              "type": "integer"
                            },
                            "main_repository_language": {
                              "items": {
                                "type": "null"
                              },
                              "type": "array"
                            },
                            "star_count": {
                              "type": "integer"
                            },
                            "stared": {
                              "type": "integer"
                            }
                          },
                          "type": "object"
                        },
                        "project_id": {
                          "type": "integer"
                        },
                        "project_name": {
                          "type": "string"
                        },
                        "push_data": {
                          "properties": {
                            "action": {
                              "type": "string"
                            },
                            "commit_count": {
                              "type": "integer"
                            },
                            "commit_from": {
                              "type": "string"
                            },
                            "commit_title": {
                              "type": "string"
                            },
                            "commit_to": {
                              "type": "string"
                            },
                            "ref": {
                              "type": "string"
                            },
                            "ref_type": {
                              "type": "string"
                            }
                          },
                          "type": "object"
                        }
                      },
                      "type": "object"
                    },
                    "type": "array"
                  }
                },
                "type": "object"
              },
              "next": {
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
