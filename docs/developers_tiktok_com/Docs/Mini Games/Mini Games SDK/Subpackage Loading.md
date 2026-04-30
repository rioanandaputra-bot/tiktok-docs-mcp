Docs
# Subpackage Loading
APIs for managing the download and execution of subpackages.
Note: The difference between `TTMinis.game.preDownloadSubpackage` and `TTMinis.game.loadSubpackage`:
- `TTMinis.game.preDownloadSubpackage` only downloads the code package without automatically executing the code.
- `TTMinis.game.loadSubpackage` will automatically execute the code after downloading the code package.
## .preDownloadSubpackage(opts)
Pre‑downloads a code bundle without executing it.
### Parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| name | string | Subcontract name | Yes |
| success | function | Subpackage loading success callback event | Yes |
| fail | function | Callback event for subpackage loading failure | Yes |
| complete | function | Callback event for the end of subpackage loading (executed upon both successful and failed loading) | Yes |

### Return value
`LoadSubpackageTask`, a subpackage loading task instance, is used to obtain the subpackage loading status.
## .loadSubpackage(opts)
Downloads and loads a code bundle, executing it immediately after download.
### Parameters

| **Field** | **Type** | **Description** | **Required** |
| --- | --- | --- | --- |
| name | string | Subcontract name | Yes |
| success | function | Subpackage loading success callback event | Yes |
| fail | function | Callback event for subpackage loading failure | Yes |
| complete | function | Callback event for the end of subpackage loading (executed upon both successful and failed loading) | Yes |

### Return value
`LoadSubpackageTask`, a subpackage loading task instance, is used to obtain the subpackage loading status.
## LoadSubpackageTask(cb)
### .onProgressUpdate
Subpackage download progress callback with bytes and percent.
#### Parameters
Listens for progress updates on the subpackage download. The callback receives an object with the followign parameters:

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| progress | number | Subpackage download progress percentage |
| totalBytesWritten | number | Length of the data already downloaded, unit: Bytes |
| totalBytesExpectedToWrite | number | Expected total length of data to be downloaded, in Bytes |

## PreDownloadSubpackageTask
### .onProgressUpdate
Registers a listener for subpackage download progress changes, receiving an object with progress percentage.
#### Parameters
The listener function for the subpackage loading progress change event.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| progress | number | Subpackage download progress percentage |
| totalBytesWritten | number | Length of the data already downloaded, in bytes |
| totalBytesExpectedToWrite | number | Expected total length of data to be downloaded, in bytes |

Was this document helpful?