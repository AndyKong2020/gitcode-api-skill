# PR Submitted File Change Information
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls-number-files-json](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls-number-files-json)
Category: Pull Requests
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/pulls/{number}/files.json`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_pulls_{number}_files.json`
- Tags: `Pull Requests`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| number | path | true | integer | The ordinal number of the PR in this repository, i.e., which PR it is. |
| access_token | query | true | string | User authorization code |
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
    "added_lines": {
      "type": "integer"
    },
    "code": {
      "type": "integer"
    },
    "count": {
      "type": "integer"
    },
    "diff_refs": {
      "properties": {
        "base_sha": {
          "type": "string"
        },
        "head_sha": {
          "type": "string"
        },
        "start_sha": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "diffs": {
      "items": {
        "properties": {
          "added_lines": {
            "type": "integer"
          },
          "content": {
            "properties": {
              "text": {
                "items": {
                  "properties": {
                    "line_content": {
                      "type": "string"
                    },
                    "new_line": {
                      "properties": {
                        "line_code": {
                          "type": "string"
                        },
                        "line_num": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "old_line": {
                      "properties": {
                        "line_code": {
                          "type": "string"
                        },
                        "line_num": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "type": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              }
            },
            "type": "object"
          },
          "head": {
            "properties": {
              "commit_id": {
                "type": "string"
              },
              "url": {
                "type": "string"
              }
            },
            "type": "object"
          },
          "new_blob_id": {
            "type": "string"
          },
          "remove_lines": {
            "type": "integer"
          },
          "statistic": {
            "properties": {
              "new_path": {
                "type": "string"
              },
              "old_path": {
                "type": "string"
              },
              "path": {
                "type": "string"
              },
              "type": {
                "type": "string"
              },
              "view": {
                "type": "integer"
              }
            },
            "type": "object"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "remove_lines": {
      "type": "integer"
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
      "added_lines": 7,
      "code": 0,
      "count": 2,
      "diff_refs": {
        "base_sha": "db015522f67b15e868c5f929ff1af4cba9ddd112",
        "head_sha": "93cd8303ac07886610d738baf7ddd620f04ee778",
        "start_sha": "db015522f67b15e868c5f929ff1af4cba9ddd112"
      },
      "diffs": [
        {
          "added_lines": 3,
          "content": {
            "text": [
              {
                "line_content": "111",
                "new_line": {
                  "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_1_1",
                  "line_num": ""
                },
                "old_line": {
                  "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_1_1",
                  "line_num": "1"
                },
                "type": "old"
              },
              {
                "line_content": "111222",
                "new_line": {
                  "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_2_1",
                  "line_num": "1"
                },
                "old_line": {
                  "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_2_1",
                  "line_num": ""
                },
                "type": "new"
              },
              {
                "line_content": " ",
                "new_line": {
                  "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_2_2",
                  "line_num": "2"
                },
                "old_line": {
                  "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_2_2",
                  "line_num": "2"
                }
              },
              {
                "line_content": "1113",
                "new_line": {
                  "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_3_3",
                  "line_num": ""
                },
                "old_line": {
                  "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_3_3",
                  "line_num": "3"
                },
                "type": "old"
              },
              {
                "line_content": "1113333",
                "new_line": {
                  "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_4_3",
                  "line_num": "3"
                },
                "old_line": {
                  "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_4_3",
                  "line_num": ""
                },
                "type": "new"
              },
              {
                "line_content": " ",
                "new_line": {
                  "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_4_4",
                  "line_num": "4"
                },
                "old_line": {
                  "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_4_4",
                  "line_num": "4"
                }
              },
              {
                "line_content": "444",
                "new_line": {
                  "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_5_5",
                  "line_num": ""
                },
                "old_line": {
                  "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_5_5",
                  "line_num": "5"
                },
                "type": "old"
              },
              {
                "line_content": "4442423",
                "new_line": {
                  "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_6_5",
                  "line_num": "5"
                },
                "old_line": {
                  "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_6_5",
                  "line_num": ""
                },
                "type": "new"
              },
              {
                "line_content": " 5555",
                "new_line": {
                  "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_6_6",
                  "line_num": "6"
                },
                "old_line": {
                  "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_6_6",
                  "line_num": "6"
                }
              }
            ]
          },
          "head": {
            "commit_id": "93cd8303ac07886610d738baf7ddd620f04ee778",
            "url": "https://pre-raw.gitcode.com/xiaogang/test/raw/93cd8303ac07886610d738baf7ddd620f04ee778/1"
          },
          "new_blob_id": "b575bd06b44029dc12771503388d61ea383169cb",
          "remove_lines": 3,
          "statistic": {
            "new_path": "1",
            "old_path": "1",
            "path": "1",
            "type": "text_type",
            "view": false
          }
        },
        {
          "added_lines": 4,
          "content": {
            "text": [
              {
                "line_content": " 11111",
                "new_line": {
                  "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_1_1",
                  "line_num": "1"
                },
                "old_line": {
                  "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_1_1",
                  "line_num": "1"
                }
              },
              {
                "line_content": "22222",
                "new_line": {
                  "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_2_2",
                  "line_num": ""
                },
                "old_line": {
                  "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_2_2",
                  "line_num": "2"
                },
                "type": "old"
              },
              {
                "line_content": "22222adfsasf",
                "new_line": {
                  "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_3_2",
                  "line_num": "2"
                },
                "old_line": {
                  "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_3_2",
                  "line_num": ""
                },
                "type": "new"
              },
              {
                "line_content": " 3333",
                "new_line": {
                  "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_3_3",
                  "line_num": "3"
                },
                "old_line": {
                  "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_3_3",
                  "line_num": "3"
                }
              },
              {
                "line_content": "",
                "new_line": {
                  "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_4_4",
                  "line_num": ""
                },
                "old_line": {
                  "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_4_4",
                  "line_num": "4"
                },
                "type": "old"
              },
              {
                "line_content": "",
                "new_line": {
                  "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_5_4",
                  "line_num": ""
                },
                "old_line": {
                  "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_5_4",
                  "line_num": "5"
                },
                "type": "old"
              },
              {
                "line_content": "4444",
                "new_line": {
                  "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_6_4",
                  "line_num": ""
                },
                "old_line": {
                  "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_6_4",
                  "line_num": "6"
                },
                "type": "old"
              }
            ]
          },
          "head": {
            "commit_id": "93cd8303ac07886610d738baf7ddd620f04ee778",
            "url": "https://pre-raw.gitcode.com/xiaogang/test/raw/93cd8303ac07886610d738baf7ddd620f04ee778/2"
          },
          "new_blob_id": "1d3e5f08788ce215053e01fd54a76c6c6fbc1ddc",
          "remove_lines": 4,
          "statistic": {
            "new_path": "2",
            "old_path": "2",
            "path": "2",
            "type": "text_type",
            "view": false
          }
        }
      ],
      "remove_lines": 7
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_pulls_{number}_files.json",
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
      "description": "The ordinal number of the PR in this repository, i.e., which PR it is.",
      "example": 0,
      "in": "path",
      "name": "number",
      "required": true,
      "schema": {
        "type": "integer"
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
  "path": "/api/v5/repos/{owner}/{repo}/pulls/{number}/files.json",
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
    "name": "PR Submitted File Change Information",
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
        "pulls",
        ":number",
        "files.json"
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
        },
        {
          "description": {
            "content": "(Required) The ordinal number of the PR in this repository, i.e., which PR it is.",
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
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "examples": {
            "1": {
              "summary": "Successful Example",
              "value": {
                "added_lines": 7,
                "code": 0,
                "count": 2,
                "diff_refs": {
                  "base_sha": "db015522f67b15e868c5f929ff1af4cba9ddd112",
                  "head_sha": "93cd8303ac07886610d738baf7ddd620f04ee778",
                  "start_sha": "db015522f67b15e868c5f929ff1af4cba9ddd112"
                },
                "diffs": [
                  {
                    "added_lines": 3,
                    "content": {
                      "text": [
                        {
                          "line_content": "111",
                          "new_line": {
                            "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_1_1",
                            "line_num": ""
                          },
                          "old_line": {
                            "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_1_1",
                            "line_num": "1"
                          },
                          "type": "old"
                        },
                        {
                          "line_content": "111222",
                          "new_line": {
                            "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_2_1",
                            "line_num": "1"
                          },
                          "old_line": {
                            "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_2_1",
                            "line_num": ""
                          },
                          "type": "new"
                        },
                        {
                          "line_content": " ",
                          "new_line": {
                            "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_2_2",
                            "line_num": "2"
                          },
                          "old_line": {
                            "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_2_2",
                            "line_num": "2"
                          }
                        },
                        {
                          "line_content": "1113",
                          "new_line": {
                            "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_3_3",
                            "line_num": ""
                          },
                          "old_line": {
                            "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_3_3",
                            "line_num": "3"
                          },
                          "type": "old"
                        },
                        {
                          "line_content": "1113333",
                          "new_line": {
                            "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_4_3",
                            "line_num": "3"
                          },
                          "old_line": {
                            "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_4_3",
                            "line_num": ""
                          },
                          "type": "new"
                        },
                        {
                          "line_content": " ",
                          "new_line": {
                            "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_4_4",
                            "line_num": "4"
                          },
                          "old_line": {
                            "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_4_4",
                            "line_num": "4"
                          }
                        },
                        {
                          "line_content": "444",
                          "new_line": {
                            "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_5_5",
                            "line_num": ""
                          },
                          "old_line": {
                            "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_5_5",
                            "line_num": "5"
                          },
                          "type": "old"
                        },
                        {
                          "line_content": "4442423",
                          "new_line": {
                            "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_6_5",
                            "line_num": "5"
                          },
                          "old_line": {
                            "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_6_5",
                            "line_num": ""
                          },
                          "type": "new"
                        },
                        {
                          "line_content": " 5555",
                          "new_line": {
                            "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_6_6",
                            "line_num": "6"
                          },
                          "old_line": {
                            "line_code": "356a192b7913b04c54574d18c28d46e6395428ab_6_6",
                            "line_num": "6"
                          }
                        }
                      ]
                    },
                    "head": {
                      "commit_id": "93cd8303ac07886610d738baf7ddd620f04ee778",
                      "url": "https://pre-raw.gitcode.com/xiaogang/test/raw/93cd8303ac07886610d738baf7ddd620f04ee778/1"
                    },
                    "new_blob_id": "b575bd06b44029dc12771503388d61ea383169cb",
                    "remove_lines": 3,
                    "statistic": {
                      "new_path": "1",
                      "old_path": "1",
                      "path": "1",
                      "type": "text_type",
                      "view": false
                    }
                  },
                  {
                    "added_lines": 4,
                    "content": {
                      "text": [
                        {
                          "line_content": " 11111",
                          "new_line": {
                            "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_1_1",
                            "line_num": "1"
                          },
                          "old_line": {
                            "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_1_1",
                            "line_num": "1"
                          }
                        },
                        {
                          "line_content": "22222",
                          "new_line": {
                            "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_2_2",
                            "line_num": ""
                          },
                          "old_line": {
                            "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_2_2",
                            "line_num": "2"
                          },
                          "type": "old"
                        },
                        {
                          "line_content": "22222adfsasf",
                          "new_line": {
                            "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_3_2",
                            "line_num": "2"
                          },
                          "old_line": {
                            "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_3_2",
                            "line_num": ""
                          },
                          "type": "new"
                        },
                        {
                          "line_content": " 3333",
                          "new_line": {
                            "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_3_3",
                            "line_num": "3"
                          },
                          "old_line": {
                            "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_3_3",
                            "line_num": "3"
                          }
                        },
                        {
                          "line_content": "",
                          "new_line": {
                            "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_4_4",
                            "line_num": ""
                          },
                          "old_line": {
                            "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_4_4",
                            "line_num": "4"
                          },
                          "type": "old"
                        },
                        {
                          "line_content": "",
                          "new_line": {
                            "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_5_4",
                            "line_num": ""
                          },
                          "old_line": {
                            "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_5_4",
                            "line_num": "5"
                          },
                          "type": "old"
                        },
                        {
                          "line_content": "4444",
                          "new_line": {
                            "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_6_4",
                            "line_num": ""
                          },
                          "old_line": {
                            "line_code": "da4b9237bacccdf19c0760cab7aec4a8359010b0_6_4",
                            "line_num": "6"
                          },
                          "type": "old"
                        }
                      ]
                    },
                    "head": {
                      "commit_id": "93cd8303ac07886610d738baf7ddd620f04ee778",
                      "url": "https://pre-raw.gitcode.com/xiaogang/test/raw/93cd8303ac07886610d738baf7ddd620f04ee778/2"
                    },
                    "new_blob_id": "1d3e5f08788ce215053e01fd54a76c6c6fbc1ddc",
                    "remove_lines": 4,
                    "statistic": {
                      "new_path": "2",
                      "old_path": "2",
                      "path": "2",
                      "type": "text_type",
                      "view": false
                    }
                  }
                ],
                "remove_lines": 7
              }
            }
          },
          "schema": {
            "properties": {
              "added_lines": {
                "type": "integer"
              },
              "code": {
                "type": "integer"
              },
              "count": {
                "type": "integer"
              },
              "diff_refs": {
                "properties": {
                  "base_sha": {
                    "type": "string"
                  },
                  "head_sha": {
                    "type": "string"
                  },
                  "start_sha": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "diffs": {
                "items": {
                  "properties": {
                    "added_lines": {
                      "type": "integer"
                    },
                    "content": {
                      "properties": {
                        "text": {
                          "items": {
                            "properties": {
                              "line_content": {
                                "type": "string"
                              },
                              "new_line": {
                                "properties": {
                                  "line_code": {
                                    "type": "string"
                                  },
                                  "line_num": {
                                    "type": "string"
                                  }
                                },
                                "type": "object"
                              },
                              "old_line": {
                                "properties": {
                                  "line_code": {
                                    "type": "string"
                                  },
                                  "line_num": {
                                    "type": "string"
                                  }
                                },
                                "type": "object"
                              },
                              "type": {
                                "type": "string"
                              }
                            },
                            "type": "object"
                          },
                          "type": "array"
                        }
                      },
                      "type": "object"
                    },
                    "head": {
                      "properties": {
                        "commit_id": {
                          "type": "string"
                        },
                        "url": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "new_blob_id": {
                      "type": "string"
                    },
                    "remove_lines": {
                      "type": "integer"
                    },
                    "statistic": {
                      "properties": {
                        "new_path": {
                          "type": "string"
                        },
                        "old_path": {
                          "type": "string"
                        },
                        "path": {
                          "type": "string"
                        },
                        "type": {
                          "type": "string"
                        },
                        "view": {
                          "type": "integer"
                        }
                      },
                      "type": "object"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "remove_lines": {
                "type": "integer"
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
    "Pull Requests"
  ]
}
```
