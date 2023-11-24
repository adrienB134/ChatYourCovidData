# ChatYourCovidData
A simple webchat using pandasAI to talk to data. FastAPI as backend, HTMX for frontend.

![image](https://github.com/adrienB134/ChatYourCovidData/assets/102990337/060fcaeb-5922-4ab4-aa50-e7d8caaca02c)

## Overview
[PandasAI](https://docs.pandas-ai.com/en/latest/) is a Python library that adds Generative AI capabilities to pandas, it uses prompt engineering to query LLMs, such as OpenAI GPT4, to get it to write the code necessary to extract the information we want from a given dataframe (or even several dataframes). It even has a neat code debugging prompt where it tries to get the LLM to correct itself if the code generated fails. <br><br>
It works nicely in a notebook but I wanted to see if it could be used in a production app. After a bit of tweaking I got it to work and this is the resulting proof of concept.

## Try it out

You can try this app [here](https://chat-covid-data-86c873eec29c.herokuapp.com/).

## Try it locally
⚠️You need to have docker installed.

If you want to try it on your computer, open a terminal and do the following:<br><br>
⚠️Replace YOUR_OPENAI_KEY with your actual OpenAI API key.

```bash
gh repo clone adrienB134/ChatYourCovidData
cd ChatYourCovidData
echo OPENAI_KEY='YOUR_OPENAI_KEY' > .env
source launch.sh
```

Then open http://0.0.0.0:4000 in your favorite browser. 

