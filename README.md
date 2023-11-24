# ChatYourCovidData
A simple webchat using pandasAI to talk to data. FastAPI as backend, HTMX for frontend.

## Try it out

You can try this app [here](https://chat-covid-data-86c873eec29c.herokuapp.com/).

## Try it locally

If you want to try it on your computer, open a terminal and do the following:

```bash
gh repo clone adrienB134/ChatYourCovidData
cd ChatYourCovidData/app/routes
wget https://opendata.ecdc.europa.eu/covid19/nationalcasedeath_eueea_daily_ei/csv/data.csv
cd ../..
source launch.sh
```

You need to have docker installed for it to work.

