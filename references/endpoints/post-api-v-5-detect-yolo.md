# Object Detection
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-detect-yolo](https://docs.gitcode.com/en/docs/apis/post-api-v-5-detect-yolo)
Category: AI hub
- Method: `POST`
- Path: `/api/v5/detect/yolo`
- Operation ID: `post-api-v-5-detect-yolo`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| Authorization | header | true | string | User Personal Token |
## Request Body
#### `application/json`
Schema:
```json
{
  "description": "",
  "properties": {
    "conf": {
      "description": "Predicted confidence threshold, valid range 0.01 - 1.0",
      "example": 0.5,
      "maximum": 1,
      "minimum": 0.01,
      "type": "number"
    },
    "imgsz": {
      "description": "The size of the input image, the valid range is 32-1280 pixels.",
      "example": 640,
      "maximum": 1280,
      "minimum": 32,
      "type": "integer"
    },
    "iou": {
      "description": "IoU threshold, valid range 0.0 - 0.95",
      "example": 0.45,
      "maximum": 0.95,
      "minimum": 0,
      "type": "number"
    },
    "model": {
      "description": "Model weight file names for yolo11 (yolo11n.pt, yolo11s.pt, yolo11m.pt, yolo11l.pt, yolo11x.pt)",
      "example": "yolo11n.pt",
      "type": "string"
    },
    "source": {
      "description": "Base64 encoded string of the image to be detected",
      "example": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQXXXXXXX",
      "type": "string"
    }
  },
  "required": [
    "model",
    "source",
    "imgsz",
    "conf",
    "iou"
  ],
  "type": "object"
}
```
Example:
```json
{
  "conf": 0.25,
  "imgsz": 640,
  "iou": 0.45,
  "model": "yolo11n.pt",
  "source": "data:image/jpeg;base64,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"
}
```
## Responses
### `200`
Headers:
```json
{}
```
#### `application/json`
Schema:
```json
{
  "properties": {
    "images": {
      "description": "List of detection result images",
      "items": {
        "description": "com.gitcode.aihub.inference.entity.dto.ObjectDetectionResp.ImageResult",
        "properties": {
          "results": {
            "description": "Test Result List",
            "items": {
              "description": "com.gitcode.aihub.inference.entity.dto.ObjectDetectionResp.DetectionResult",
              "properties": {
                "box": {
                  "description": "Bounding Box Coordinates",
                  "properties": {
                    "x1": {
                      "description": "Top-left x coordinate",
                      "example": 14.55554,
                      "type": "number"
                    },
                    "x2": {
                      "description": "Lower right x coordinate",
                      "example": 72.45978,
                      "type": "number"
                    },
                    "y1": {
                      "description": "Top-left y coordinate",
                      "example": 116.72369,
                      "type": "number"
                    },
                    "y2": {
                      "description": "Lower right y-coordinate",
                      "example": 268.92963,
                      "type": "number"
                    }
                  },
                  "required": [
                    "x1",
                    "x2",
                    "y1",
                    "y2"
                  ],
                  "type": "object"
                },
                "class": {
                  "description": "Category ID",
                  "example": 0,
                  "type": "integer"
                },
                "confidence": {
                  "description": "Confidence Level",
                  "example": 0.83583,
                  "type": "number"
                },
                "name": {
                  "description": "Category Name",
                  "example": "person",
                  "type": "string"
                }
              },
              "required": [
                "box",
                "confidence",
                "name"
              ],
              "type": "object"
            },
            "type": "array"
          },
          "shape": {
            "description": "Image size [width, height]",
            "items": {
              "type": "integer"
            },
            "type": "array"
          },
          "speed": {
            "description": "Processing speed information",
            "properties": {
              "inference": {
                "description": "Inference Time (ms)",
                "example": 56.13449,
                "type": "number"
              },
              "postprocess": {
                "description": "Post-processing Time (ms)",
                "example": 0.05426,
                "type": "number"
              },
              "preprocess": {
                "description": "Preprocessing Time (ms)",
                "example": 21.20275,
                "type": "number"
              }
            },
            "required": [
              "inference",
              "postprocess",
              "preprocess"
            ],
            "type": "object"
          }
        },
        "required": [
          "results",
          "shape",
          "speed"
        ],
        "type": "object"
      },
      "type": "array"
    },
    "metadata": {
      "description": "Metadata Information",
      "properties": {
        "functionTimeAlive": {
          "description": "Function Survival Time (ms)",
          "example": 163779.863,
          "type": "number"
        },
        "functionTimeCall": {
          "description": "Function call time (ms)",
          "example": 0.57,
          "type": "number"
        },
        "imageCount": {
          "description": "Number of images",
          "example": 1,
          "type": "integer"
        },
        "model": {
          "description": "Model Name",
          "example": "yolo11n-cls.pt",
          "type": "string"
        },
        "version": {
          "description": "Version Information",
          "properties": {
            "python": {
              "description": "Python version",
              "example": "3.11.14",
              "type": "string"
            },
            "torch": {
              "description": "PyTorch Version",
              "example": "2.9.1+cpu",
              "type": "string"
            },
            "torchvision": {
              "description": "版本",
              "example": "0.24.1+cpu",
              "type": "string"
            },
            "ultralytics": {
              "description": "ultralytics version",
              "example": "8.3.228",
              "type": "string"
            }
          },
          "required": [
            "python",
            "ultralytics"
          ],
          "type": "object"
        }
      },
      "required": [
        "version"
      ],
      "type": "object"
    }
  },
  "required": [
    "images",
    "metadata"
  ],
  "type": "object"
}
```
Example:
```json
{
  "images": [
    {
      "results": [
        {
          "box": {
            "x1": 1.511962890625,
            "x2": 263.31793212890625,
            "y1": 0.378143310546875,
            "y2": 200.42999267578125
          },
          "confidence": 0.6070891618728638,
          "name": "person"
        }
      ],
      "shape": [
        203,
        320
      ],
      "speed": {
        "inference": 235.26057600975037,
        "postprocess": 1.4520995318889618,
        "preprocess": 3.9573051035404205
      }
    }
  ],
  "metadata": {
    "version": {
      "python": "3.11.13",
      "ultralytics": "8.3.231"
    }
  }
}
```
## JSON Request Example
```json
{
  "conf": 0.5,
  "imgsz": 640,
  "iou": 0.45,
  "model": "yolo11n.pt",
  "source": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQXXXXXXX"
}
```
## Raw OpenAPI Operation
```json
{
  "deprecated": false,
  "description": "Use YOLO model for object detection in images, identify objects in the images",
  "info": {
    "description": "",
    "title": "GicodeOpenAPI",
    "version": "1.0.0"
  },
  "jsonRequestBodyExample": {
    "conf": 0.5,
    "imgsz": 640,
    "iou": 0.45,
    "model": "yolo11n.pt",
    "source": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQXXXXXXX"
  },
  "method": "post",
  "operationId": "post-api-v-5-detect-yolo",
  "parameters": [
    {
      "description": "User Personal Token",
      "example": "",
      "in": "header",
      "name": "Authorization",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/detect/yolo",
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
      "content": "Use YOLO model for object detection in images, identify objects in the images",
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
    "name": "Object Detection",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "detect",
        "yolo"
      ],
      "query": [],
      "variable": []
    }
  },
  "requestBody": {
    "content": {
      "application/json": {
        "example": {
          "conf": 0.25,
          "imgsz": 640,
          "iou": 0.45,
          "model": "yolo11n.pt",
          "source": "data:image/jpeg;base64,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"
        },
        "schema": {
          "description": "",
          "properties": {
            "conf": {
              "description": "Predicted confidence threshold, valid range 0.01 - 1.0",
              "example": 0.5,
              "maximum": 1,
              "minimum": 0.01,
              "type": "number"
            },
            "imgsz": {
              "description": "The size of the input image, the valid range is 32-1280 pixels.",
              "example": 640,
              "maximum": 1280,
              "minimum": 32,
              "type": "integer"
            },
            "iou": {
              "description": "IoU threshold, valid range 0.0 - 0.95",
              "example": 0.45,
              "maximum": 0.95,
              "minimum": 0,
              "type": "number"
            },
            "model": {
              "description": "Model weight file names for yolo11 (yolo11n.pt, yolo11s.pt, yolo11m.pt, yolo11l.pt, yolo11x.pt)",
              "example": "yolo11n.pt",
              "type": "string"
            },
            "source": {
              "description": "Base64 encoded string of the image to be detected",
              "example": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQXXXXXXX",
              "type": "string"
            }
          },
          "required": [
            "model",
            "source",
            "imgsz",
            "conf",
            "iou"
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
            "images": [
              {
                "results": [
                  {
                    "box": {
                      "x1": 1.511962890625,
                      "x2": 263.31793212890625,
                      "y1": 0.378143310546875,
                      "y2": 200.42999267578125
                    },
                    "confidence": 0.6070891618728638,
                    "name": "person"
                  }
                ],
                "shape": [
                  203,
                  320
                ],
                "speed": {
                  "inference": 235.26057600975037,
                  "postprocess": 1.4520995318889618,
                  "preprocess": 3.9573051035404205
                }
              }
            ],
            "metadata": {
              "version": {
                "python": "3.11.13",
                "ultralytics": "8.3.231"
              }
            }
          },
          "schema": {
            "properties": {
              "images": {
                "description": "List of detection result images",
                "items": {
                  "description": "com.gitcode.aihub.inference.entity.dto.ObjectDetectionResp.ImageResult",
                  "properties": {
                    "results": {
                      "description": "Test Result List",
                      "items": {
                        "description": "com.gitcode.aihub.inference.entity.dto.ObjectDetectionResp.DetectionResult",
                        "properties": {
                          "box": {
                            "description": "Bounding Box Coordinates",
                            "properties": {
                              "x1": {
                                "description": "Top-left x coordinate",
                                "example": 14.55554,
                                "type": "number"
                              },
                              "x2": {
                                "description": "Lower right x coordinate",
                                "example": 72.45978,
                                "type": "number"
                              },
                              "y1": {
                                "description": "Top-left y coordinate",
                                "example": 116.72369,
                                "type": "number"
                              },
                              "y2": {
                                "description": "Lower right y-coordinate",
                                "example": 268.92963,
                                "type": "number"
                              }
                            },
                            "required": [
                              "x1",
                              "x2",
                              "y1",
                              "y2"
                            ],
                            "type": "object"
                          },
                          "class": {
                            "description": "Category ID",
                            "example": 0,
                            "type": "integer"
                          },
                          "confidence": {
                            "description": "Confidence Level",
                            "example": 0.83583,
                            "type": "number"
                          },
                          "name": {
                            "description": "Category Name",
                            "example": "person",
                            "type": "string"
                          }
                        },
                        "required": [
                          "box",
                          "confidence",
                          "name"
                        ],
                        "type": "object"
                      },
                      "type": "array"
                    },
                    "shape": {
                      "description": "Image size [width, height]",
                      "items": {
                        "type": "integer"
                      },
                      "type": "array"
                    },
                    "speed": {
                      "description": "Processing speed information",
                      "properties": {
                        "inference": {
                          "description": "Inference Time (ms)",
                          "example": 56.13449,
                          "type": "number"
                        },
                        "postprocess": {
                          "description": "Post-processing Time (ms)",
                          "example": 0.05426,
                          "type": "number"
                        },
                        "preprocess": {
                          "description": "Preprocessing Time (ms)",
                          "example": 21.20275,
                          "type": "number"
                        }
                      },
                      "required": [
                        "inference",
                        "postprocess",
                        "preprocess"
                      ],
                      "type": "object"
                    }
                  },
                  "required": [
                    "results",
                    "shape",
                    "speed"
                  ],
                  "type": "object"
                },
                "type": "array"
              },
              "metadata": {
                "description": "Metadata Information",
                "properties": {
                  "functionTimeAlive": {
                    "description": "Function Survival Time (ms)",
                    "example": 163779.863,
                    "type": "number"
                  },
                  "functionTimeCall": {
                    "description": "Function call time (ms)",
                    "example": 0.57,
                    "type": "number"
                  },
                  "imageCount": {
                    "description": "Number of images",
                    "example": 1,
                    "type": "integer"
                  },
                  "model": {
                    "description": "Model Name",
                    "example": "yolo11n-cls.pt",
                    "type": "string"
                  },
                  "version": {
                    "description": "Version Information",
                    "properties": {
                      "python": {
                        "description": "Python version",
                        "example": "3.11.14",
                        "type": "string"
                      },
                      "torch": {
                        "description": "PyTorch Version",
                        "example": "2.9.1+cpu",
                        "type": "string"
                      },
                      "torchvision": {
                        "description": "版本",
                        "example": "0.24.1+cpu",
                        "type": "string"
                      },
                      "ultralytics": {
                        "description": "ultralytics version",
                        "example": "8.3.228",
                        "type": "string"
                      }
                    },
                    "required": [
                      "python",
                      "ultralytics"
                    ],
                    "type": "object"
                  }
                },
                "required": [
                  "version"
                ],
                "type": "object"
              }
            },
            "required": [
              "images",
              "metadata"
            ],
            "type": "object"
          }
        }
      },
      "description": "",
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
  "tags": []
}
```
