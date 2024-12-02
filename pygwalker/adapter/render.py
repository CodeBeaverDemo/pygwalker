from pygwalker.adapter.utils import can_open_window, is_notebook
from pygwalker.api import repl, webview, jupyter
from typing import Optional, Union
from pygwalker._typing import DataFrame, IAppearance, IThemeKey
from pygwalker.data_parsers.database_parser import Connector

def render(
    dataset: Union[DataFrame, Connector, str],
    spec: str,
    *,
    theme_key: IThemeKey = 'g2',
    appearance: IAppearance = 'media',
    kernel_computation: Optional[bool] = None,
    kanaries_api_key: str = "",
    **kwargs
):
    """
    Args:
        - dataset (pl.DataFrame | pd.DataFrame | Connector, optional): dataframe.
        - spec (str): chart config data. config id, json, remote file url

    Kargs:
        - theme_key ('vega' | 'g2'): theme type.
        - appearance (Literal['media' | 'light' | 'dark']): 'media': auto detect OS theme.
        - kernel_computation(bool): Whether to use kernel compute for datas, Default to None.
        - kanaries_api_key (str): kanaries api key, Default to "".
    """
    
    if is_notebook():
        return jupyter.render(
            dataset,
            spec,
            theme_key=theme_key,
            appearance=appearance,
            kernel_computation=kernel_computation,
            kanaries_api_key=kanaries_api_key,
            **kwargs
        )
    elif can_open_window():
        return webview.render(
            dataset,   
            spec,
            theme_key=theme_key,
            appearance=appearance,
            kernel_computation=kernel_computation,
            kanaries_api_key=kanaries_api_key,
            **kwargs
        )
    else:
        return repl.render(
            dataset,   
            spec,
            theme_key=theme_key,
            appearance=appearance,
            kernel_computation=kernel_computation,
            kanaries_api_key=kanaries_api_key,
            **kwargs
        )

