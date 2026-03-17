# Update Issue
Source: [https://docs.gitcode.com/en/docs/apis/patch-api-v-5-repos-owner-issues-number](https://docs.gitcode.com/en/docs/apis/patch-api-v-5-repos-owner-issues-number)
Category: Issues
- Method: `PATCH`
- Path: `/api/v5/repos/{owner}/issues/{number}`
- Operation ID: `patch_api_v5_repos_{owner}_issues_{number}`
- Tags: `Issues`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| number | path | true | string | Which issue number, the ordinal number of the issue in this repository |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "assignee": {
      "description": "Issue Owner's username, separated by English commas for multiple ones",
      "type": "string"
    },
    "body": {
      "description": "Issue Description",
      "type": "string"
    },
    "custom_fields": {
      "description": "Custom field information (Enterprise edition supported)",
      "items": {
        "properties": {
          "field_name": {
            "description": "Field Name",
            "type": "string"
          },
          "field_values": {
            "description": "Field value array",
            "items": {
              "type": "string"
            },
            "type": "array"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "issue_severity": {
      "description": "Issue Priority (Enterprise Edition Supported)",
      "type": "string"
    },
    "labels": {
      "description": "A comma-separated list of labels, where the name must be between 2-20 characters long and cannot contain special characters. For example: bug,performance",
      "type": "string"
    },
    "milestone": {
      "description": "Milestone Sequence Number",
      "type": "integer"
    },
    "repo": {
      "description": "Repository path",
      "type": "string"
    },
    "security_hole": {
      "description": "Whether it is a private issue (default is false)",
      "type": "string"
    },
    "state": {
      "description": "Issue Status, reopen (open)、close (closed)",
      "type": "string"
    },
    "status": {
      "description": "Issue Status (Enterprise Edition Supported)",
      "type": "string"
    },
    "title": {
      "description": "Issue Title",
      "type": "string"
    }
  },
  "required": [
    "repo",
    "title",
    "issue_severity"
  ],
  "type": "object"
}
```
Example:
```json
"{\n    \"repo\": \"test666\",\n    \"title\": \"fsds11\",\n    \"body\": \"new body\",\n    \"state\": \"closed\",\n    \"assignee\": \"aron1\",\n    \"milestone\": \"0706\",\n    \"labels\": \"new label\",\n    // \"security_hole\": \"\",\n    \"status\": \"rejected\"\n}"
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
    "assignee": {
      "properties": {
        "avatar_url": {
          "type": "string"
        },
        "events_url": {
          "type": "null"
        },
        "followers_url": {
          "type": "null"
        },
        "following_url": {
          "type": "null"
        },
        "gists_url": {
          "type": "null"
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
        "member_role": {
          "type": "null"
        },
        "name": {
          "type": "string"
        },
        "organizations_url": {
          "type": "null"
        },
        "received_events_url": {
          "type": "null"
        },
        "remark": {
          "type": "null"
        },
        "repos_url": {
          "type": "null"
        },
        "starred_url": {
          "type": "null"
        },
        "subscriptions_url": {
          "type": "null"
        },
        "type": {
          "type": "null"
        },
        "url": {
          "type": "null"
        }
      },
      "type": "object"
    },
    "body": {
      "type": "string"
    },
    "created_at": {
      "type": "string"
    },
    "custom_fields": {
      "description": "Custom field information (Enterprise edition supported)",
      "items": {
        "properties": {
          "field_name": {
            "description": "Custom Field Name",
            "type": "string"
          },
          "field_type": {
            "description": "Field type. text_single: single line text, text_multi: multi-line text, integer: integer, decimal: decimal, date: date, select_single: single select dropdown, select_multi: multi-select dropdown, member_single: single select member, member_multi: multi-select member",
            "type": "string"
          },
          "field_values": {
            "description": "Custom field value",
            "items": {
              "type": "string"
            },
            "type": "array"
          },
          "field_visibility": {
            "description": "Visibility. 0: Visible to administrators only, 1: Visible to everyone",
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "finished_at": {
      "type": "string"
    },
    "html_url": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    },
    "labels": {
      "items": {
        "properties": {
          "color": {
            "type": "string"
          },
          "id": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "number": {
      "type": "integer"
    },
    "repository": {
      "properties": {
        "created_at": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "full_name": {
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
        "updated_at": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "severity": {
      "type": "string"
    },
    "stage": {
      "type": "string"
    },
    "state": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "updated_at": {
      "type": "string"
    },
    "user": {
      "properties": {
        "avatar_url": {
          "type": "string"
        },
        "events_url": {
          "type": "null"
        },
        "followers_url": {
          "type": "null"
        },
        "following_url": {
          "type": "null"
        },
        "gists_url": {
          "type": "null"
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
        "member_role": {
          "type": "null"
        },
        "name": {
          "type": "string"
        },
        "organizations_url": {
          "type": "null"
        },
        "received_events_url": {
          "type": "null"
        },
        "remark": {
          "type": "null"
        },
        "repos_url": {
          "type": "null"
        },
        "starred_url": {
          "type": "null"
        },
        "subscriptions_url": {
          "type": "null"
        },
        "type": {
          "type": "null"
        },
        "url": {
          "type": "null"
        }
      },
      "type": "object"
    }
  },
  "type": "object"
}
```
Example:
```json
{
  "assignee": {
    "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/fa/fe/f32a9fecc53e890afbd48fd098b0f6c5f20f062581400c76c85e5baab3f0d5b2.png",
    "events_url": null,
    "followers_url": null,
    "following_url": null,
    "gists_url": null,
    "html_url": "https://test.gitcode.net/dengmengmian",
    "id": "661ce4eab470b1430d456154",
    "login": "dengmengmian",
    "member_role": null,
    "name": "MaFan_",
    "organizations_url": null,
    "received_events_url": null,
    "remark": null,
    "repos_url": null,
    "starred_url": null,
    "subscriptions_url": null,
    "type": null,
    "url": null
  },
  "body": "abcabcabc",
  "created_at": "2024-04-16T14:38:43.464+08:00",
  "finished_at": "2024-04-16T14:49:45.166+08:00",
  "html_url": "https://test.gitcode.net/dengmengmian/test01/issues/14",
  "id": 152467,
  "labels": [
    {
      "color": "#428BCA",
      "id": 382389,
      "name": "ad"
    },
    {
      "color": "#428BCA",
      "id": 382388,
      "name": "id"
    }
  ],
  "number": 14,
  "repository": {
    "created_at": "2024-04-16T14:38:43.464+08:00",
    "description": "",
    "full_name": "dengmengmian/test01",
    "id": 152467,
    "name": "test01",
    "path": "test01",
    "updated_at": "2024-04-18T18:27:21.955+08:00"
  },
  "severity": "Major",
  "stage": "New",
  "state": "closed",
  "title": "abcabcabc",
  "updated_at": "2024-04-18T18:27:21.955+08:00",
  "user": {
    "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/fa/fe/f32a9fecc53e890afbd48fd098b0f6c5f20f062581400c76c85e5baab3f0d5b2.png",
    "events_url": null,
    "followers_url": null,
    "following_url": null,
    "gists_url": null,
    "html_url": "https://test.gitcode.net/dengmengmian",
    "id": "661ce4eab470b1430d456154",
    "login": "dengmengmian",
    "member_role": null,
    "name": "MaFan_",
    "organizations_url": null,
    "received_events_url": null,
    "remark": null,
    "repos_url": null,
    "starred_url": null,
    "subscriptions_url": null,
    "type": null,
    "url": null
  }
}
```
## JSON Request Example
```json
{
  "assignee": "string",
  "body": "string",
  "custom_fields": [
    {
      "field_name": "string",
      "field_values": [
        "string"
      ]
    }
  ],
  "issue_severity": "string",
  "labels": "string",
  "milestone": 0,
  "repo": "string",
  "security_hole": "string",
  "state": "string",
  "status": "string",
  "title": "string"
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
    "assignee": "string",
    "body": "string",
    "custom_fields": [
      {
        "field_name": "string",
        "field_values": [
          "string"
        ]
      }
    ],
    "issue_severity": "string",
    "labels": "string",
    "milestone": 0,
    "repo": "string",
    "security_hole": "string",
    "state": "string",
    "status": "string",
    "title": "string"
  },
  "method": "patch",
  "operationId": "patch_api_v5_repos_{owner}_issues_{number}",
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
      "description": "Which issue number, the ordinal number of the issue in this repository",
      "example": "",
      "in": "path",
      "name": "number",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "User authorization code",
      "example": "",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/issues/{number}",
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
    "name": "Update Issue",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "repos",
        ":owner",
        "issues",
        ":number"
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
            "content": "(Required) Which issue number, the ordinal number of the issue in this repository",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "number",
          "type": "any",
          "value": ""
        }
      ]
    }
  },
  "requestBody": {
    "content": {
      "application/json": {
        "example": "{\n    \"repo\": \"test666\",\n    \"title\": \"fsds11\",\n    \"body\": \"new body\",\n    \"state\": \"closed\",\n    \"assignee\": \"aron1\",\n    \"milestone\": \"0706\",\n    \"labels\": \"new label\",\n    // \"security_hole\": \"\",\n    \"status\": \"rejected\"\n}",
        "schema": {
          "properties": {
            "assignee": {
              "description": "Issue Owner's username, separated by English commas for multiple ones",
              "type": "string"
            },
            "body": {
              "description": "Issue Description",
              "type": "string"
            },
            "custom_fields": {
              "description": "Custom field information (Enterprise edition supported)",
              "items": {
                "properties": {
                  "field_name": {
                    "description": "Field Name",
                    "type": "string"
                  },
                  "field_values": {
                    "description": "Field value array",
                    "items": {
                      "type": "string"
                    },
                    "type": "array"
                  }
                },
                "type": "object"
              },
              "type": "array"
            },
            "issue_severity": {
              "description": "Issue Priority (Enterprise Edition Supported)",
              "type": "string"
            },
            "labels": {
              "description": "A comma-separated list of labels, where the name must be between 2-20 characters long and cannot contain special characters. For example: bug,performance",
              "type": "string"
            },
            "milestone": {
              "description": "Milestone Sequence Number",
              "type": "integer"
            },
            "repo": {
              "description": "Repository path",
              "type": "string"
            },
            "security_hole": {
              "description": "Whether it is a private issue (default is false)",
              "type": "string"
            },
            "state": {
              "description": "Issue Status, reopen (open)、close (closed)",
              "type": "string"
            },
            "status": {
              "description": "Issue Status (Enterprise Edition Supported)",
              "type": "string"
            },
            "title": {
              "description": "Issue Title",
              "type": "string"
            }
          },
          "required": [
            "repo",
            "title",
            "issue_severity"
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
            "assignee": {
              "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/fa/fe/f32a9fecc53e890afbd48fd098b0f6c5f20f062581400c76c85e5baab3f0d5b2.png",
              "events_url": null,
              "followers_url": null,
              "following_url": null,
              "gists_url": null,
              "html_url": "https://test.gitcode.net/dengmengmian",
              "id": "661ce4eab470b1430d456154",
              "login": "dengmengmian",
              "member_role": null,
              "name": "MaFan_",
              "organizations_url": null,
              "received_events_url": null,
              "remark": null,
              "repos_url": null,
              "starred_url": null,
              "subscriptions_url": null,
              "type": null,
              "url": null
            },
            "body": "abcabcabc",
            "created_at": "2024-04-16T14:38:43.464+08:00",
            "finished_at": "2024-04-16T14:49:45.166+08:00",
            "html_url": "https://test.gitcode.net/dengmengmian/test01/issues/14",
            "id": 152467,
            "labels": [
              {
                "color": "#428BCA",
                "id": 382389,
                "name": "ad"
              },
              {
                "color": "#428BCA",
                "id": 382388,
                "name": "id"
              }
            ],
            "number": 14,
            "repository": {
              "created_at": "2024-04-16T14:38:43.464+08:00",
              "description": "",
              "full_name": "dengmengmian/test01",
              "id": 152467,
              "name": "test01",
              "path": "test01",
              "updated_at": "2024-04-18T18:27:21.955+08:00"
            },
            "severity": "Major",
            "stage": "New",
            "state": "closed",
            "title": "abcabcabc",
            "updated_at": "2024-04-18T18:27:21.955+08:00",
            "user": {
              "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/fa/fe/f32a9fecc53e890afbd48fd098b0f6c5f20f062581400c76c85e5baab3f0d5b2.png",
              "events_url": null,
              "followers_url": null,
              "following_url": null,
              "gists_url": null,
              "html_url": "https://test.gitcode.net/dengmengmian",
              "id": "661ce4eab470b1430d456154",
              "login": "dengmengmian",
              "member_role": null,
              "name": "MaFan_",
              "organizations_url": null,
              "received_events_url": null,
              "remark": null,
              "repos_url": null,
              "starred_url": null,
              "subscriptions_url": null,
              "type": null,
              "url": null
            }
          },
          "schema": {
            "properties": {
              "assignee": {
                "properties": {
                  "avatar_url": {
                    "type": "string"
                  },
                  "events_url": {
                    "type": "null"
                  },
                  "followers_url": {
                    "type": "null"
                  },
                  "following_url": {
                    "type": "null"
                  },
                  "gists_url": {
                    "type": "null"
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
                  "member_role": {
                    "type": "null"
                  },
                  "name": {
                    "type": "string"
                  },
                  "organizations_url": {
                    "type": "null"
                  },
                  "received_events_url": {
                    "type": "null"
                  },
                  "remark": {
                    "type": "null"
                  },
                  "repos_url": {
                    "type": "null"
                  },
                  "starred_url": {
                    "type": "null"
                  },
                  "subscriptions_url": {
                    "type": "null"
                  },
                  "type": {
                    "type": "null"
                  },
                  "url": {
                    "type": "null"
                  }
                },
                "type": "object"
              },
              "body": {
                "type": "string"
              },
              "created_at": {
                "type": "string"
              },
              "custom_fields": {
                "description": "Custom field information (Enterprise edition supported)",
                "items": {
                  "properties": {
                    "field_name": {
                      "description": "Custom Field Name",
                      "type": "string"
                    },
                    "field_type": {
                      "description": "Field type. text_single: single line text, text_multi: multi-line text, integer: integer, decimal: decimal, date: date, select_single: single select dropdown, select_multi: multi-select dropdown, member_single: single select member, member_multi: multi-select member",
                      "type": "string"
                    },
                    "field_values": {
                      "description": "Custom field value",
                      "items": {
                        "type": "string"
                      },
                      "type": "array"
                    },
                    "field_visibility": {
                      "description": "Visibility. 0: Visible to administrators only, 1: Visible to everyone",
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "finished_at": {
                "type": "string"
              },
              "html_url": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "labels": {
                "items": {
                  "properties": {
                    "color": {
                      "type": "string"
                    },
                    "id": {
                      "type": "integer"
                    },
                    "name": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "number": {
                "type": "integer"
              },
              "repository": {
                "properties": {
                  "created_at": {
                    "type": "string"
                  },
                  "description": {
                    "type": "string"
                  },
                  "full_name": {
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
                  "updated_at": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "severity": {
                "type": "string"
              },
              "stage": {
                "type": "string"
              },
              "state": {
                "type": "string"
              },
              "title": {
                "type": "string"
              },
              "updated_at": {
                "type": "string"
              },
              "user": {
                "properties": {
                  "avatar_url": {
                    "type": "string"
                  },
                  "events_url": {
                    "type": "null"
                  },
                  "followers_url": {
                    "type": "null"
                  },
                  "following_url": {
                    "type": "null"
                  },
                  "gists_url": {
                    "type": "null"
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
                  "member_role": {
                    "type": "null"
                  },
                  "name": {
                    "type": "string"
                  },
                  "organizations_url": {
                    "type": "null"
                  },
                  "received_events_url": {
                    "type": "null"
                  },
                  "remark": {
                    "type": "null"
                  },
                  "repos_url": {
                    "type": "null"
                  },
                  "starred_url": {
                    "type": "null"
                  },
                  "subscriptions_url": {
                    "type": "null"
                  },
                  "type": {
                    "type": "null"
                  },
                  "url": {
                    "type": "null"
                  }
                },
                "type": "object"
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
    "Issues"
  ]
}
```
