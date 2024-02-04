# fritz-data-horder
Easy to use "No Code" Script-Creator for collecting and storing Fritz and HAN Fun Sensor Data in a SQLight Database



## Welcome!

👋 Welcome to the FritzBox Sensor Data Logger project. This tool is a solution for logging sensor data from your  Fritz and HAN-FUN devices into a  SQLite database. Whether you're a home automation enthusiast, a data hoarder, or just curious about your smart home, you're in the right place!

## What's This All About?

I´ve never been happy with the limited possibilitys inside the Fritz UI for logging and exporting your Sensor Data. The Fritz API is not Documented very well so i made the FritzBox Sensor Data Horder – a Python script designed to help  automatically log data from the smart devices. It uses the AHA (AVM Home Automation) HTTP interface to communicate with FritzBox routers, fetching  data from connected smart devices and storing them in a sqlite Database



## SQLite Database 

Why SQLite, you ask? Well, SQLite is a lightweight, yet powerful database engine that requires zero configuration, making it perfect for both beginners and pros. It stores all your data in a single file, which you can query with SQL to uncover trends or monitor device performance. It´s super easy to use without any knowledge of SQL.



## Getting Started

Here's how to embark on your data-hording mission:

### Prerequisites

- A FritzBox router with smart devices connected
- Python 3.x installed on your machine


### Step 1: Configuration Magic with `json_generator.html`

1. Open `json_generator.html` in your favorite browser. This form will guide you through generating your `fb_config.json` configuration file.
2. Fill in the blanks with your router's URL, credentials, the device AIN you're interested in, and how often you want to fetch data.
3. Hit "Generate Configuration" to download your personalized `fb_config.json` file. Voilà!


### Step 2: Running the Script

With your `fb_config.json` in hand, place it in the same directory as `fb_collect.py`, and run:

```bash
python fb_collect.py
````



## Deployment Scenarios

The script can be run in various environments, depending on your needs:

- **Laptop/Desktop:** Great for occasional logging. Just remember, it needs to stay awake.
- **Raspberry Pi:** Set up a dedicated logging station for continuous monitoring without breaking the bank.
- **Local Server:** Ideal for tech-savvy households with a server rack (or a closet doubling as one).
- **External Server:** For the adventurous, deploy it in the cloud. Note: This requires additional security measures.



## DIY Configuration

For those who know what they are doing, `fb_config.json` can be edited manually. This approach allows for custom commands and deeper customization. Check out the `json_generator.html` for command inspirations and refer to the [AHA-HTTP-Interface documentation](AHA-HTTP-Interface.pdf) for a complete command list.



### Example `fb_config.json`

```json
{
  "routerurl": "http://192.168.178.1",
  "username": "admin",
  "password": "verysecret",
  "device_ain": "0987654321",
  "command_cmd": "gettemperature",
  "interval": 300
}
```


## Closing Thoughts

Thank you for checking out the FritzBox Sensor Data Horder! Whether you're monitoring your home's temperature, keeping tabs on your energy consumption, or just playing with data, I hope this tool adds a little joy and a lot of insights to your smart home journey.

Contributions, ideas, and feedback are always welcome! Feel free to fork the project, open issues, or submit pull requests. If you have questions or just want to say hi, feel free to reach out.

Happy hording!

