# -*- coding: utf-8 -*-

##
# Module dependencies

import os.path
import json
import shutil
import requests


##
# Sends request to the Optidash API

def sendRequest(options):
    if 'errorMessage' in options:
        if 'toBuffer' in options:
            return options['errorMessage'], None, None
        else:
            return options['errorMessage'], None


    ##
    # Define empty headers hash wich will be injected
    # along with Requests parameters

    headers = {}


    ##
    # Set up HTTP proxy

    if 'proxy' in options:
        proxy = options['proxy']


    ##
    # Set the response mode to binary
    # and stream the response back
    # when dealing with Binary Responses

    if 'toFile' in options or 'toBuffer' in options:
        options['request']['response'] = {
            'mode': 'binary'
        }

        headers['X-Optidash-Binary'] = '1'
        stream = True


    ##
    # Use JSON request for fetch() mode

    if 'withFetch' in options:
        endpoint = 'https://api.optidash.ai/1.0/fetch'
        headers['Content-Type'] = 'application/json'


    ##
    # Use Multipart request for upload() mode

    if 'withUpload' in options:
        endpoint = 'https://api.optidash.ai/1.0/upload'

        if type(options['file']) is not str:
            file = options['file'].getvalue()
        else:
            if (os.path.isfile(options['file']) is False):
                error = 'Input file `' + options['file'] + '` does not exist'

                if 'toBuffer' in options:
                    return error, None, None
                else:
                    return error, None

            file = open(options['file'], 'rb')

        files = {
            'file': file
        }


    ##
    # Stringify processing parameters

    data = {
        'data': json.dumps(options['request'])
    }


    ##
    # Initiate POST request to the API

    r = requests.post(
        endpoint,
        auth = (options['key'], ''),
        headers = headers,
        files = files if 'files' in vars() else None,
        proxies = proxy if 'proxy' in vars() else None,
        stream = stream if 'stream' in vars() else False,
        data = data
    )


    ##
    # Parse the response body when dealing with toJSON() requests
    # and return the data to the user

    if 'toJSON' in options:
        try:
            response = r.json()
        except Exception as e:
            error = 'Unable to parse JSON response from the Optidash API'

            if 'toBuffer' in options:
                return error, None, None
            else:
                return error, None

        if response['success'] is False:
            error = response['message']

            if 'toBuffer' in options:
                return error, None, None
            else:
                return error, None

        return None, response


    ##
    # Try to parse JSON data from X-Optidash-Meta header

    try:
        meta = json.loads(r.headers['X-Optidash-Meta'])
    except Exception as e:
        error = 'Unable to parse JSON data from X-Optidash-Meta header'

        if 'toBuffer' in options:
            return error, None, None
        else:
            return error, None


    ##
    # Check whether the API call resulted with a failed response
    # and pass the error message to the user

    if meta['success'] is False:
        error = meta['message']

        if 'toBuffer' in options:
            return error, meta, None
        else:
            return error, meta


    ##
    # Stream incoming binary data to disk
    # when dealing with toFile() requests

    if 'toFile' in options:
        try:
            with open(options['outputPath'], 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        except Exception as e:
            error = 'Unable to save resulting image at `' + options['outputPath'] + '` location'

            if 'toBuffer' in options:
                return error, meta, None
            else:
                return error, meta

        return None, meta, None


    ##
    # Return raw data to the user
    # when dealing with toBuffer() requests

    if 'toBuffer' in options:
        r.raw.decode_content = True
        return None, meta, r.raw.data