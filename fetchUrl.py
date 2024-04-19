import pycurl
from io import BytesIO

def fetch_url(url):
    buffer = BytesIO()
    curl = pycurl.Curl()

    # Set the URL to fetch
    curl.setopt(curl.URL, url)

    # Write the response data to the buffer
    curl.setopt(curl.WRITEDATA, buffer)

    try:
        # Perform the request
        curl.perform()

        # Get the HTTP response code
        response_code = curl.getinfo(curl.RESPONSE_CODE)
        if response_code == 200:
            pass
            # Successful response
            # print(f"Response:\n{buffer.getvalue().decode('utf-8')}")
        else:
            print(f"Error: HTTP {response_code}")
    except pycurl.error as e:
        print(f"Error: {e}")

    # Clean up
    curl.close()

# Usage
fetch_url("http://9.0.0.2/")
