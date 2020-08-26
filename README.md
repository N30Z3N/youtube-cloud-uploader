# YouTube Cloud Uploader
Web application to integrate YouTube with various cloud storage services. Your one-stop solution for downloading YouTube videos directly to Dropbox, Microsoft OneDrive, Google Drive or Amazon S3.

### Project setup

### Installation

```shell
pip install -r requirements.txt --no-cache-dir

pylint -f colorized main.py --disable=W

python -B main.py
```

```powershell
[Environment]::SetEnvironmentVariable("PYTHONDONTWRITEBYTECODE", "1", "Machine")

$env:FLASK_APP = "main"

$env:FLASK_ENV = "development"

$env:EXPLAIN_TEMPLATE_LOADING = $True

$env:TEMPLATES_AUTO_RELOAD = $True

$env:APPLICATION_ROOT = ""

flask run
```

### Docker Setup

```powershell
docker build --compress --rm -t youtube-cloud-uploader .

docker run -d -p 5000:5000 -n ytcu youtube-cloud-uploader
```

### Resources
- [Get Started With Django](https://realpython.com/get-started-with-django-1/)

- [Django Example Projects & Code](https://www.fullstackpython.com/django-code-examples.html)

- [Sending Emails With Python](https://realpython.com/python-send-email/)

- [How to Send an Email in Python](https://blog.mailtrap.io/sending-emails-in-python-tutorial-with-code-examples/)

- [Flask Mail](https://pythonhosted.org/Flask-Mail/)
