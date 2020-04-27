# YouTube embed image overlay

A tool to add more visual cue when embedding YouTube videos in GitHub.


## Example

The method I used before to embed YouTube videos inside my repos was from [here](https://stackoverflow.com/questions/11804820/how-can-i-embed-a-youtube-video-on-github-wiki-pages)


For example, If I want to embed [this video](https://www.youtube.com/watch?v=3BYNj6Yvl8I) I'd use:

```
[![](http://img.youtube.com/vi/3BYNj6Yvl8I/0.jpg)](http://www.youtube.com/watch?v=3BYNj6Yvl8I "Video Title")

```

Here's how it'd look:

[![](http://img.youtube.com/vi/3BYNj6Yvl8I/0.jpg)](http://www.youtube.com/watch?v=3BYNj6Yvl8I "Video Title")

The answer above suggest that we take screen shot and embed it to make it easir to reason that the above is a video and not an image.

This tool will automate this process and add visial cues similar to an embeded youtube video.

Here's how it'd look:

[![](https://yt-embed.herokuapp.com/embed?v=3BYNj6Yvl8I)](http://www.youtube.com/watch?v=3BYNj6Yvl8I "Video Title")


```
[![](https://yt-embed.herokuapp.com/embed?v=3BYNj6Yvl8I)](http://www.youtube.com/watch?v=3BYNj6Yvl8I "Video Title")
```

