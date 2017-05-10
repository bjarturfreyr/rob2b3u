raspivid -o - -t 0 -hf -vf -w 640 -h 360 -fps 24 --nopreview | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554}' :demux=h264
