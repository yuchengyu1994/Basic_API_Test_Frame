#!/usr/bin/env python
# encoding: utf-8
# @author:Yuchengyu
# @time: 2022/7/15 0015 20:45
import requests
from common.config_utils import read_config


class CommonApi:
    def __init__(self):
        self.session=requests.session()
        self.hosts=read_config.get_url
        self.proxies={'http': 'http://127.0.0.1:7890',
                   'https': 'http://127.0.0.1:7890'}

    def get_access_token_api(self,grant_type,appid,secret):
        params={
            'grant_type':grant_type,
            'appid':appid,
            'secret':secret
        }
        response=self.session.get(
            url=self.hosts+'/cgi-bin/token',
            params=params,
            proxies = self.proxies
        )
        return response

    def get_access_token(self):
        response=self.get_access_token_api('client_credential',read_config.get_appid,read_config.get_secret)
        access_token=response.json()['access_token']
        return access_token

    def create_user_tag_api(self,access_token,tag_json):
        params = {
            'access_token': access_token,
        }
        json_data=tag_json
        response=self.session.post(url=self.hosts + '/cgi-bin/tags/create',
                              params=params,
                              json=json_data,
                              proxies=self.proxies)
        return response

    def delete_user_tag_api(self,access_token,tag_id_json):
        params = {
            'access_token': access_token,
        }
        json_data = tag_id_json
        response = self.session.post(url=self.hosts + '/cgi-bin/tags/delete',
                                     params=params,
                                     data=json_data.encode('utf-8'),
                                     proxies=self.proxies)
        return response
