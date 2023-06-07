# plughook

## Webhook server for Kasa Smart Plugs

This project launches a webhook server that controls a Kasa smart plug. It's setup to handle a single plug, with only 2 ops - on & off. Why? My son has a nifty neon sign with his Twitch username hanging on his wall. He activates various scenes for his streams with a button on his Elgato Streamdeck. This integrates the control of that device.

You pass a few variables into the container, and have the option to set the hook names (ie you can use random strings to secure access). Check out the included example docker-compose file to see the details. Add an action to your buttons that load a web page in the background, drop in the URL for each of your webhooks, and boom, you're set.
