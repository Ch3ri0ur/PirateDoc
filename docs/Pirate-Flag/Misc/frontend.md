# Frontend thoughts

TODO Redo Page or in sub Folder

Here is a assortment of random thoughts about the frontend

Limit rerender by not using state changes in higher components, triggering subsequent rerender of whole tree

<!-- how to display video [[streamingmethods]] -->

SSE events go into event queue and are dealt with in batches -> every 50ms -> no smooth update possible

on requestanimationframe to make updates smoother

antd to make styling easier, bloats the bundle size.
tailwind as alternative

perhaps interesting
https://stackoverflow.com/questions/29487978/how-to-embed-h264-video-file-in-html-webpage-using-video-tags/29489356

synchronize video and graphs ? if possible how

perhaps what kind of player?

graphs

extension janus makes problems -> when 
janus.js defaultExtension checks in init for
```
event.data.type == 'janusGotScreen' && cache[event.data.id]
```
this test fails with type being undefined when another application sends messages that are not in the expected format.
This test is more stable and does not error if a unknown message is received.
```
event.data?.type && event.data.type == 'janusGotScreen' && cache[event.data.id]
```
in line 72 and 84 of janus.js


uplot has a problem in 1.2.1 when no y-scale and no initial values for the data is used. something about wsc.range not defined. Initialize with a value and it works
solved in 1.2.2

