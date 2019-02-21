## To use slack messaging you must first setup slack messaging bot and capture api-key
## install the following packages pip install slackclient && pip install slacker

from slacker import Slacker

slack = Slacker('---Your Slack API Token---')

message = "Insert your message here"
slack.chat.post_message('#Development', message);
