import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/h0p3rwe/api/youtube-search-and-download'

mcp = FastMCP('youtube-search-and-download')

@mcp.tool()
def about_channel(id: Annotated[str, Field(description='Channel id')]) -> dict: 
    '''Return more info about channel'''
    url = 'https://youtube-search-and-download.p.rapidapi.com/channel/about'
    headers = {'x-rapidapi-host': 'youtube-search-and-download.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def channel(id: Annotated[Union[str, None], Field(description='Channel id.')] = None,
            next: Annotated[Union[str, None], Field(description="Pagination(continuation) parameter to get next channel video, no need any other parameters if 'next' present. Can be obtained from inside channel request result.")] = None,
            sort: Annotated[Union[str, None], Field(description='Sort parameter. Available options: n - newest; o - oldest; p - popular')] = None,
            filter: Annotated[Union[str, None], Field(description='Filter for live streams. Available options: l - live now; p - past live streams;')] = None) -> dict: 
    '''Channel videos'''
    url = 'https://youtube-search-and-download.p.rapidapi.com/channel'
    headers = {'x-rapidapi-host': 'youtube-search-and-download.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'next': next,
        'sort': sort,
        'filter': filter,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def video_related(id: Annotated[str, Field(description='Video id')],
                  hl: Annotated[Union[str, None], Field(description='Locale/language for request')] = None,
                  gl: Annotated[Union[str, None], Field(description='Country code like US(default), UK, BE, etc...')] = None,
                  next: Annotated[Union[str, None], Field(description="Pagination(continuation) parameter to get more related videos, no need any other parameters if 'next' present. Can be obtained from first response.")] = None) -> dict: 
    '''Get related videos'''
    url = 'https://youtube-search-and-download.p.rapidapi.com/video/related'
    headers = {'x-rapidapi-host': 'youtube-search-and-download.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'hl': hl,
        'gl': gl,
        'next': next,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def video_comments(id: Annotated[Union[str, None], Field(description='Video id to get first part of comments.')] = None,
                   next: Annotated[Union[str, None], Field(description='Pagination(continuation) parameter to get more comments , no need any other parameters if \'next\' present. Could be used for sorting, just pass "sortNewestNext" or "sortTopNext" field values for newest or top sorting. Can be obtained from response with "id" parameter in request')] = None) -> dict: 
    '''Get video comments list. If you need sorting then use "sortTopNext" or "sortNewestNext" fields from first response and pass it to "next" parameter.'''
    url = 'https://youtube-search-and-download.p.rapidapi.com/video/comments'
    headers = {'x-rapidapi-host': 'youtube-search-and-download.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'next': next,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def trending(type: Annotated[Union[str, None], Field(description='Type of trending videos: n - now (default) mu - music mo - movies g - gaming')] = None,
             hl: Annotated[Union[str, None], Field(description='Locale/language for request')] = None,
             gl: Annotated[Union[str, None], Field(description='Country from you want get trendings like US(default), UK, BE, etc...')] = None) -> dict: 
    '''Get list of trending videos'''
    url = 'https://youtube-search-and-download.p.rapidapi.com/trending'
    headers = {'x-rapidapi-host': 'youtube-search-and-download.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'type': type,
        'hl': hl,
        'gl': gl,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def video_info(id: Annotated[str, Field(description='Video id from YouTube')]) -> dict: 
    '''Get video info by id'''
    url = 'https://youtube-search-and-download.p.rapidapi.com/video'
    headers = {'x-rapidapi-host': 'youtube-search-and-download.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def playlist(id: Annotated[Union[str, None], Field(description='Playlist id')] = None,
             next: Annotated[Union[str, None], Field(description="Pagination(continuation) parameter to get more playlist items, no need any other parameters if 'next' present. Can be obtained from inside playlist request result.")] = None) -> dict: 
    '''Playlist videos'''
    url = 'https://youtube-search-and-download.p.rapidapi.com/playlist'
    headers = {'x-rapidapi-host': 'youtube-search-and-download.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'next': next,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def channels_playlists(query: Annotated[Union[str, None], Field(description='Search query you want to search')] = None,
                       next: Annotated[Union[str, None], Field(description="Pagination(continuation) parameter to get next result for same search query, no need any other parameters if 'next' present. Can be obtained from inside search result.")] = None,
                       hl: Annotated[Union[str, None], Field(description='Search language')] = None,
                       gl: Annotated[Union[str, None], Field(description='Search location')] = None,
                       upload_date: Annotated[Union[str, None], Field(description='Upload date filter. Available options: l - last hour; t - today; w - weak ago; m - month ago; y - year ago;')] = None,
                       type: Annotated[Union[str, None], Field(description='Search type. Available options: v - video; c - channel; p - playlist;')] = None,
                       duration: Annotated[Union[str, None], Field(description='Video duration. Available options: s - short; l - long;')] = None,
                       features: Annotated[Union[str, None], Field(description="Video features. Available options(could be joined by ';'): h - hdr; hd - hd; s - subtitles; c - cc; 3d - 3d; 3 - 360; li - live; lo - location; 4 - 4k;")] = None,
                       sort: Annotated[Union[str, None], Field(description='Result sort. Available options: r - relevance; ra - rating; u - upload date; v - view count;')] = None) -> dict: 
    '''Search any youtube content with all available filters'''
    url = 'https://youtube-search-and-download.p.rapidapi.com/search'
    headers = {'x-rapidapi-host': 'youtube-search-and-download.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'next': next,
        'hl': hl,
        'gl': gl,
        'upload_date': upload_date,
        'type': type,
        'duration': duration,
        'features': features,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
