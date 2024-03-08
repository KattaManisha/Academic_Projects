from flask import Flask, redirect, request, url_for, render_template
import requests
import os

app = Flask(__name__)

""" This is the NASA API Key generated """ """ Created the variable and saved the API KEY which are generated """
NASA_API_KEY = os.environ['NASA_API_KEY']

"""Routing to the Picture of the day """ 
@app.route('/apod',methods=["GET"]) 
def apod():

    """A request to the APOD is being made"""
    apod_url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    response = requests.get(apod_url)
    data = response.json()

    """ Relevant information is being extracted """
    title = data['title']
    explanation = data['explanation']
    image_url = data['url']

    """ Here the  APOD template will be rendered with the data that is being retrieved """
    return render_template('apod.html', title=title, explanation=explanation, image_url=image_url)

@app.route('/epic', methods=["GET"])
def epic():
    epic_url = f"https://api.nasa.gov/EPIC/api/natural?api_key={NASA_API_KEY}"
   
    response = requests.get(epic_url)
    data = response.json()

    # Extract relevant information from the EPIC API response
    if data:
        caption = data[0]['caption']
        date = data[0]['date']
        date_str = date[:10]  # Extract the first 10 characters
        # Replace the hyphens with slashes
        formatted_date = date_str.replace("-", "/")
        img = data[0]['image']
        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{formatted_date}/png/{img}.png"
        centroid_coordinates = data[0]['centroid_coordinates']
        attitude_quaternions = data[0]['attitude_quaternions']
        sun_j2000_position = data[0]['sun_j2000_position']
        lunar_j2000_position = data[0]['lunar_j2000_position']
    else:
        image_url = None
        caption = "No EPIC image available for today."

    return render_template('epic.html', caption=caption, image_url=image_url, date=date, centroid_coordinates=centroid_coordinates, attitude_quaternions=attitude_quaternions,sun_j2000_position=sun_j2000_position,lunar_j2000_position=lunar_j2000_position)


""" Routing to index which will help us to both the API"""
@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


""" Specifying the port number on which the server would listen to for incoming traffic"""
if __name__ == '__main__':
     app.run(debug=True)
