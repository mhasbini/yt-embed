# YouTube embed image overlay

A tool to add more visual cue when embedding YouTube videos in GitHub.

## Run app localy

- Make sure to have [nix package manager](https://nixos.org/download.html) installed.
- Clone repo & cd into it.
- Run: `nix-shell`
- Inside the shell run `gunicorn -w 4 -b 0.0.0.0:8080 wsgi:app` and visit http://localhost:8080/

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

[![](https://yt-embed.live/embed?v=3BYNj6Yvl8I)](http://www.youtube.com/watch?v=3BYNj6Yvl8I "Video Title")


```
[![](https://yt-embed.live/embed?v=3BYNj6Yvl8I)](http://www.youtube.com/watch?v=3BYNj6Yvl8I "Video Title")
```

## Deployment & Hosting

### systemd service

```
# cat /lib/systemd/system/yt-embed.service
[Unit]
Description=yt-embed

[Service]
Type=simple
Restart=always
RestartSec=5s
WorkingDirectory=/home/ubuntu/yt-embed
ExecStart=/home/ubuntu/.nix-profile/bin/nix-shell -I /home/ubuntu/.nix-defexpr/channels --run "gunicorn -w 4 -b 0.0.0.0:9070 wsgi:app"

[Install]
WantedBy=multi-user.target
```

### nginx config

```
$ cat /etc/nginx/sites-enabled/yt-embed
server {
    server_name yt-embed.live www.yt-embed.live;

    location / { 
        proxy_pass http://localhost:9070;
    }


    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/yt-embed.live/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/yt-embed.live/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot


}

server {
    if ($host = www.yt-embed.live) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    if ($host = yt-embed.live) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    server_name yt-embed.live www.yt-embed.live;
    listen 80;
    return 404; # managed by Certbot




}
```
