import os
import platform
import sys
import urllib.parse
import requests
import dropbox
import pytube
from flask import Flask, jsonify, request, render_template, redirect, abort

app = Flask(__name__)


global SAVE_PATH
SAVE_PATH = 'tmp'

@app.route('/')
def index():
    """ Render home page """
    return render_template('home.html', title="YouTube-Dropbox Uploader")

@app.route('/save', methods=['GET', 'POST'])
def process_video():
    """ Download YouTube videos """
    video_url = str(request.args.get('video_url'))
    dbx_access_token = request.args.get('access_token')

    if len(video_url) != 0:
        result = download_video(video_url)
    else:
        result = "No YouTube link provided."
    
    return render_template('default.html', response=result)

def download_video(video_url, dbx_access_token):
    """ """
    result_status = ""
    try:
        yt = pytube.YouTube(video_url)
        if not os.path.exists(SAVE_PATH):
            os.makedirs(SAVE_PATH)
        yt.streams.filter(subtype='mp4', progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if yt.length <= (30*60):
            yt.download(SAVE_PATH)
            result_status = upload_to_dropbox()
            if not result_status:
                result_status = "Your video has been uploaded to your Dropbox account."
        else:
            result_status = "Your video length is more than 30 minutes. Please either choose a video of length less than 30 minutes or pay a subtle amount via various payment methods."
        return result_status
    except ConnectionError:
        pass

def upload_to_dropbox(out_file, file_name, access_token):
    """ Upload to Dropbox """
    with dropbox.Dropbox(access_token) as dbx:
        try:
            dbx.users_get_current_account()
            dbx.files_upload(out_file, '/YouTube/{}'.format(file_name))
            return ""
        except dropbox.ApiError as err:
            if err.error.is_path() and err.error.get_path().reason.is_insufficient_space():
                return "ERROR: Cannot back up; insufficient space."
            elif err.user_message_text:
                return str(err.user_message_text)
            else:
                return str(err)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, ssl_context='adhoc')