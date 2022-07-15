"""Модуль содержит базовый код для сбора информации на конкретном сайте,
используя в качествен основы некий набор готовых тестовых данных.
В настоящей версии код заточен под один конкретный сайт.
В коде модуля имеется несколько классов перечислений,
которые соответствуют стратегиям: 
- работы с входными (базовыми) тестовыми данными;
- работы с конкретным вебсайтом;
- сохранения собранных данных.
Число различных стратегий ограничено, чтобы потратить время только на работу
с конкретным источником базовых данных и
с конкретным источником актуальных данных - с конкретным сайтом.
"""

import collections
import typing
import numpy as np
import pandas as pd
import pandas_mapper
import re
import lxml
import requests as rq
import requests_ip_rotator as rq_aws

from enum import Enum
from abc import ABC, abstractmethod

# ==================================================

class WebscraperError(Exception):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)

# ==================================================

class WrongDataMappersError(WebscraperError):
    def __init__(self, message=""):
        super().__init__(message)


class WrongDataError(WebscraperError):
    def __init__(self, message=""):
        super().__init__(message)


class WrongDataStrategyError(WebscraperError):
    def __init__(self, message=""):
        super().__init__(message)


class DataStrategyType(Enum):
    DATAFRAME = 1
    # JSON = 2


class AbstractDataStrategy(ABC):

    raw_data: pd.DataFrame = None
    raw_data_mappers = collections.OrderedDict()

    data = None

    def __init__(self, raw_data_mappers):
        if not raw_data_mappers:
            raise WrongDataMappersError(f"Please provide a non empty mapper map.")

        for mapper_name, mapper_instance in raw_data_mappers.items():
            raw_data_mappers[mapper_name] = mapper_instance

    def load_data(self, data_object) -> pd.DataFrame:
        self._check_data_object(data_object)
        self.raw_data = data_object
        self.data = self._load_data_impl(data_object)
        return self.data

    @abstractmethod
    def _check_data_object(self, data_object) -> None:
        pass

    @abstractmethod
    def _load_data_impl(self, data_object):
        pass


class DataFrameDataStrategy(AbstractDataStrategy):

    def __init__(self, raw_input_data_mappers: OrderedDict):
        super().__init__(raw_input_data_mappers)
        if not all(isinstance(mapper_name, str) for mapper_name in raw_input_data_mappers.keys()):
            raise WrongDataMappersError("All keys in the data mappers must be strings.")
        if not all(mapper_name != "" for mapper_name in raw_input_data_mappers.keys()):
            raise WrongDataMappersError("All keys in the data mappers must be non-empty strings.")
        for column_name, mapper_object in raw_input_data_mappers.items():
            if not isinstance(mapper_object, tuple):
                raise WrongDataMappersError("All mapper objects in the data mappers must be tuples; column name: {column_name}.")
            if len(mapper_object) != 3:
                raise WrongDataMappersError("All mapper objects in the data mappers must be tuples of size 3: (column_name, [target_columns], transform_function); column name: {column_name}.")
            if column_name != mapper_object[0]:
                raise WrongDataMappersError("The column name '{column_name}' is not equal to the source column name {mapper_object[0]} in the mapper object.")
            if isinstance(mapper_object[1], list):
                raise WrongDataMappersError("The second part of the mapper object must be a list; column name: {column_name}.")
            if isinstance(mapper_object[2], typing.Callable):
                raise WrongDataMappersError("The third part of the mapper object must be a row transforming function; column name: {column_name}.")

    def _check_data_object(self, data_object) -> None:
        if not isinstance(data_object, pd.DataFrame):
            raise TypeError(f"Input data object must be of type: {str(pd.DataFrame)}; actual type: {str(type(data_object))}")
        data_frame = data_object as pd.DataFrame
        if not all(column in data_frame.columns for column in self.raw_input_data_mappers.keys):
            raise WrongDataMappersError(
                    f"All columns of the data frame must be among the names of the raw input data mappers."
                )

    def _load_data_impl(self, data_frame: pd.DataFrame):
        data_columns_to_map = [column_name for column_name in self.raw_input_data_mappers]
        raw_data_to_map = data_frame[data_columns_to_map]

        mapping_rules = list()
        for column_name, mapper_object in self.raw_input_data_mappers.itemset():
            mapping_rules.append(mapper_object)

        new_input_data = raw_data_to_map.mapping(mapping_rules)
        return new_input_data


# ==================================================


DATA_STRATEGY_TYPES = {
    DataStrategyType.DATAFRAME: type(DataFrameDataStrategy)
}


def create_datastrategy(strategy_type: DataStrategyType, **kwargs) -> AbstractDataStrategy:
    if strategy_type in DATA_STRATEGY_TYPES:
        try:
            strategy_type_class = DATA_STRATEGY_TYPES[strategy_type]
            strategy = strategy_type_class(kwargs)
            return strategy
        except Exception as error:
            raise error
    else:
        raise WrongDataStrategyError(f"Wrong data strategy type: {strategy_type}.")


# ==================================================


class WebscraperWebengineType(Enum):
    PLAIN_REQUESTS = "requests"
    AWS_REQUESTS = "aws_requests"


# class AbstractWebengineDecorator(ABS):
#     def 


# ==================================================


class WrongWebscraperError(WebscraperError):
    def __init__(self, message=""):
        super().__init__(message)


class WebscraperStrategyType(Enum):
    AUTO_RU = 1


class AbstractWebscraperStrategy(ABC):
    input_strategy: AbstractDataStrategy = None
    output_strategy: AbstractDataStrategy = None

    input_data: pd.DataFrame = None
    output_data: pd.DataFrame = None

    web_engine_type: 


    def __init__(self, input_data_strategy: DataStrategyType, output_data_strategy: DataStrategyType):
        self.input_strategy = create_datastrategy(input_data_strategy)
        self.output_strategy = create_datastrategy(output_data_strategy)

    def load_input_data(self, data_object) -> pd.DataFrame:
        self.input_data = self.input_strategy.load_data(data_object)
        return self.input_data

    def load_output_data(self, data_object) -> pd.DataFrame:
        self.output_data = self.output_strategy.load_data(data_object)
        return self.output_data

    def scrap(website_url: str):



class AutoRuWebscraperStrategy(AbstractWebscraperStrategy):
    def __init__(self):
        super(AutoRuWebscraperStrategy, self).__init__()


# ==================================================


WEBSCRAPER_TYPES = {
    WebscraperStrategyType.AUTO_RU: type(AutoRuWebscraperStrategy)
}


def create_webscraper(strategy_type: WebscraperStrategyType, **kwargs) -> AbstractWebscraperStrategy:
    if strategy_type in WEBSCRAPER_TYPES:
        try:
            strategy_type_class = WEBSCRAPER_TYPES[strategy_type]
            strategy = strategy_type_class(kwargs)
            return strategy
        except Exception as error:
            raise error
    else:
        raise WrongWebscraperError(f"Wrong web-scrapper type: {strategy_type}.")


# ==================================================