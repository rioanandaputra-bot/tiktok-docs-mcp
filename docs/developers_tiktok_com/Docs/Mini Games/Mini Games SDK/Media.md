Docs
# Media
## Audio
The Media Audio APIs provide the tools to create and manage audio playback. Use`InnerAudioContext`for straightforward audio playback controls, and`WebAudioContext`for advanced audio processing, synthesis, and analysis.
## .createInnerAudioContext
Creates an`InnerAudioContext`instance for basic audio playback.
### Return Value

| Object | Description |
| --- | --- |
| InnerAudioContext | An`InnerAudioContext`object instance. |

### Example
```

      const innerAudioContext = tt.createInnerAudioContext();
```
## .createWebAudioContext
Creates a`WebAudioContext`instance for advanced audio processing.
### Return Value

| Object | Description |
| --- | --- |
| WebAudioContext | A`WebAudioContext`object instance. |

### Example
```

      const webAudioContext = tt.createWebAudioContext();
```
## InnerAudioContext
### .destroy
Destroys the current audio instance, releasing its resources.
### Listeners
#### .onCanplay(listener)
Listens for the event when the audio enters a playable state.
#### .offCanplay(listener)
Removes the event listener.
```
const listener = function (res) { console.log(res) }

InnerAudioContext.onCanplay(listener)
InnerAudioContext.offCanplay(listener) // The same function object used for listening must be passed in.
```
#### .onEnded(listener)
Listens for the event when playback completes naturally.
#### .offEnded(listener)
Removes the event listener.
```
const listener = function (res) { console.log(res) }

InnerAudioContext.onEnded(listener)
InnerAudioContext.offEnded(listener) // The same function object used for listening must be passed in.
```
#### .onError(listener)
Listens for playback errors. The listener receives an object response with `errMsg(string)` and `errorCode(number)`.

| Attribute | Type |
| --- | --- |
| errMsg | string |
| errorCode | number |

#### .offError(listener)
Removes the event listener.
```
const listener = function (res) { console.log(res) }

InnerAudioContext.onError(listener)
InnerAudioContext.offError(listener) // The same function object used for listening must be passed in.
```
#### .onPause(listener)
Listens for the audio pause event.
#### .offPause(listener)
Removes the event listener.
```
const listener = function (res) { console.log(res) }

InnerAudioContext.onPause(listener)
InnerAudioContext.offPause(listener) // The same function object used for listening must be passed in.
```
#### .onPlay(listener)
Listens for the audio playback event.
#### .offPlay(listener)
Removes the event listener.
```
const listener = function (res) { console.log(res) }

InnerAudioContext.onPlay(listener)
InnerAudioContext.offPlay(listener) // The same function object used for listening must be passed in.
```
#### .onSeeked(listener)
Listens for the completion of a seek operation.
#### .offSeeked(listener)
Removes the event listener.
```
const listener = function (res) { console.log(res) }

InnerAudioContext.onSeeked(listener)
InnerAudioContext.offSeeked(listener) // The same function object used for listening must be passed in.
```
#### .onSeeking(listener)
Listens for when a seek operation begins.
#### .offSeeking(listener)
Removes the event listener.
```
const listener = function (res) { console.log(res) }

InnerAudioContext.onSeeking(listener)
InnerAudioContext.offSeeking(listener) // The same function object used for listening must be passed in.
```
#### .onStop(listener)
Listens for the audio stop event.
#### .offStop(listener)
Removes the event listener.
```
const listener = function (res) { console.log(res) }

InnerAudioContext.onStop(listener)
InnerAudioContext.offStop(listener) // The same function object used for listening must be passed in.
```
#### .onTimeUpdate(listener)
Listens for playback progress updates.
#### .offTimeUpdate(listener)
Removes the event listener.
```
const listener = function (res) { console.log(res) }

InnerAudioContext.onTimeUpdate(listener)
InnerAudioContext.offTimeUpdate(listener) // The same function object used for listening must be passed in.
```
#### .onWaiting(listener)
Listens for when playback pauses due to data buffering.
#### .offWaiting(listener)
Removes the event listener.
```
const listener = function (res) { console.log(res) }

InnerAudioContext.onWaiting(listener)
InnerAudioContext.offWaiting(listener) // The same function object used for listening must be passed in.
```
### Controls
#### .pause
Pauses audio playback.
#### .play
Starts or resumes audio playback.
#### .seek
Jumps to a specified time position in the audio.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| position | number | The time to jump to, in seconds. |

#### .stop
Stops audio playback. When played again, it will start from the beginning.
## WebAudioContext
### .close
Closes the WebAudio context and releases associated resources.
#### Return Value
`Promise`
**Note:** Synchronously close the corresponding WebAudio context. After closing, the resources of the current context will be immediately released.  Do not access the state property again after closing.
#### Example
```
const audioCtx = TTMinis.game.createWebAudioContext()
audioCtx.close().then(() => {
  console.log(audioCtx.state) // Error: state should not be accessed after close
})
```
### Node Creation
#### .createAnalyser()
Creates an AnalyserNodefor audio time and frequency analysis.
```
const audioCtx = TTMinis.game.createWebAudioContext();
const analyser = audioCtx.createAnalyser();
analyser.fftSize = 2048;
const bufferLength = analyser.fftSize;
const dataArray = new Uint8Array(bufferLength);
analyser.getByteTimeDomainData(dataArray);
```
#### .createBiquadFilter()
Creates a BiquadFilterNode for filtering.
#### .createBuffer(...)
Creates an empty AudioBuffer.
##### Parameters
- numOfChannels: (number) An integer that defines the number of audio channels contained in the buffer
- length: (number) represents an integer indicating the number of sample frames in the buffer
- sampleRate: (number)** **Sampling rate of linear audio samples, i.e., the number of keyframes contained in each second
##### Return Value
- AudioBuffer: Buffer returns an AudioBuffer instance
##### Example
```
const audioCtx = TTMinis.game.createWebAudioContext()
const channels = 2, frameCount = audioCtx.sampleRate * 2.0
const myArrayBuffer = audioCtx.createBuffer(channels, frameCount, audioCtx.sampleRate)
```
#### .createBufferSource()
Creates a BufferSourceNodeto play audio data from an AudioBuffer.
##### Return Value
BufferSourceNode
##### Example
```
const audioCtx = TTMinis.game.createWebAudioContext() 
const
```
#### .createChannelMerger(inputs)
Creates a ChannelMergerNode to combine channels.
##### Parameter
- numberOfInputs: (number) Number of Input Streams to be retained in the Output Stream
##### Return Value
- ChannelMergerNode
#### .createChannelSplitter(outputs)
Creates a ChannelSplitterNode to separate channels.
##### Parameter
- numberOfOutputs: (number) Number of channels in the input audio stream to be output separately
##### Return Value
- ChannelSplitterNode
#### .createDelay(maxDelayTime):
Creates a DelayNode.
##### Parameter
- maxDelayTime: (number) Maximum Delay Time
##### Return Value
- DelayNode
**Example**
```
let audioCtx = TTMinis.game.createWebAudioContext()
const delayNode = audioCtx.createDelay(5)
```
#### .createDynamicsCompressor()
Creates a DynamicsCompressorNode for audio compression.
##### Return Value
- DynamicsCompressorNode
##### Example
```
let audioCtx = TTMinis.game.createWebAudioContext()
let compressor = audioCtx.createDynamicsCompressor()

compressor.threshold.value = -50
compressor.knee.value = 40
compressor.ratio.value = 12
compressor.attack.value = 0
compressor.release.value = 0.25
```
#### .createGain()
Creates a GainNode to control volume.
##### Return Value
- GainNode
#### .createOscillator():
Creates an OscillatorNode to generate a periodic waveform.
##### Return Value
- OscillatorNode
#### .createPanner()
Creates a PannerNode for spatial audio.
##### Return Value
- PannerNode
#### .createScriptProcessor(...)
Creates a ScriptProcessorNode for custom JavaScript audio processing.
##### Parameters
- bufferSize: (number) Buffer size, in sample frames
- numberOfInputChannels:(number) is used to specify the number of channels of the input node
- numberOfOutputChannels: (number) is used to specify the number of channels of the output node
##### Return Value
- ScriptProcessorNode
##### Example
```
let audioCtx = TTMinis.game.createWebAudioContext()
const sampleSize = 4096
audioCtx.createScriptProcessor(sampleSize, 1, 1)
```
#### .createWaveShaper()
Creates a WaveShaperNode for non-linear distortion.
##### Return Value
- WaveShaperNode
### Operations
#### .decodeAudioData
Asynchronously decodes audio file data from an`ArrayBuffer`into an`AudioBuffer`.

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| audioData | ArrayBuffer | An ArrayBuffer containing the audio data. |
| successCallback | function | Callback executed on successful decoding, receives the`AudioBuffer`. |
| errorCallback | function | Callback executed on decoding failure. |

##### Return Value
- AudioBuffer
```
TTMinis.game.request({
  url: url,
```
#### .resume
Resumes a paused WebAudio context.
##### Return Value
- Promise
#### .suspend
Synchronously pause the WebAudioContext.
- Promise
Was this document helpful?