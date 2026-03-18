# Commits Comparison
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-compare-base-head](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-compare-base-head)
Category: Commit
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/compare/{base}...{head}`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_compare_{base}_{head}`
- Tags: `Commit`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| base | path | true | string | The starting point for comparison. Commit SHA, branch name, or tag name. |
| head | path | true | string | The end point for comparison. Can be a commit SHA, branch name, or tag name. |
| access_token | query | true | string | User authorization code |
| straight | query | false | boolean | Whether to perform a direct comparison. Defaults to false. |
| suffix | query | false | string | Filter files by file extension, such as `.txt`. Affects only `files`. |
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
    "base_commit": {
      "properties": {
        "author": {
          "properties": {
            "id": {
              "type": "integer"
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
        "comments_url": {
          "type": "string"
        },
        "commit": {
          "properties": {
            "author": {
              "properties": {
                "date": {
                  "type": "string"
                },
                "email": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                }
              },
              "type": "object"
            },
            "committer": {
              "properties": {
                "date": {
                  "type": "string"
                },
                "email": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                }
              },
              "type": "object"
            },
            "message": {
              "type": "string"
            },
            "tree": {
              "properties": {
                "sha": {
                  "type": "string"
                },
                "url": {
                  "type": "string"
                }
              },
              "type": "object"
            }
          },
          "type": "object"
        },
        "committer": {
          "properties": {
            "id": {
              "type": "integer"
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
        "html_url": {
          "type": "string"
        },
        "parents": {
          "items": {
            "properties": {
              "sha": {
                "type": "string"
              },
              "url": {
                "type": "string"
              }
            },
            "type": "object"
          },
          "type": "array"
        },
        "sha": {
          "type": "string"
        },
        "url": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "commits": {
      "items": {
        "properties": {
          "author": {
            "properties": {
              "id": {
                "type": "integer"
              },
              "login": {
                "type": "string"
              },
              "name": {
                "type": "string"
              }
            },
            "type": "object"
          },
          "commit": {
            "properties": {
              "author": {
                "properties": {
                  "date": {
                    "type": "string"
                  },
                  "email": {
                    "type": "string"
                  },
                  "name": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "committer": {
                "properties": {
                  "date": {
                    "type": "string"
                  },
                  "email": {
                    "type": "string"
                  },
                  "name": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "message": {
                "type": "string"
              }
            },
            "type": "object"
          },
          "committer": {
            "properties": {
              "id": {
                "type": "integer"
              },
              "login": {
                "type": "string"
              },
              "name": {
                "type": "string"
              }
            },
            "type": "object"
          },
          "sha": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "files": {
      "items": {
        "properties": {
          "additions": {
            "type": "integer"
          },
          "blob_url": {
            "type": "string"
          },
          "changes": {
            "type": "integer"
          },
          "deletions": {
            "type": "integer"
          },
          "filename": {
            "type": "string"
          },
          "patch": {
            "type": "string"
          },
          "raw_url": {
            "type": "string"
          },
          "sha": {
            "type": "string"
          },
          "status": {
            "type": "string"
          },
          "truncated": {
            "type": "integer"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "merge_base_commit": {
      "properties": {
        "author": {
          "properties": {
            "id": {
              "type": "integer"
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
        "comments_url": {
          "type": "string"
        },
        "commit": {
          "properties": {
            "author": {
              "properties": {
                "date": {
                  "type": "string"
                },
                "email": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                }
              },
              "type": "object"
            },
            "committer": {
              "properties": {
                "date": {
                  "type": "string"
                },
                "email": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                }
              },
              "type": "object"
            },
            "message": {
              "type": "string"
            },
            "tree": {
              "properties": {
                "sha": {
                  "type": "string"
                },
                "url": {
                  "type": "string"
                }
              },
              "type": "object"
            }
          },
          "type": "object"
        },
        "committer": {
          "properties": {
            "id": {
              "type": "integer"
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
        "html_url": {
          "type": "string"
        },
        "parents": {
          "items": {
            "properties": {
              "sha": {
                "type": "string"
              },
              "url": {
                "type": "string"
              }
            },
            "type": "object"
          },
          "type": "array"
        },
        "sha": {
          "type": "string"
        },
        "url": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "truncated": {
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
      "base_commit": {
        "author": {
          "id": 953,
          "login": "malongge5",
          "name": "malongge5",
          "type": "User"
        },
        "comments_url": "https://test.gitcode.net/api/v5/repos/owner-test/secure-issue/commits/17922544024484084e2b6218eb0d46d76f354ffa/comments",
        "commit": {
          "author": {
            "date": "2024-08-13T11:34:35Z",
            "email": "malongge5@noreply.gitcode.com",
            "name": "malongge5"
          },
          "committer": {
            "date": "2024-08-13T11:34:35Z",
            "email": "malongge5@noreply.gitcode.com",
            "name": "malongge5"
          },
          "message": "new: Added file test.py",
          "tree": {
            "sha": "4e12f62b7fe2f78cb7c1b088e8f7e797a8c898a3",
            "url": "https://api.gitcode.com/repos/owner-test/secure-issue/git/trees/4e12f62b7fe2f78cb7c1b088e8f7e797a8c898a3"
          }
        },
        "committer": {
          "id": 953,
          "login": "malongge5",
          "name": "malongge5",
          "type": "User"
        },
        "html_url": "https://test.gitcode.net/owner-test/secure-issue/commit/17922544024484084e2b6218eb0d46d76f354ffa",
        "parents": [
          {
            "sha": "7ea40eef5f96c3f263f17438b294a6ea9b771cc5",
            "url": "https://api.gitcode.com/api/v5/repos/owner-test/secure-issue/commits/7ea40eef5f96c3f263f17438b294a6ea9b771cc5"
          }
        ],
        "sha": "17922544024484084e2b6218eb0d46d76f354ffa",
        "url": "https://api.gitcode.com/api/v5/repos/owner-test/secure-issue/commits/17922544024484084e2b6218eb0d46d76f354ffa"
      },
      "commits": [
        {
          "author": {
            "id": 953,
            "login": "malongge5",
            "name": "malongge5"
          },
          "commit": {
            "author": {
              "date": "2024-09-09T07:29:23Z",
              "email": "malongge5@noreply.gitcode.com",
              "name": "malongge5"
            },
            "committer": {
              "date": "2024-09-09T07:29:23Z",
              "email": "malongge5@noreply.gitcode.com",
              "name": "malongge5"
            },
            "message": "new: Added file bbb.rs"
          },
          "committer": {
            "id": 953,
            "login": "malongge5",
            "name": "malongge5"
          },
          "sha": "97fd5a05e18bcd5b633a279fd7d395784d272321"
        }
      ],
      "files": [
        {
          "additions": 3,
          "blob_url": "https://test.gitcode.net/owner-test/secure-issue/blob/6533e5c4585eb91faa9331b8de6b22f9ff31d387/bbb.rs",
          "changes": 3,
          "deletions": 0,
          "filename": "bbb.rs",
          "patch": "@@ -0,0 +1,3 @@\n+\n+\n+println!(\"hello\")\n\\ No newline at end of file\n",
          "raw_url": "https://test.gitcode.net/owner-test/secure-issue/raw/6533e5c4585eb91faa9331b8de6b22f9ff31d387/bbb.rs",
          "sha": "6533e5c4585eb91faa9331b8de6b22f9ff31d387",
          "status": "added",
          "truncated": false
        }
      ],
      "merge_base_commit": {
        "author": {
          "id": 953,
          "login": "malongge5",
          "name": "malongge5",
          "type": "User"
        },
        "comments_url": "https://test.gitcode.net/api/v5/repos/owner-test/secure-issue/commits/17922544024484084e2b6218eb0d46d76f354ffa/comments",
        "commit": {
          "author": {
            "date": "2024-08-13T11:34:35Z",
            "email": "malongge5@noreply.gitcode.com",
            "name": "malongge5"
          },
          "committer": {
            "date": "2024-08-13T11:34:35Z",
            "email": "malongge5@noreply.gitcode.com",
            "name": "malongge5"
          },
          "message": "new: Added file test.py",
          "tree": {
            "sha": "4e12f62b7fe2f78cb7c1b088e8f7e797a8c898a3",
            "url": "https://api.gitcode.com/repos/owner-test/secure-issue/git/trees/4e12f62b7fe2f78cb7c1b088e8f7e797a8c898a3"
          }
        },
        "committer": {
          "id": 953,
          "login": "malongge5",
          "name": "malongge5",
          "type": "User"
        },
        "html_url": "https://test.gitcode.net/owner-test/secure-issue/commit/17922544024484084e2b6218eb0d46d76f354ffa",
        "parents": [
          {
            "sha": "7ea40eef5f96c3f263f17438b294a6ea9b771cc5",
            "url": "https://api.gitcode.com/api/v5/repos/owner-test/secure-issue/commits/7ea40eef5f96c3f263f17438b294a6ea9b771cc5"
          }
        ],
        "sha": "17922544024484084e2b6218eb0d46d76f354ffa",
        "url": "https://api.gitcode.com/api/v5/repos/owner-test/secure-issue/commits/17922544024484084e2b6218eb0d46d76f354ffa"
      },
      "truncated": false
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_compare_{base}_{head}",
  "parameters": [
    {
      "description": "Repository space address (address path of the enterprise, organization, or individual)",
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
      "description": "The starting point for comparison. Commit SHA, branch name, or tag name.",
      "example": "",
      "in": "path",
      "name": "base",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "The end point for comparison. Can be a commit SHA, branch name, or tag name.",
      "example": "",
      "in": "path",
      "name": "head",
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
      "description": "Whether to perform a direct comparison. Defaults to false.",
      "in": "query",
      "name": "straight",
      "required": false,
      "schema": {
        "type": "boolean"
      }
    },
    {
      "description": "Filter files by file extension, such as `.txt`. Affects only `files`.",
      "in": "query",
      "name": "suffix",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/compare/{base}...{head}",
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "examples": {
            "1": {
              "summary": "Successful Example",
              "value": {
                "base_commit": {
                  "author": {
                    "id": 953,
                    "login": "malongge5",
                    "name": "malongge5",
                    "type": "User"
                  },
                  "comments_url": "https://test.gitcode.net/api/v5/repos/owner-test/secure-issue/commits/17922544024484084e2b6218eb0d46d76f354ffa/comments",
                  "commit": {
                    "author": {
                      "date": "2024-08-13T11:34:35Z",
                      "email": "malongge5@noreply.gitcode.com",
                      "name": "malongge5"
                    },
                    "committer": {
                      "date": "2024-08-13T11:34:35Z",
                      "email": "malongge5@noreply.gitcode.com",
                      "name": "malongge5"
                    },
                    "message": "new: Added file test.py",
                    "tree": {
                      "sha": "4e12f62b7fe2f78cb7c1b088e8f7e797a8c898a3",
                      "url": "https://api.gitcode.com/repos/owner-test/secure-issue/git/trees/4e12f62b7fe2f78cb7c1b088e8f7e797a8c898a3"
                    }
                  },
                  "committer": {
                    "id": 953,
                    "login": "malongge5",
                    "name": "malongge5",
                    "type": "User"
                  },
                  "html_url": "https://test.gitcode.net/owner-test/secure-issue/commit/17922544024484084e2b6218eb0d46d76f354ffa",
                  "parents": [
                    {
                      "sha": "7ea40eef5f96c3f263f17438b294a6ea9b771cc5",
                      "url": "https://api.gitcode.com/api/v5/repos/owner-test/secure-issue/commits/7ea40eef5f96c3f263f17438b294a6ea9b771cc5"
                    }
                  ],
                  "sha": "17922544024484084e2b6218eb0d46d76f354ffa",
                  "url": "https://api.gitcode.com/api/v5/repos/owner-test/secure-issue/commits/17922544024484084e2b6218eb0d46d76f354ffa"
                },
                "commits": [
                  {
                    "author": {
                      "id": 953,
                      "login": "malongge5",
                      "name": "malongge5"
                    },
                    "commit": {
                      "author": {
                        "date": "2024-09-09T07:29:23Z",
                        "email": "malongge5@noreply.gitcode.com",
                        "name": "malongge5"
                      },
                      "committer": {
                        "date": "2024-09-09T07:29:23Z",
                        "email": "malongge5@noreply.gitcode.com",
                        "name": "malongge5"
                      },
                      "message": "new: Added file bbb.rs"
                    },
                    "committer": {
                      "id": 953,
                      "login": "malongge5",
                      "name": "malongge5"
                    },
                    "sha": "97fd5a05e18bcd5b633a279fd7d395784d272321"
                  }
                ],
                "files": [
                  {
                    "additions": 3,
                    "blob_url": "https://test.gitcode.net/owner-test/secure-issue/blob/6533e5c4585eb91faa9331b8de6b22f9ff31d387/bbb.rs",
                    "changes": 3,
                    "deletions": 0,
                    "filename": "bbb.rs",
                    "patch": "@@ -0,0 +1,3 @@\n+\n+\n+println!(\"hello\")\n\\ No newline at end of file\n",
                    "raw_url": "https://test.gitcode.net/owner-test/secure-issue/raw/6533e5c4585eb91faa9331b8de6b22f9ff31d387/bbb.rs",
                    "sha": "6533e5c4585eb91faa9331b8de6b22f9ff31d387",
                    "status": "added",
                    "truncated": false
                  }
                ],
                "merge_base_commit": {
                  "author": {
                    "id": 953,
                    "login": "malongge5",
                    "name": "malongge5",
                    "type": "User"
                  },
                  "comments_url": "https://test.gitcode.net/api/v5/repos/owner-test/secure-issue/commits/17922544024484084e2b6218eb0d46d76f354ffa/comments",
                  "commit": {
                    "author": {
                      "date": "2024-08-13T11:34:35Z",
                      "email": "malongge5@noreply.gitcode.com",
                      "name": "malongge5"
                    },
                    "committer": {
                      "date": "2024-08-13T11:34:35Z",
                      "email": "malongge5@noreply.gitcode.com",
                      "name": "malongge5"
                    },
                    "message": "new: Added file test.py",
                    "tree": {
                      "sha": "4e12f62b7fe2f78cb7c1b088e8f7e797a8c898a3",
                      "url": "https://api.gitcode.com/repos/owner-test/secure-issue/git/trees/4e12f62b7fe2f78cb7c1b088e8f7e797a8c898a3"
                    }
                  },
                  "committer": {
                    "id": 953,
                    "login": "malongge5",
                    "name": "malongge5",
                    "type": "User"
                  },
                  "html_url": "https://test.gitcode.net/owner-test/secure-issue/commit/17922544024484084e2b6218eb0d46d76f354ffa",
                  "parents": [
                    {
                      "sha": "7ea40eef5f96c3f263f17438b294a6ea9b771cc5",
                      "url": "https://api.gitcode.com/api/v5/repos/owner-test/secure-issue/commits/7ea40eef5f96c3f263f17438b294a6ea9b771cc5"
                    }
                  ],
                  "sha": "17922544024484084e2b6218eb0d46d76f354ffa",
                  "url": "https://api.gitcode.com/api/v5/repos/owner-test/secure-issue/commits/17922544024484084e2b6218eb0d46d76f354ffa"
                },
                "truncated": false
              }
            }
          },
          "schema": {
            "properties": {
              "base_commit": {
                "properties": {
                  "author": {
                    "properties": {
                      "id": {
                        "type": "integer"
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
                  "comments_url": {
                    "type": "string"
                  },
                  "commit": {
                    "properties": {
                      "author": {
                        "properties": {
                          "date": {
                            "type": "string"
                          },
                          "email": {
                            "type": "string"
                          },
                          "name": {
                            "type": "string"
                          }
                        },
                        "type": "object"
                      },
                      "committer": {
                        "properties": {
                          "date": {
                            "type": "string"
                          },
                          "email": {
                            "type": "string"
                          },
                          "name": {
                            "type": "string"
                          }
                        },
                        "type": "object"
                      },
                      "message": {
                        "type": "string"
                      },
                      "tree": {
                        "properties": {
                          "sha": {
                            "type": "string"
                          },
                          "url": {
                            "type": "string"
                          }
                        },
                        "type": "object"
                      }
                    },
                    "type": "object"
                  },
                  "committer": {
                    "properties": {
                      "id": {
                        "type": "integer"
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
                  "html_url": {
                    "type": "string"
                  },
                  "parents": {
                    "items": {
                      "properties": {
                        "sha": {
                          "type": "string"
                        },
                        "url": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "type": "array"
                  },
                  "sha": {
                    "type": "string"
                  },
                  "url": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "commits": {
                "items": {
                  "properties": {
                    "author": {
                      "properties": {
                        "id": {
                          "type": "integer"
                        },
                        "login": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "commit": {
                      "properties": {
                        "author": {
                          "properties": {
                            "date": {
                              "type": "string"
                            },
                            "email": {
                              "type": "string"
                            },
                            "name": {
                              "type": "string"
                            }
                          },
                          "type": "object"
                        },
                        "committer": {
                          "properties": {
                            "date": {
                              "type": "string"
                            },
                            "email": {
                              "type": "string"
                            },
                            "name": {
                              "type": "string"
                            }
                          },
                          "type": "object"
                        },
                        "message": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "committer": {
                      "properties": {
                        "id": {
                          "type": "integer"
                        },
                        "login": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "sha": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "files": {
                "items": {
                  "properties": {
                    "additions": {
                      "type": "integer"
                    },
                    "blob_url": {
                      "type": "string"
                    },
                    "changes": {
                      "type": "integer"
                    },
                    "deletions": {
                      "type": "integer"
                    },
                    "filename": {
                      "type": "string"
                    },
                    "patch": {
                      "type": "string"
                    },
                    "raw_url": {
                      "type": "string"
                    },
                    "sha": {
                      "type": "string"
                    },
                    "status": {
                      "type": "string"
                    },
                    "truncated": {
                      "type": "integer"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "merge_base_commit": {
                "properties": {
                  "author": {
                    "properties": {
                      "id": {
                        "type": "integer"
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
                  "comments_url": {
                    "type": "string"
                  },
                  "commit": {
                    "properties": {
                      "author": {
                        "properties": {
                          "date": {
                            "type": "string"
                          },
                          "email": {
                            "type": "string"
                          },
                          "name": {
                            "type": "string"
                          }
                        },
                        "type": "object"
                      },
                      "committer": {
                        "properties": {
                          "date": {
                            "type": "string"
                          },
                          "email": {
                            "type": "string"
                          },
                          "name": {
                            "type": "string"
                          }
                        },
                        "type": "object"
                      },
                      "message": {
                        "type": "string"
                      },
                      "tree": {
                        "properties": {
                          "sha": {
                            "type": "string"
                          },
                          "url": {
                            "type": "string"
                          }
                        },
                        "type": "object"
                      }
                    },
                    "type": "object"
                  },
                  "committer": {
                    "properties": {
                      "id": {
                        "type": "integer"
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
                  "html_url": {
                    "type": "string"
                  },
                  "parents": {
                    "items": {
                      "properties": {
                        "sha": {
                          "type": "string"
                        },
                        "url": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "type": "array"
                  },
                  "sha": {
                    "type": "string"
                  },
                  "url": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "truncated": {
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
    "Commit"
  ]
}
```
