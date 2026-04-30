Docs
# File
## .getFileSystemManager
Returns the global file system manager for local file operations.
### Return value
`FileSystemManager`
## FileSystemManager
### .readFile
Reads a local file asynchronously (text or ArrayBuffer).
#### Parameters

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| filePath | string | Path of the file to be read (local path) | Yes |
| encoding | string | Specify the character encoding for reading the file. If encoding is not passed, the binary content of the file will be read in ArrayBuffer format | No |
| position | number | Read from the specified position in the file; if not specified, read from the beginning of the file. The read range should be a left-closed, right-open interval [position, position+length). Valid range: [0, fileLength - 1]. Unit: byte | No |
| length | number | Specify the length of the file; if not specified, read until the end of the file. Valid range: [1, fileLength]. Unit: byte | No |
| success | function | Callback function for successful interface call | No |
| fail | function | Callback function for interface call failure | No |
| complete | function | Callback function for the end of interface call (executed upon both successful and failed calls) | No |

#### Successful callback
Object type:

| Field | Type | Description |
| --- | --- | --- |
| data | string | Data. Type string or ArrayBuffer |
| errMsg | string | "readFile:ok" |

#### Example
```
const fs = TTMinis.game.getFileSystemManager();

fs.readFile({
  filePath: `${TTMinis.game.env.USER_DATA_PATH}/hello.txt`,
  encoding: 'utf8',
  position: 0,
  success(res) {
    console.log(res.data)
  },
  fail(res) {
    console.error(res)
  }
})
```
### .readFileSync(string filePath, string encoding, number post, number length)
Reads a local file synchronously.
#### Parameters
- string filePath: Character encoding of the file to be read.
- string encoding: Specify the character encoding for reading the file; if encoding is not passed, the binary content of the file will be read in ArrayBuffer format.
- number postion: Read from the specified position in the file; if not specified, read from the beginning of the file.
- number length: Specify the length of the file; if not specified, read until the end of the file.
#### Return value
string | Arraybuffer data
#### Example
```
const fs = TTMinis.game.getFileSystemManager();

try {
  const res = fs.readFileSync(`${TTMinis.game.env.USER_DATA_PATH}/hello.txt`, 'utf8', 0)
  console.log(res)
} catch(e) {
  console.error(e)
}
```
### .access
Checks existence of a file or directory asynchronously.
#### Parameters

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| path | string | The file/directory path (local path) to check for existence | Yes |
| success | function | Callback function for successful interface call | No |
| fail | function | Callback function for interface call failure | No |
| complete | function | Callback function for the end of interface call (executed upon both successful and failed calls) | No |

#### Example
```
const fs = TTMinis.game.getFileSystemManager();
// Check if a file/directory exists
fs.access({
  path: `${TTMinis.game.env.USER_DATA_PATH}/hello.txt`,
  success(res) {
    // File exists
    console.log(res)
  },
  fail(res) {
    // File does not exist or another error occurred
    console.error(res)
  }
})
```
### .accessSync
Checks existence of a file or directory synchronously.
#### Parameters

| Field | Type | Description |
| --- | --- | --- |
| path | string | File/directory structure to determine existence |

#### Example
```
const fs = TTMinis.game.getFileSystemManager();
// Check if a file/directory exists
fs.access({
  path: `${TTMinis.game.env.USER_DATA_PATH}/hello.txt`,
  success(res) {
    // File exists
    console.log(res)
  },
  fail(res) {
    // File does not exist or another error occurred
    console.error(res)
  }
})
```
### .writeFile
Writes text or binary data to a local file asynchronously.
#### Parameters

| **Attribute** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- |
| filePath | string | Yes | File path to write (local path) |
| data | string/ArrayBuffer | Yes | Text or binary data to be written |
| encoding | string | No | Specify the character encoding of the file to be written, default value is utf8 |
| success | function | No | Callback function for successful interface call |
| fail | function | No | Callback function for interface call failure |
| complete | function | No | Callback function for the end of interface call (executed upon both successful and failed calls) |

- Sample Code
```
const fs = TTMinis.game.getFileSystemManager();

fs.writeFile({
  filePath: `${TTMinis.game.env.USER_DATA_PATH}/hello.txt`,
  data: 'some text or arrayBuffer',
  encoding: 'utf8',
  success(res) {
    console.log(res)
  },
  fail(res) {
    console.error(res)
  }
})
```
### .writeFileSync
Writes data to a local file synchronously.
#### Parameters

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| filePath | string | File path to write (local path) |
| data | string/ArrayBuffer | Text or binary data to be written |
| encoding | string | Specify the character encoding of the file to be written |

#### Example
```
const fs = TTMinis.game.getFileSystemManager();

try {
  const res = fs.writeFileSync(
    `${TTMinis.game.env.USER_DATA_PATH}/hello.txt`,
    'some text or arrayBuffer',
    'utf8'
  )
  console.log(res)
} catch(e) {
  console.error(e)
}
```
### .mkdir
Creates a directory, optionally recursively, asynchronously.
#### Parameters

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| dirPath | string | Created directory path (local path) | Yes |
| recursive | boolean | Whether to create this directory after recursively creating its parent directories. If the corresponding parent directory already exists, it will not be created. For example, if dirPath is a/b/c/d and recursive is true, directory a will be created first, then directory b will be created under a, and so on until directory d under a/b/c is created. Default value is false. | No |
| success | function | Callback function for successful interface call | No |
| fail | function | Callback function for interface call failure | No |
| complete | function | Callback function for the end of interface call (executed upon both successful and failed calls) | No |

#### Example
```
const fs = TTMinis.game.getFileSystemManager();

fs.mkdir({
  dirPath: `${TTMinis.game.env.USER_DATA_PATH}/example`,
  recursive: false,
  success(res) {
    console.log(res)
  },
  fail(res) {
    console.error(res)
  }
})
```
### .mkdirSync
Creates a directory synchronously.
#### Parameter

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| dirPath | string | Created directory path (local path) |

#### Example
```
const fs = TTMinis.game.getFileSystemManager()

fs.mkdir({
  dirPath: `${TTMinis.game.env.USER_DATA_PATH}/example`,
  recursive: false,
  success(res) {
    console.log(res)
  },
  fail(res) {
    console.error(res)
  }
})
```
### .copyFile
Copies a file asynchronously.
#### Parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| srcPath | string | Source file path, supports local path | Yes |
| destPath | string | Target file path, supporting local paths | Yes |
| success | function | Callback function for successful interface call | No |
| fail | function | Callback function for interface call failure | No |
| complete | function | Callback function for the end of interface call (executed upon both successful and failed calls) | No |

- Example
```
const fs = TTMinis.game.getFileSystemManager()

fs.copyFile({
  srcPath: `${TTMinis.game.env.USER_DATA_PATH}/hello.txt`,
  destPath: `${TTMinis.game.env.USER_DATA_PATH}/hello_copy.txt`
  success(res) {
    console.log(res)
  },
  fail(res) {
    console.error(res)
  }
})
```
### .copyFileSync
Copies a file synchronously.
#### Parameters

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| srcPath | string | Source file path, supports local path |
| destPath | string | Target file path, supporting local paths |

#### Example
```
const fs = TTMinis.game.getFileSystemManager();

try {
  fs.copyFileSync(
    `${TTMinis.game.env.USER_DATA_PATH}/hello.txt`,
    `${TTMinis.game.env.USER_DATA_PATH}/hello_copy.txt`
  )
} catch(e) {
  console.error(e)
}
```
### .unzip
Unzips the file.
#### Parameters

| Field | Type | Description | Required |
| --- | --- | --- | --- |
| zipFilePath | string | Source file path, supports local paths, and can only be a zip compressed file | Yes |
| targetPath | string | Target directory path, supports local paths | Yes |
| success | function | Callback function for successful interface call | No |
| fail | function | Callback function for interface call failure | No |
| complete | function | Callback function for the end of interface call (executed upon both successful and failed calls) | No |

Was this document helpful?