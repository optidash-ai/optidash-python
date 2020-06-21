# -*- coding: utf-8 -*-

##
# Module dependencies

import json
import requests

from . import client


##
# Optidash class

class optidash(object):
    def __init__(self, key = None):
        self.options = {
            'key': key,
            'request': {}
        }

        if key is None or key is not key or type(key) is not str:
            self.options['errorMessage'] = 'Optidash constructor requires a valid API Key'


    ##
    # Uploads an image for processing
    #
    # @param {String|Buffer} file
    # @returns {Optidash}

    def upload(self, file = ''):
        if 'withFetch' in self.options:
            self.options['errorMessage'] = 'Optidash only accepts one file input method per call: upload(String|Buffer) or fetch(String)'

        if file is None or file is not file:
            self.options['errorMessage'] = 'Optidash upload(String|Buffer) method requires file path or a Buffer passed as an argument'
        else:
            self.options['withUpload'] = True
            self.options['file'] = file

        return self


    ##
    # Provides a URL of the image for processing
    #
    # @param {String} url
    # @returns {Optidash}

    def fetch(self, url = ''):
        if 'withUpload' in self.options:
            self.options['errorMessage'] = 'Optidash only accepts one file input method per call: upload(String|Buffer) or fetch(String)'

        if file is None or file is not file or type(url) is not str:
            self.options['errorMessage'] = 'Optidash fetch(String) method requires a valid file URL passed as an argument'
        else:
            self.options['withFetch'] = True
            self.options['url'] = file

        return self


    ##
    # Sets a proxy for HTTP requests
    #
    # @param {Dict} proxy
    # @returns {Optidash}

    def setProxy(self, proxy = {}):
        if proxy is not None and type(proxy) is dict:
            self.options['proxy'] = proxy

        return self


    ##
    # Optimizes an image
    #
    # @param {Dict} data
    # @returns {Optidash}

    def optimize(self, data = {}):
        if data is not None and type(data) is dict:
            self.options['request']['optimize'] = data

        return self


    ##
    # Flips an image
    #
    # @param {Dict} data
    # @returns {Optidash}

    def flip(self, data = {}):
        if data is not None and type(data) is dict:
            self.options['request']['flip'] = data

        return self


    ##
    # Optimizes an image
    #
    # @param {Dict} data
    # @returns {Optidash}

    def optimize(self, data = {}):
        if data is not None and type(data) is dict:
            self.options['request']['optimize'] = data

        return self


    ##
    # Resizes an image
    #
    # @param {Dict} data
    # @returns {Optidash}

    def resize(self, data = {}):
        if data is not None and type(data) is dict:
            self.options['request']['resize'] = data

        return self


    ##
    # Scales an image
    #
    # @param {Dict} data
    # @returns {Optidash}

    def scale(self, data = {}):
        if data is not None and type(data) is dict:
            self.options['request']['scale'] = data

        return self


    ##
    # Applies a watermark
    #
    # @param {Dict} data
    # @returns {Optidash}

    def watermark(self, data = {}):
        if data is not None and type(data) is dict:
            self.options['request']['watermark'] = data

        return self


    ##
    # Applies an elliptical mask
    #
    # @param {Dict} data
    # @returns {Optidash}

    def mask(self, data = {}):
        if data is not None and type(data) is dict:
            self.options['request']['mask'] = data

        return self


    ##
    # Applies a filter
    #
    # @param {Dict} data
    # @returns {Optidash}

    def filter(self, data = {}):
        if data is not None and type(data) is dict:
            self.options['request']['filter'] = data

        return self


    ##
    # Adjusts visual parameters
    #
    # @param {Dict} data
    # @returns {Optidash}

    def adjust(self, data = {}):
        if data is not None and type(data) is dict:
            self.options['request']['adjust'] = data

        return self


    ##
    # Automatically enhances an image
    #
    # @param {Dict} data
    # @returns {Optidash}

    def auto(self, data = {}):
        if data is not None and type(data) is dict:
            self.options['request']['auto'] = data

        return self


    ##
    # Applies a border to an image
    #
    # @param {Dict} data
    # @returns {Optidash}

    def border(self, data = {}):
        if data is not None and type(data) is dict:
            self.options['request']['border'] = data

        return self


    ##
    # Pads the image
    #
    # @param {Dict} data
    # @returns {Optidash}

    def padding(self, data = {}):
        if data is not None and type(data) is dict:
            self.options['request']['padding'] = data

        return self


    ##
    # Stores processed image externally
    #
    # @param {Dict} data
    # @returns {Optidash}

    def store(self, data = {}):
        if data is not None and type(data) is dict:
            self.options['request']['store'] = data

        return self


    ##
    # Sets output format and encoding
    #
    # @param {Dict} data
    # @returns {Optidash}

    def output(self, data = {}):
        if data is not None and type(data) is dict:
            self.options['request']['output'] = data

        return self


    ##
    # Sets a Webhook as a reponse delivery method
    #
    # @param {Dict} data
    # @returns {Optidash}

    def webhook(self, data = {}):
        if data is not None and type(data) is dict:
            self.options['request']['webhook'] = data

        return self


    ##
    # Sends a standard request to the API
    # and returns a JSON response
    #
    # @returns {String, Dict}

    def toJSON(self):
        if 'toFile' in self.options or 'toBuffer' in self.options:
            self.options['errorMessage'] = 'Optidash only accepts one response method per call: toJSON(), toFile(String) or toBuffer()'

        if 'withUpload' not in self.options and 'withFetch' not in self.options:
            self.options['errorMessage'] = 'No file input has been specified with either upload(String|Buffer) or fetch(String) method'

        self.options['toJSON'] = True

        return client.sendRequest(self.options)


    ##
    # Instructs the API to use a Binary Response
    # and streams the response to disk
    #
    # @param {String} path
    # @returns {String, Dict}

    def toFile(self, path = ''):
        if path is None or path is not path or type(path) is not str:
            self.options['errorMessage'] = 'Optidash toFile(String) method requires a valid output file path as a parameter'

        if 'toJSON' in self.options or 'toBuffer' in self.options:
            self.options['errorMessage'] = 'Optidash only accepts one response method per call: toJSON(), toFile(String) or toBuffer()'

        if 'webhook' in self.options['request']:
            self.options['errorMessage'] = 'Binary responses with toFile(String) method are not supported when using Webhooks'

        if 'store' in self.options['request']:
            self.options['errorMessage'] = 'Binary responses with toFile(String) method are not supported when using External Storage'

        if 'withUpload' not in self.options and 'withFetch' not in self.options:
            self.options['errorMessage'] = 'No file input has been specified with either upload(String|Buffer) or fetch(String) method'

        self.options['toFile'] = True
        self.options['outputPath'] = path

        return client.sendRequest(self.options)


    ##
    # Instructs the API to use a Binary Response
    # and returns a buffer to the user
    #
    # @param {Array} data
    # @returns {String, Dict, Buffer}

    def toBuffer(self):
        if 'toJSON' in self.options or 'toFile' in self.options:
            self.options['errorMessage'] = 'Optidash only accepts one response method per call: toJSON(), toFile(String) or toBuffer()'

        if 'webhook' in self.options['request']:
            self.options['errorMessage'] = 'Binary responses with toBuffer() method are not supported when using Webhooks'

        if 'store' in self.options['request']:
            self.options['errorMessage'] = 'Binary responses with toBuffer() method are not supported when using External Storage'

        if 'withUpload' not in self.options and 'withFetch' not in self.options:
            self.options['errorMessage'] = 'No file input has been specified with either upload(String|Buffer) or fetch(String) method'

        self.options['toBuffer'] = True

        return client.sendRequest(self.options)
